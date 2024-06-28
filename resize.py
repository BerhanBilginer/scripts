import os
import cv2
import argparse

def resize_image(src, dst, extension, size):
    for filename in os.listdir(src):
        if filename.endswith(extension):
            img = cv2.imread(os.path.join(src, filename))
            if img is not None and not img.size == 0:
                resized_img = cv2.resize(img, size)
                cv2.imwrite(os.path.join(dst, filename), resized_img)
                print(f"{filename} resized to {size} from {img.shape}")
            else:
                print(f"Warning: Unable to read or empty image: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images in a directory.")
    parser.add_argument("--src", required=True, help="Source directory containing images.")
    parser.add_argument("--dst", required=True, help="Destination directory for resized images.")
    parser.add_argument("--extension", required=True, help="File extension of images to resize (e.g., '.jpg').")
    parser.add_argument("--width", type=int, required=True, help="Width of resized images.")
    parser.add_argument("--height", type=int, required=True, help="Height of resized images.")
    args = parser.parse_args()
    size = (args.width, args.height)
    resize_image(args.src, args.dst, args.extension, size)