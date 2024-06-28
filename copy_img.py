import os
import shutil

src = "/home/berhan/Desktop/vest_detecetion_last/augmented_data/process2"
dst = "/home/berhan/Desktop/vest_detecetion_last/augmented_data/process2/images"
src_path=os.listdir(src)

for file in src_path:
    if file.endswith(".jpg"):
        txt = shutil.copy((src + "/" + file),dst)
        #jpg = shutil.copy((src + "/" + file).replace(".txt",".jpg"),dst)

        print(f"{src}'dan {dst}'a kopyalandi.")