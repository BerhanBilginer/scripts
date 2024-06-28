import os

path = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/labeled/1.09.23_dataset_fire_detection"

label_mapping = {0: 1, 1: 0}

for filename in os.listdir(path):
    if filename.endswith(".txt"):
        file_path = os.path.join(path, filename)
    
        with open(file_path, "r") as f:
            lines = f.readlines()

        modified_lines = []
        for line in lines:
            parts = line.split()
            if len(parts) > 0 and parts[0] in ['0', '1']:
                old_label = int(parts[0])
                new_label = label_mapping[old_label]
                modified_line = f"{new_label} {' '.join(parts[1:])}\n"
                modified_lines.append(modified_line)
            else:
                modified_lines.append(line)
                
        with open(file_path, "w") as f:
            f.writelines(modified_lines)

        print(f"Labels in '{filename}' have been reconfigured.")
