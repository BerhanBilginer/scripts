import os
import shutil

count=13
file_path = 'E:\\kamera_arka_images\\' + str(count) + '\\'
dest_path = 'E:\\kamera_arka_images\\dataset\\'

for cnt in range(13,24):
    file_path = 'E:\\kamera_arka_images\\' + str(count) + '\\'
for files in os.listdir(file_path):
    if files.endswith('.txt'):
        copied = shutil.copy((file_path+files),dest_path)
        print(copied)

    count+=1