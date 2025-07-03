import os

def remove_txt_files_with_only_one(folder_path):
    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a txt file
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            
            # Open the file and read its content
            try:
                with open(file_path, 'r') as file:
                    content = file.read().strip()
                    print(f"content: {content}")

                    # Check if the content is just '1'
                    if content == '1':
                        # Remove the file if the content is only '1'
                        os.remove(file_path)
                        print(f"Removed: {file_name}")
                    else:
                        print(f"There is nothing to remove.")
            except PermissionError as e:
                print(f"PermissionError: {e} for file {file_name}")

# Example folder path (replace with your actual path)
folder_path = "/home/berhan/Downloads/labels-20240914T173009Z-001/labels/"
remove_txt_files_with_only_one(folder_path)
