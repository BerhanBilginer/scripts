import os
import shutil

file_path = "/media/berhan/Berhan/UBUNTU/PPE/VEST-DETECTION/vest_detection_v3.0.0/data/emended_dataset"
dest_path_1 = "/media/berhan/Berhan/UBUNTU/PPE/VEST-DETECTION/vest_detection_v3.0.0/data/vest_detection_dataset_26_09_23_alper"
dest_path_2 = "/media/berhan/Berhan/UBUNTU/PPE/VEST-DETECTION/vest_detection_v3.0.0/data/vest_detection_dataset_26_09_23_erdem"

cnt = 0
copied_files = []

for filename in os.listdir(file_path):
    if filename.endswith(".txt"):
        txt_path = os.path.join(file_path, filename)
        jpg_path = os.path.join(file_path, filename.replace(".txt", ".jpg"))

        if txt_path not in copied_files:
            # Copy the .txt and .jpg files to dest_path_1
            shutil.copy(txt_path, dest_path_1)
            shutil.copy(jpg_path, dest_path_1)
            copied_files.append(txt_path)

        cnt += 1

        if cnt == 28665:
            # Copy the .txt and .jpg files to dest_path_2
            shutil.copy(txt_path, dest_path_2)
            shutil.copy(jpg_path, dest_path_2)

        print(f"Copied: {txt_path} and {jpg_path} to dest_path_1")
        print(f"Count = {cnt}")

print(f"Finished copying to dest_path_1 and dest_path_2")
