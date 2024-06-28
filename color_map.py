import cv2
import numpy as np

video_path = '/home/berhan/Downloads/f.mp4'
cap = cv2.VideoCapture(video_path)

# Create an empty canvas to store the color map
color_map = np.zeros((256, 256, 3), dtype=np.uint8)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Map the HSV values to the color_map
    for y in range(hsv_frame.shape[0]):
        for x in range(hsv_frame.shape[1]):
            h, s, v = hsv_frame[y, x]
            color_map[h, s] = (h, s, 255)  # Set the value of the color_map pixel
            
    cv2.imshow('Color Map', color_map)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()