import cv2
import os

def get_frames(v_path, i_path, count=1, frame_rate=1):
    '''
    Explanation
    -----------
    * Captures and saves frames from the video at intervals based on the frame rate.
    
    Parameters
    -----------
    * v_path: The path of the video (Source) 
    * i_path: The path of the image (Destination)
    * count: Starting number for image file naming
    * frame_rate: Number of frames to skip before capturing a frame
    
    Returns
    -----------
    * Does not return anything
    '''
    folder_count = 1
    for video_name in os.listdir(v_path):
        if video_name.endswith('.mp4'):
            print(f"Processing {video_name} in folder {folder_count}")
            # Create a folder named after the video (without extension) to store its frames
            dst_path = os.path.join(i_path, os.path.splitext(video_name)[0])
            os.makedirs(dst_path, exist_ok=True)
            folder_count += 1
            cap = cv2.VideoCapture(os.path.join(v_path, video_name))
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            print(f"Total frames in video: {frame_count}")
            
            i = 0
            while i < frame_count:
                ret, frame = cap.read()
                if not ret:
                    print("Error reading frame or end of video reached.")
                    break
                
                if i % frame_rate == 0:
                    cv2.imwrite(os.path.join(dst_path, f"{video_name[:-4]}_{count}.jpg"), frame)
                    count += 1
                i += 1
                
            cap.release()
            print(f"Finished processing {video_name}")
            count = 1  # Reset count for the next video if needed

# Define video and image paths
video_path = '/home/berhan/Desktop/b_ai/lansman_video_creator/raw_data/videos/'
image_path = '/home/berhan/Desktop/b_ai/lansman_video_creator/raw_data/images/'

# Call the function to process the video
get_frames(video_path, image_path, count=1, frame_rate=1)