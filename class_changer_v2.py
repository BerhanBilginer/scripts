import os
def process_txt_files(folder_path):
    def adjust_starting_index(line):
        if line.startswith('0'):
            return '1' + line[1:]
        elif line.startswith('2'):
            return '3' + line[1:]
        elif line.startswith('4'):
            return '2' + line[1:]
        elif line.startswith('7'):
            return '0' + line[1:]
        return line
    def process_file(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [adjust_starting_index(line) for line in lines]
        with open(file_path, 'w') as file:
            file.writelines(lines)
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        process_file(file_path)
if __name__ == "__main__":
    folder_path = "/media/berhan/ÖZGÜN/PPE_DETECTION_DATA/new_data/data"
    process_txt_files(folder_path)