import cv2
import time
import os
import threading

stream_data = [
    {"url": "rtsp://service:Dfds2023!@192.168.100.199:554/media/video1", "output_dir": "/home/berhan/Desktop/sahi/ultralytics/examples/YOLOv8-SAHI-Inference-Video/yelekk/video"}
]

def record_stream(stream_url, output_dir, recording_duration):
    try:
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

        while time.time() - start_time < recording_duration:
            ret, frame = cap.read()
            if not ret:
                print(f"Error reading frame from stream: {stream_url}")
                break
            out.write(frame)

            cv2.imshow("frame",frame)

            if time.time() - start_time >= recording_duration:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        print(f"Recording saved as {output_filename}")
    except Exception as e:
        print(f"Error during recording: {str(e)}")

recording_duration = 60 

threads = []
for stream_info in stream_data:
    url = stream_info["url"]
    output_dir = stream_info["output_dir"]

    os.makedirs(output_dir, exist_ok=True)

    thread = threading.Thread(target=record_stream, args=(url, output_dir, recording_duration))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All recordings completed.")