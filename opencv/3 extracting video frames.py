# Extracting Video Frames
import cv2
import os

video_path = 'D:/hridz4u/Youtube Videos Data Set/10_popnpop.mp4' 
output_directory = 'D:/hridz4u/Youtube Frames Data Set'
os.makedirs(output_directory, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_count = 0
desired_frames = 205 # Set the desired number of frames to extract
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # Get the total number of frames in the video
frame_interval = total_frames // desired_frames # Get the total number of frames in the video

while frame_count < total_frames:
    ret, frame = cap.read()
    if not ret:
        break

    # Only save frames at intervals determined by frame_interval
    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(output_directory, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)

    frame_count += 1

cap.release()
print(f'Total frames extracted: {frame_count}')

