import os

def delete_audio_files(directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has a .mp3 or .opus extension
            if file.endswith('.mp3') or file.endswith('.opus'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except OSError as e:
                    print(f"Error deleting {file_path}: {e}")

# Example usage
directory_path = "./PhoneBackup"
delete_audio_files(directory_path)
