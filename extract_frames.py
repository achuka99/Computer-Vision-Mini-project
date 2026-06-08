import os
import subprocess

def extract_all_frames(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # List all mp4 files in the input directory
    video_files = [f for f in os.listdir(input_dir) if f.endswith('.mp4')]
    
    print(f"Found {len(video_files)} videos. Starting extraction...")
    
    for video in video_files:
        video_path = os.path.join(input_dir, video)
        video_name = os.path.splitext(video)[0]
        
        # Extract 1 frame per second
        # %03d will name them 001.jpg, 002.jpg etc.
        output_pattern = os.path.join(output_dir, f"{video_name}_%03d.jpg")
        
        command = [
            'ffmpeg', '-i', video_path,
            '-vf', 'fps=1',
            '-q:v', '2', # High quality
            output_pattern,
            '-y' # Overwrite if exists
        ]
        
        try:
            subprocess.run(command, check=True, capture_output=True)
            print(f"Successfully processed: {video}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {video}: {e}")

if __name__ == "__main__":
    # Change these paths if your videos are elsewhere
    input_folder = "/home/ubuntu/upload"
    output_folder = "/home/ubuntu/leaf_detection_project/full_dataset"
    
    extract_all_frames(input_folder, output_folder)
    print(f"\nDone! All frames are saved in: {output_folder}")
