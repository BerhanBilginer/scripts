import cv2
import numpy as np

lower_color = np.array([0, 100, 100])
upper_color = np.array([30, 255, 255])

video_path = '/home/berhan/Downloads/f.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame, (640, 640))
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    color_map = cv2.cvtColor(hsv_frame, cv2.COLORMAP_HSV)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    for y in range(0, hsv_frame.shape[0], 10):
        for x in range(0, hsv_frame.shape[1], 10):
            hsv_value = hsv_frame[y, x]
            cv2.putText(frame, f"{hsv_value}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
    
    cv2.imshow('Flame Detection', frame)
    cv2.imshow('flame',hsv_frame)
    cv2.imshow('color_map',color_map)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()