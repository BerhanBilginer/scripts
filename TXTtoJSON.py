import os
import cv2
import numpy as np
from shapely.geometry import Polygon

# YOLO annotation directory and output directory
yolo_annotation_dir = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/output_umudum_kalmadi/test/labels_c/"
output_dir = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/output_umudum_kalmadi/test/pascal/"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def create_mask_image(bbox, image_width, image_height):
    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    cv2.rectangle(mask, (int(bbox[0]), int(bbox[1])), (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])), 255, -1)
    return mask

def create_polygon_coordinates(bbox):
    polygon = Polygon([
        (bbox[0], bbox[1]),
        (bbox[0] + bbox[2], bbox[1]),
        (bbox[0] + bbox[2], bbox[1] + bbox[3]),
        (bbox[0], bbox[1] + bbox[3])
    ])
    return list(polygon.exterior.coords)

# Iterate through YOLO annotation files
for filename in os.listdir(yolo_annotation_dir):
    if filename.endswith(".txt"):
        yolo_path = os.path.join(yolo_annotation_dir, filename)
        image_path = os.path.splitext(yolo_path)[0] + ".jpg"  # Assuming corresponding image file
        
        # Load the image to get its dimensions
        img = cv2.imread(image_path)
        image_height, image_width, _ = img.shape
        
        with open(yolo_path, "r") as yolo_file:
            lines = yolo_file.readlines()
            for line in lines:
                data = line.strip().split()
                class_id, x_center, y_center, width, height = map(float, data)
                
                # Convert YOLO coordinates to Pascal VOC coordinates
                x_min = (x_center - width / 2)
                y_min = (y_center - height / 2)
                x_max = (x_center + width / 2)
                y_max = (y_center + height / 2)
                
                bbox = (x_min * image_width, y_min * image_height, width * image_width, height * image_height)
                
                # Create mask image
                mask_image = create_mask_image(bbox, image_width, image_height)
                mask_filename = os.path.splitext(filename)[0] + "_mask.png"
                mask_path = os.path.join(output_dir, mask_filename)
                cv2.imwrite(mask_path, mask_image)
                
                # Create polygon coordinates
                polygon_coordinates = create_polygon_coordinates(bbox)
                
                # Save or use mask image and polygon coordinates as needed

print("Conversion complete.")
