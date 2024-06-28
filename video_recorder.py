import cv2
import time

def videoRecorder():

    #source = input("Please enter the source of stream = ")
    #dst = str(input("Please enter the destination path where the stream log will be saved = "))

    source = 'rtsp://service:Dfds2023!@192.168.100.197:554/media/video1'
    dst = "/home/berhan/Desktop/video_recorder"

    cap = cv2.VideoCapture(source)
    
    if not cap.isOpened():
        print("Error: Couldn't reach to the stream.")
        exit()

    count = 0
    stream_name = "stream" + str(count) + ".mp4"

    output_path = dst + "/" + stream_name
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 60
    frame_size = (int(cap.get(3)), int(cap.get(4)))

    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    start_time = time.time()
    recording_time = 120

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        out.write(frame)

        cv2.imshow("Recording Stream", frame)

        if (time.time() - start_time) >= recording_time:
            count += 1
            start_time = time.time()
   
        if count == 2:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

videoRecorder()