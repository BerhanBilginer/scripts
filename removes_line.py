import os
def remove_lines_starting_with_one(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Filtreleme: 1 ile başlayan satırları filtrele
    lines = [line for line in lines if not line.startswith('1')]
    with open(file_path, 'w') as file:
        file.writelines(lines)
def process_all_txt_files(folder_path):
    # Belirtilen klasördeki tüm .txt dosyalarını bul
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    # Her bir .txt dosyasını işle
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        remove_lines_starting_with_one(file_path)
if __name__ == "__main__":
    # Klasör yolunu belirtin
    folder_path = "/home/berhan/Desktop/Development-Berhan/Test_Workspace/dataset/work"
    # Tüm .txt dosyalarını işle
    process_all_txt_files(folder_path)