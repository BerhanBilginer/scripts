import os
import random
import shutil

def copy_random_images(src, dst, num_images_to_copy_per_folder):
    image_files = [file for file in os.listdir(src) if file.lower().endswith((".jpg", ".jpeg", ".png"))]

    if num_images_to_copy_per_folder * len(dst) > len(image_files):
        print("Not enough images to copy.")
        return

    random.shuffle(image_files)

    for dest_folder in dst:
        images_to_copy = random.sample(image_files, num_images_to_copy_per_folder)
        
        for image_file in images_to_copy:
            source_filepath = os.path.join(src, image_file)
            destination_filepath = os.path.join(dest_folder, image_file)

            shutil.copyfile(source_filepath, destination_filepath)
            print(f"Copied '{image_file}' to '{dest_folder}'")

            image_files.remove(image_file)  

src = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/25.08.23_gece_testi/images/images"  
dst = ["/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/25.08.23_gece_testi/images/29.08.23_alper_fire_detection_dataset", 
       "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/25.08.23_gece_testi/images/29.08.23_erdem_fire_detection_dataset"]  
num_images_to_copy_per_folder = 4137

copy_random_images(src, dst, num_images_to_copy_per_folder)
