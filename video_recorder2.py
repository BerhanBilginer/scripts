import cv2
import time
import os

stream_url = "rtsp://service:Dfds2023!@192.168.100.197:554/media/video1"

output_directory = "/home/berhan/Desktop/video_recorder"
os.makedirs(output_directory, exist_ok=True)
while True:
    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    output_filename = os.path.join(output_directory, f"stream_{timestamp}.mp4")
    
    cap = cv2.VideoCapture(stream_url)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    out = cv2.VideoWriter(output_filename, fourcc, 60.0, frame_size)
    start_time = time.time()
    recording_duration = 1800
    while time.time() - start_time < recording_duration:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('Live Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Recording saved as {output_filename}")