import os
import shutil


def clsChooser(source_path,dest_path1, dest_path2):
    for files in os.listdir(source_path):
        if files.endswith(".txt"):
            with open(source_path + "/" + files) as f:
                line = f.read()
                line_0 = line[0]
                print(line_0)

            if line_0 == str(0) or str(1):
                txt = shutil.copy(source_path + "/" + files , dest_path1)
                jpg = shutil.copy((source_path + "/" + files).replace(".txt",".jpg"),dest_path1)

            
            elif line_0 == str(2) or str(3):
                txt = shutil.copy(source_path + "/" + files , dest_path2)
                jpg = shutil.copy((source_path + "/" + files).replace(".txt",".jpg"), dest_path2)

clsChooser(source_path="/media/berhan/Berhan/CukurSenaryo/06-07-23_dataset/deneme", dest_path1="/media/berhan/Berhan/CukurSenaryo/06-07-23_dataset/0_1_cls",dest_path2="/media/berhan/Berhan/CukurSenaryo/06-07-23_dataset/2_3_cls")

def clsDelete(source_path):
    for files in os.listdir(source_path):
        if files.endswith(".txt"):
            with open(source_path + "/" + files) as f:
                line = f.read()
                line_0 = line[0]
                print(line_0)