import os
import argparse
import random

def delete_empty_txt_related_images(images_path, labels_path, deletion_probability):
    # List all the txt files in the labels_path
    txt_files = [f for f in os.listdir(labels_path) if f.endswith('.txt')]

    for txt_file in txt_files:
        txt_file_path = os.path.join(labels_path, txt_file)

        # Check if txt file is empty
        if os.path.getsize(txt_file_path) == 0:
            # Generate a random number between 0 and 1
            rand_num = random.random()

            # If the random number is less than or equal to the deletion_probability, delete the image and txt file
            if rand_num <= deletion_probability:
                # Form the corresponding image filename
                image_filename = txt_file.rsplit('.', 1)[0] + '.jpg'  # Assuming images are jpg. Change this if needed

                # Check if the corresponding image file exists in the images_path
                image_file_path = os.path.join(images_path, image_filename)
                if os.path.isfile(image_file_path):
                    # Delete the image file
                    os.remove(image_file_path)
                    print(f"Deleted: {image_file_path}")

                # Delete the txt file
                os.remove(txt_file_path)
                print(f"Deleted: {txt_file_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--images-path', type=str, required=True, help='Path to the images folder')
    parser.add_argument('--labels-path', type=str, required=True, help='Path to the labels folder')
    parser.add_argument('--deletion-probability', type=float, required=False, default=0.3, help='Probability of deleting an image file and its corresponding empty txt file')
    args = parser.parse_args()

    delete_empty_txt_related_images(args.images_path, args.labels_path, args.deletion_probability)