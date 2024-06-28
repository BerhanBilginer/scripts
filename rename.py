import os

directory_path = "/home/berhan/Desktop/Development-Berhan/Test_Workspace/dataset/images"  # Replace with the actual path to your directory
extension_to_rename = ".jpg"  # Specify the file extension you want to rename

file_list = [file for file in os.listdir(directory_path) if file.endswith(extension_to_rename)]

for index, old_filename in enumerate(file_list, start=1):
    extension = old_filename.split(".")[-1]
    new_filename = f"{index}.{extension}"
    
    old_filepath = os.path.join(directory_path, old_filename)
    new_filepath = os.path.join(directory_path, new_filename)
    
    os.rename(old_filepath, new_filepath)
    print(f"Renamed '{old_filename}' to '{new_filename}'")