import os
import shutil

label_path = "/home/berhan/Desktop/zeg/data-manipulation/Albumentations/rogar_mazgal_dataset/dataset/labels"
image_path = "/home/berhan/Desktop/zeg/data-manipulation/Albumentations/rogar_mazgal_dataset/dataset/images"
destination_path = "/home/berhan/Desktop/zeg/data-manipulation/Albumentations/rogar_mazgal_dataset/dataset/labels_with_0s"

# Create the destination directory if it doesn't exist
os.makedirs(destination_path, exist_ok=True)

for file in os.listdir(label_path):
    if file.endswith(".txt") and not file.startswith("process"):
        label_source = os.path.join(label_path, file)

        with open(label_source) as f:
            labels = f.readlines()

        # Check if all non-empty lines start with '0'
        only_zeros = all(label.strip().startswith('0') for label in labels if label.strip())

        if only_zeros:
            print(f"File contains only lines starting with '0': {file}")

            # Copy the text file to the destination directory
            shutil.copy(label_source, destination_path)
            
            # Find the corresponding image file (same name, different extension)
            image_name = os.path.splitext(file)[0] + ".jpg"  # Assuming images are .jpg, adjust if needed
            image_source = os.path.join(image_path, image_name)
            
            # Check if the image file exists before copying
            if os.path.exists(image_source):
                shutil.copy(image_source, destination_path)
                print(f"Copied {image_name} to {destination_path}")
            else:
                print(f"Image file {image_name} not found!")
