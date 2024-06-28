import cv2
import time
import os
import threading

stream_data = [
    {"url": "rtsp://service:Dfds2023!@192.168.100.197:554/media/video1", "output_dir": "/home/berhan/Desktop/video_recorder/simultaneously_videos/197"},
    {"url": "rtsp://service:Dfds2023!@192.168.100.198:554/media/video1", "output_dir": "/home/berhan/Desktop/video_recorder/simultaneously_videos/198"},
    {"url": "rtsp://service:Dfds2023!@192.168.100.199:554/media/video1", "output_dir": "/home/berhan/Desktop/video_recorder/simultaneously_videos/199"},
]

def record_stream(stream_url, output_dir):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = os.path.join(output_dir, f"stream_{timestamp}.mp4")

    cap = cv2.VideoCapture(stream_url)
    if not cap.isOpened():
        print(f"Could not open stream: {stream_url}")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    out = cv2.VideoWriter(output_filename, fourcc, 60.0, frame_size)

    start_time = time.time()
    recording_duration = 5

    while time.time() - start_time < recording_duration:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    print(f"Recording saved as {output_filename}")

threads = []
for stream_info in stream_data:
    url = stream_info["url"]
    output_dir = stream_info["output_dir"]
    
    os.makedirs(output_dir, exist_ok=True)
    
    thread = threading.Thread(target=record_stream, args=(url, output_dir))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All recordings completed.")