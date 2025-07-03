import os

source_path = "/home/berhan/Desktop/zeg/area-violation/kuzeystar/labels/Grendook_cropped/"

for file in os.listdir(source_path):
    if file.endswith(".txt"):
        file_path = os.path.join(source_path, file)

        with open(file_path, 'r') as f:
            lines = f.readlines()

        filtered_lines = []
        for line in lines:
            line_parts = line.split()
            print(f"line part is {line_parts}")
            print(f"line part index 1 is {line_parts[1]}")
            if not line_parts[0] == 2:
                if not line_parts[1].startswith("0.38"):
                    filtered_lines.append(line)

        with open(file_path, 'w') as f:
            f.writelines(filtered_lines)