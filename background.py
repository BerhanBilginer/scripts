import os

def count_jpg_without_txt(jpg_directory, txt_directory):
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

    # Count the number of JPG files without corresponding TXT files
    jpg_without_txt = len(jpg_files - txt_files)
    return jpg_without_txt

if __name__ == "__main__":
    jpg_directory = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/output_umudum_kalmadi/train/images"
    txt_directory = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/output_umudum_kalmadi/train/labels"
    
    jpg_without_txt_count = count_jpg_without_txt(jpg_directory, txt_directory)
    print(f"Number of JPG files without corresponding TXT files: {jpg_without_txt_count}")