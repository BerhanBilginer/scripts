import os

def formConverter(src):
    for filename in os.listdir(src):
        if filename.endswith(".txt"):
            filepath = os.path.join(src, filename)
            with open(filepath, "r") as f:
                lines = f.readlines()

            with open(filepath, "w") as f:
                for line in lines:
                    parts = line.strip().split()
                    print(f"{parts} before from pop out \n")
                
                    poped_outed = parts.pop()
                    print(f"the {poped_outed} is poped out \n")

                    print(f"{parts} after from pop out \n")

                    new_line = " ".join(parts)
                    print(f"reunited: {new_line}")

                    f.write(new_line + "\n")

formConverter(src="/home/berhan/Desktop/Development-Berhan/Metrics_Structures/test/mmdet/detected_images_plotted_txt")