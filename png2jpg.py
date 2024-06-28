from PIL import Image
import os

input_directory = "/home/berhan/Desktop/Augmentation/fire"  # Replace with the path to the directory containing PNG files
output_directory = "/home/berhan/Desktop/Augmentation"  # Replace with the path where you want to save JPG files

png_files = [file for file in os.listdir(input_directory) if file.lower().endswith(".png")]

for png_file in png_files:
    png_filepath = os.path.join(input_directory, png_file)
    jpg_filename = os.path.splitext(png_file)[0] + ".jpg"
    jpg_filepath = os.path.join(output_directory, jpg_filename)
    
    img = Image.open(png_filepath)
    img = img.convert("RGB")  # Convert to RGB before saving as JPG
    img.save(jpg_filepath, "JPEG")
    
    print(f"Converted '{png_file}' to '{jpg_filename}'")
