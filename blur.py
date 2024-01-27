from PIL import Image, ImageFilter
import os

# Directories
input_dir = 'photos'
output_dir = 'blurred_photos'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):  # Check if the file is a PNG
        file_path = os.path.join(input_dir, filename)

        # Open the image
        with Image.open(file_path) as img:
            # Apply a blur filter
            blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))

            # Save the blurred image to the output directory
            blurred_img.save(os.path.join(output_dir, filename))

print("Blurring complete.")
