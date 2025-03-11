import os
import shutil

def organize_files(directory):
    # Define file type categories and their extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Others": []  # Catch-all for unclassified files
    }
    
    # Create the directory if it doesn’t exist
    if not os.path.exists(directory):
        print(f"Directory '{directory}' doesn’t exist!")
        return
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip if it’s a directory
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # Find the appropriate category for the file
        moved = False
        for category, extensions in file_types.items():
            if ext in extensions:
                destination_folder = os.path.join(directory, category)
                # Create the folder if it doesn’t exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                # Move the file
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved '{filename}' to '{category}'")
                moved = True
                break
        
        # If no category matches, move to "Others"
        if not moved:
            others_folder = os.path.join(directory, "Others")
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved '{filename}' to 'Others'")

# Example usage
if __name__ == "__main__":
    # Replace this with the path to the folder you want to organize
    target_directory = "C:/Users/YourUsername/Downloads"
    print(f"Organizing files in '{target_directory}'...")
    organize_files(target_directory)
    print("Done!")