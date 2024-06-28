import os

directory = "/home/berhan/Desktop/vest_detecetion_last/augmented_data/process7"  # Change this to the directory containing your files
prefix = "pr7-"

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        new_filename = prefix + filename
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f'Renamed: {filename} to {new_filename}')