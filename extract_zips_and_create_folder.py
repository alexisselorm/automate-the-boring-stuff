import os
import zipfile
import shutil
import time

def extract_zip_files(source_dir):
    """
    Extracts all .zip files in the specified directory.
    """
    for filename in os.listdir(source_dir):
        if filename.endswith(".zip"):
            zip_path = os.path.join(source_dir, filename)
            extract_path = os.path.join(source_dir, os.path.splitext(filename)[0])
            print(f"Extracting {filename} to {extract_path}...")
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

def move_ipynb_files(source_dir, target_dir):
    """
    Moves all .ipynb files from the source directory (and subdirectories) to the target directory.
    """
    os.makedirs(target_dir, exist_ok=True)
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".ipynb"):
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, file)
                print(f"Moving {file} to {target_path}...")
                
                shutil.move(source_path, target_path)

def delete_zip_files(source_dir):
    """
    Deletes all .zip files in the specified directory with error handling.
    """
    for filename in os.listdir(source_dir):
        if filename.endswith(".zip"):
            zip_path = os.path.join(source_dir, filename)
            try:
                print(f"Deleting {filename}...")
                os.remove(zip_path)
                time.sleep(0.1)  # Short delay to ensure file is unlocked
            except PermissionError:
                print(f"Permission denied for {filename}. Retrying...")
                time.sleep(1)  # Wait a bit before retrying
                try:
                    os.remove(zip_path)
                except PermissionError:
                    print(f"Could not delete {filename} due to permission issues.")

# Example usage
source_directory = "."
target_directory = ".\Classes"

# Extract all zip files
# extract_zip_files(source_directory)

# Move all .ipynb files to the target directory
# move_ipynb_files(source_directory, target_directory)

delete_zip_files(source_directory)