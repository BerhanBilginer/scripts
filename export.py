# The script gets five arguments from command line, first one is a path to a directory
# and the directory contains image files with bounding boxes in txt files with the same
# name as the image file. The script creates a new directory with the name provided as
# the second argument and converts to the YOLOv5 dataset format. The new directory contains
# train, test and valid directories with images and labels. The script also creates a
# data.yaml file with the class names and the number of classes. The third argument is the
# percentage of the images that will be used for training, the fourth argument is the
# percentage of the images that will be used for validation and the fifth argument is the
# percentage of the images that will be used for testing. Please note that the sum of the
# percentages must be 100. Also train, test and valid directories must be populated as
# evenly as possible with classes and background images.

# Usage: python export.py --input-dir <path to directory> --output-dir <name of new directory>
# --train-ratio <percentage> --val-ratio <percentage> --test-ratio <percentage>


import argparse
import os
import random
import shutil

import yaml


def get_all_files(directory):
    return [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]


def get_class_from_file(filename):
    with open(filename, "r") as file:
        for line in file:
            return line.split()[0]


def get_class_names(directory):
    txt_files = [
        f for f in get_all_files(directory) if f.endswith(".txt") and f != "classes.txt"
    ]
    bbox_classes = sorted(
        set(get_class_from_file(os.path.join(directory, f)) for f in txt_files)
    )
    classes_file = f"{directory}/classes.txt"
    if os.path.isfile(classes_file):
        with open(classes_file, "r") as file:
            class_names_from_file = [line.strip() for line in file]
    else:
        class_names_from_file = []

    # Convert to set for efficient membership tests
    bbox_classes_unique = sorted(list(set(bbox_classes)))

    # If class_names_from_file is empty, use bbox_classes
    class_names = class_names_from_file or bbox_classes_unique

    # Check that length of class_names is equal to number of classes
    if len(class_names) != len(bbox_classes_unique):
        raise ValueError(
            f"Number of classes in {directory} does not match number of classes in {classes_file}"
        )

    return class_names, bbox_classes_unique


def split_data(directory, class_names, train_ratio, valid_ratio, test_ratio):
    data_per_class = {class_name: [] for class_name in class_names}
    for filename in get_all_files(directory):
        if filename.endswith(".txt") and filename != "classes.txt":
            class_id = str(get_class_from_file(os.path.join(directory, filename)))
            data_per_class[class_id].append(filename.replace(".txt", ""))

    split_data = {
        class_name: {"train": [], "val": [], "test": []} for class_name in class_names
    }
    for class_name, filenames in data_per_class.items():
        random.shuffle(filenames)
        total = len(filenames)
        train_end = int(total * train_ratio)
        valid_end = train_end + int(total * valid_ratio)
        test_end = valid_end + int(total * test_ratio)

        split_data[class_name]["train"] = filenames[:train_end]
        split_data[class_name]["val"] = filenames[train_end:valid_end]
        split_data[class_name]["test"] = filenames[valid_end:test_end]

    return split_data


def copy_files(data, source_directory, dest_directory):
    for class_name, split_data in data.items():
        for split, filenames in split_data.items():
            if filenames:
                for filename in filenames:
                    shutil.copy2(
                        os.path.join(source_directory, f"{filename}.jpg"),
                        os.path.join(dest_directory, split, "images"),
                    )
                    shutil.copy2(
                        os.path.join(source_directory, f"{filename}.txt"),
                        os.path.join(dest_directory, split, "labels"),
                    )


def create_data_yaml(
    class_names, num_classes, new_directory, train_ratio, valid_ratio, test_ratio
):
    data = {}
    if train_ratio > 0:
        data["train"] = os.path.join(new_directory, "train", "images")
    if valid_ratio > 0:
        data["val"] = os.path.join(new_directory, "val", "images")
    if test_ratio > 0:
        data["test"] = os.path.join(new_directory, "test", "images")
    data["nc"] = num_classes
    data["names"] = {i: class_name for i, class_name in enumerate(class_names)}

    with open(os.path.join(new_directory, "data.yaml"), "w") as outfile:
        yaml.dump(data, outfile, default_flow_style=False, sort_keys=False)


def main(directory, new_directory, train_ratio, valid_ratio, test_ratio):
    class_names, bbox_classes = get_class_names(directory)
    num_classes = len(class_names)
    if train_ratio > 0:
        os.makedirs(os.path.join(new_directory, "train", "images"), exist_ok=True)
        os.makedirs(os.path.join(new_directory, "train", "labels"), exist_ok=True)
    if valid_ratio > 0:
        os.makedirs(os.path.join(new_directory, "val", "images"), exist_ok=True)
        os.makedirs(os.path.join(new_directory, "val", "labels"), exist_ok=True)
    if test_ratio > 0:
        os.makedirs(os.path.join(new_directory, "test", "images"), exist_ok=True)
        os.makedirs(os.path.join(new_directory, "test", "labels"), exist_ok=True)

    data = split_data(directory, bbox_classes, train_ratio, valid_ratio, test_ratio)

    copy_files(data, directory, new_directory)

    create_data_yaml(
        class_names, num_classes, new_directory, train_ratio, valid_ratio, test_ratio
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a directory of images and labels to YOLOv5 format."
    )
    parser.add_argument(
        "--input-dir", type=str, help="The directory containing the images and labels."
    )
    parser.add_argument(
        "--output-dir", type=str, help="The name of the new directory to create."
    )
    parser.add_argument(
        "--train-ratio",
        type=float,
        default=0.6,
        help="The ratio of images to use for training.",
    )
    parser.add_argument(
        "--val-ratio",
        type=float,
        default=0.2,
        help="The ratio of images to use for validation.",
    )
    parser.add_argument(
        "--test-ratio",
        type=float,
        default=0.2,
        help="The ratio of images to use for testing.",
    )

    args = parser.parse_args()

    main(
        args.input_dir,
        args.output_dir,
        args.train_ratio,
        args.val_ratio,
        args.test_ratio,
    )
