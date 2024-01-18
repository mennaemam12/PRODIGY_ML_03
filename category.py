import os
import shutil

# Specify the path to the folder containing the images
folder_path = 'dogs-vs-cats/train/train'

# Create subdirectories if they don't exist
cat_subdirectory = os.path.join(folder_path, 'cats')
dog_subdirectory = os.path.join(folder_path, 'dogs')

os.makedirs(cat_subdirectory, exist_ok=True)
os.makedirs(dog_subdirectory, exist_ok=True)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if the file name contains "cat" and move it to the 'cats' subdirectory
    if 'dog' in filename.lower():
        shutil.move(file_path, os.path.join(dog_subdirectory, filename))
        print(f'Moved {filename} to dogs subdirectory.')
