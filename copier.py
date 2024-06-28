import os
import shutil

count = 5
file_path_origin = '/media/berhan/Berhan/28-07-jetsondan-gelenler/region0/camera197/2023-07-28/'+str(count)+'/detected_images_not_plotted/'
dest_path_origin = "/media/berhan/Berhan/28-07-jetsondan-gelenler/region0/camera197/197-dataset"

for cnt in range(0,100):
    file_path_origin = '/media/berhan/Berhan/28-07-jetsondan-gelenler/region0/camera197/2023-07-28/'+str(count)+'/detected_images_not_plotted/'
    for files in os.listdir(file_path_origin):    
        if files.endswith(".jpg") and not files.startswith("classes"):
            txt = shutil.copy(file_path_origin + files, dest_path_origin)
            #jpg = shutil.copy((file_path_origin+files).replace(".txt",".jpg"),dest_path_origin)
    count+=1

    print(file_path_origin)