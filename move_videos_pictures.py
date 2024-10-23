import os
import shutil

# Define image and video extensions
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
VIDEO_EXTENSIONS = ('.mp4', '.mkv', '.avi', '.mov', '.wmv','.3gp')

def move_files_to_folders(directory):
    # Create target folders for pictures and videos if they don't exist
    pictures_folder = os.path.join(directory, 'newly_created_pictures')
    videos_folder = os.path.join(directory, 'newly_created_videos')
    
    os.makedirs(pictures_folder, exist_ok=True)
    os.makedirs(videos_folder, exist_ok=True)

    # Traverse through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        # Skip moving if we're already in the pictures or videos folder
        if root in [pictures_folder, videos_folder]:
            continue
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # Check if the file is an image
            if file.lower().endswith(IMAGE_EXTENSIONS):
                new_path = os.path.join(pictures_folder, file)
                shutil.move(file_path, new_path)
                print(f"Moved: {file} -> pictures/")
            
            # Check if the file is a video
            elif file.lower().endswith(VIDEO_EXTENSIONS):
                new_path = os.path.join(videos_folder, file)
                shutil.move(file_path, new_path)
                print(f"Moved: {file} -> videos/")

# Example usage
directory_path = "./PhoneBackup"
move_files_to_folders(directory_path)
