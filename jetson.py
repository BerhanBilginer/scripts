import os
import argparse
import shutil

def copy_jpg_and_txt(src, dest):

    for kamera in os.listdir(src):
        print(f"--> {kamera}")
        for gun in os.listdir(src + "/" + kamera):
            print(f"    --> {gun}")
            for saat in os.listdir(src + "/" + kamera + "/" + gun):
                print(f"        --> {saat}")
                for data in os.listdir(src + "/" + kamera + "/" + gun + "/" + saat):
                    print(f"            --> {data}")
                    
                    if data == "detected_images_not_plotted":
                        for img in os.listdir(src + "/" + kamera + "/" + gun + "/" + saat + "/" + data):
                                if img.endswith(".jpg"):
                                    shutil.copy((src + "/" + kamera + "/" + gun + "/" + saat + "/" + data + "/" + img), dest)

                    if data == "detected_images_plotted_txt":
                        for txt in os.listdir(src + "/" + kamera + "/" + gun + "/" + saat + "/" + data):
                                if txt.endswith(".txt"):
                                    shutil.copy((src + "/" + kamera + "/" + gun + "/" + saat + "/" + data + "/" + txt), dest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy JPG and TXT files from specified directories.")
    parser.add_argument("--src", required=True, help="Source directory to search for specified directories.")
    parser.add_argument("--dest", required=True, help="Destination directory to store images and labels.")
    args = parser.parse_args()
    copy_jpg_and_txt(args.src, args.dest)