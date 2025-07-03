import os
import shutil

images_src = "/home/berhan/Desktop/datasets/dataset2/images"
labels_src = "/home/berhan/Desktop/datasets/dataset2/test"
dst = "/home/berhan/Desktop/datasets/dataset2/test"

for image_file in os.listdir(images_src):
    if image_file.endswith(".jpg"):
        image_name = os.path.splitext(image_file)[0]
        label_file = image_name + ".txt"

        image_src_path = os.path.join(images_src, image_file)
        label_src_path = os.path.join(labels_src, label_file)
        image_dst_path = os.path.join(dst, image_file)
        label_dst_path = os.path.join(dst, label_file)

        if os.path.isfile(label_src_path):
            shutil.copy(image_src_path, image_dst_path)
            shutil.copy(label_src_path, label_dst_path)
            print(f"Copied: {image_file} and {label_file}")
        else:
            print(f"No label for {image_file}")