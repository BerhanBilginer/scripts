import os

def find_and_rename_images_without_labels(jpg_directory, txt_directory):
    jpg_files = set()
    txt_files = set()

    # Collect the names of all JPG files in the JPG directory
    for filename in os.listdir(jpg_directory):
        if filename.lower().endswith('.jpg'):
            jpg_files.add(filename[:-4])  # Remove the '.jpg' extension
    
    # Collect the names of all TXT files in the TXT directory
    for filename in os.listdir(txt_directory):
        if filename.lower().endswith('.txt'):
            txt_files.add(filename[:-4])  # Remove the '.txt' extension

    # Find JPG files without corresponding TXT files
    jpg_without_txt = jpg_files - txt_files
    
    # Rename the JPG files without labels with a count starting from 1
    count = 1
    for filename in jpg_without_txt:
        old_path = os.path.join(jpg_directory, filename + '.jpg')
        new_filename = f"image_without_label_{count}.jpg"
        new_path = os.path.join(jpg_directory, new_filename)
        
        os.rename(old_path, new_path)
        count += 1
    
    return len(jpg_without_txt)

if __name__ == "__main__":
    jpg_directory = "/media/berhan/Berhan/segmente_data/images"
    txt_directory = "/media/berhan/Berhan/segmente_data/labels"
    
    jpg_without_txt_count = find_and_rename_images_without_labels(jpg_directory, txt_directory)
    print(f"Number of JPG files without corresponding TXT files: {jpg_without_txt_count}")
