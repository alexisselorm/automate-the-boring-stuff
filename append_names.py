import os

def append_name_to_files(directory, append_name):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Get the full file path
        file_path = os.path.join(directory, filename)
        
        # Ensure it is a file, not a directory
        if os.path.isfile(file_path):
            # Split filename into name and extension
            name, ext = os.path.splitext(filename)
            
            # Create new file name by appending the name before the extension
            new_filename = f"{name}_{append_name}{ext}"
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Example usage
directory_path = ".\judekm"
append_name_to_files(directory_path, "jude")
