import os
import random
import shutil

def copy_images_without_duplicates(src, dst, exclude_folders, num_images_to_copy):
    source_image_files = set(file.lower() for file in os.listdir(src) if file.lower().endswith((".jpg", ".jpeg", ".png")))

    for exclude_folder in exclude_folders:
        exclude_image_files = set(file.lower() for file in os.listdir(exclude_folder) if file.lower().endswith((".jpg", ".jpeg", ".png")))
        source_image_files -= exclude_image_files

    source_image_files = list(source_image_files)
    random.shuffle(source_image_files)

    images_to_copy = source_image_files[:num_images_to_copy]

    for image_file in images_to_copy:
        source_filepath = os.path.join(src, image_file)
        destination_filepath = os.path.join(dst, image_file)

        shutil.copyfile(source_filepath, destination_filepath)
        print(f"Copied '{image_file}' to '{dst}'")

src = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/17.08.23_yangin_goruntuleri/dataset"  
dst = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/17.08.23_yangin_goruntuleri/berhan"  
exclude_folders = ["/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/17.08.23_yangin_goruntuleri/dataset_of_boys/alper", "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/17.08.23_yangin_goruntuleri/dataset_of_boys/erdem"
       , "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/17.08.23_yangin_goruntuleri/dataset_of_boys/yunus","/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/17.08.23_yangin_goruntuleri/umut"]  # Replace with the paths to the folders to exclude
num_images_to_copy = 1282  

copy_images_without_duplicates(src, dst, exclude_folders, num_images_to_copy)