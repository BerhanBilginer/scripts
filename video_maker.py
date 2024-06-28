import cv2
import os

# Define the path to your images and the output video file
image_folder = '/home/berhan/Desktop/Development-Berhan/c/content/c/vis'
output_video = '2.mp4'

# Define the frame rate (number of frames per second)
frame_rate = 1  # Adjust as needed

# Get a list of all image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

# Sort the images based on their filename
images.sort()

# Get the dimensions of the first image to set the video size
img = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = img.shape

# Create a VideoWriter object to write the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed
out = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

# Iterate through the images and add them to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    out.write(frame)

# Release the video writer and close the video file
out.release()

print(f"Video created: {output_video}")
