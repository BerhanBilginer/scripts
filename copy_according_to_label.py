import os
import shutil
import argparse

def LabelCopier(label_source, dest):
    for label in os.listdir(label_source):
        if label.endswith(".txt"):
            with open(os.path.join(label_source, label), 'r') as f:
                rows = f.readlines()

                if rows and rows[0].strip().startswith("1"):
                    shutil.copy(os.path.join(label_source, label), dest)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--label_source', type=str, required=True, help='Label path')
    parser.add_argument('--dest', type=str, required=True, help='Cropped save path.')
    args = parser.parse_args()

    LabelCopier(args.label_source, args.dest)
