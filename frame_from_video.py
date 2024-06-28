import cv2
import os

# Emniyet Kemeri için frame_rate 170
# Yoğunluk için frame rate 150
# Jetson için 3


def get_frames(v_path, i_path, count=1, frame_rate=2):
    '''
    Explanation
    -----------
    * Captures and saves footage from the video in seconds
    * For an infinite number of samples, the written algorithm runs in O(n^2)!

    Parameters
    -----------
    * v_path: The path of the video (Source) 
    * i_path: The path of tge image (Destination)
    * sec: Start seconds / Default = 0
    * count: Name of image for serial order / Default = 1
    * frame_rate: Number of frames per second  / Default = 0.8

    Returns
    -----------
    * Does not include returns
    '''
    # wh= (640, 480)
    i = 0
    folder_count = 1
    for video_name in os.listdir(v_path):
        if video_name.endswith('.mp4'):
            print(v_path + video_name)
            print(folder_count)
            dst_path = i_path +"/"+ str(len(os.listdir(i_path)) + 1) + "/"
            os.mkdir(dst_path)
            folder_count = folder_count + 1
            cap = cv2.VideoCapture(v_path+video_name)
            ret, frame = cap.read()
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            print(frame_rate, frame_count, fps, (frame_count / frame_rate))
            while i < frame_count:
                ret, frame = cap.read()
                if i % frame_rate == 0 and i < frame_count and frame is not None:
                    # frame_r = cv2.resize(frame, wh, interpolation=cv2.INTER_LINEAR)
                    #cropped_frame = frame[0:int(frame.shape[0]/2)]
                    # frame = cv2.rotate(frame, cv2.ROTATE_180)
                    cv2.imwrite(dst_path + str(video_name[:-4]) + str(count) + '.jpg', frame)
                    count = count + 1
                i = i + 1
                if i == int(frame_count) or ret == False:
                    print("Frame is over in current video.")
            cap.release()
            i = 0
    

video_path = '/home/berhan/Desktop/Development-Berhan/area-violation/distance-calculation/test_videos/basket/'
image_path = '/home/berhan/Desktop/Development-Berhan/area-violation/distance-calculation/test_images'

get_frames(video_path, image_path, count=1, frame_rate=30)