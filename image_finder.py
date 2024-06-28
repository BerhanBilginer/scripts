import os
from PIL import Image
import imagehash

# Function to calculate the hash of an image
def calculate_image_hash(image_path):
    with Image.open(image_path) as img:
        hash_val = imagehash.average_hash(img)
    return str(hash_val)

# Function to check if an image hash exists in a folder
def image_exists_in_folder(image_hash, folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if calculate_image_hash(file_path) == image_hash:
                return True
    return False

if __name__ == "__main__":
    # Path to the image you want to check
    image_to_check_path = "/home/berhan/Desktop/513.jpg"

    # Path to the folder where you want to search for the image
    search_folder = "/home/berhan/Desktop/Augmentation/augmented_fire_data/process5/img"

    image_hash_to_check = calculate_image_hash(image_to_check_path)

    if image_exists_in_folder(image_hash_to_check, search_folder):
        print("Image exists in the folder.")
    else:
        print("Image does not exist in the folder.")