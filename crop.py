from PIL import Image 
import os

current_directory = os.getcwd()

output_folder = "out"
out_path = os.path.join(current_directory, output_folder)

folder_name = "image"
folder_path = os.path.join(current_directory, folder_name)
os.chdir(folder_path)



i = 1
# Loop through each file in the directory
for filename in os.listdir(folder_path):
    # Check if the file is an image (you may need more robust checks depending on your use case)
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Process your image here, for example, print its filename
        print("Processing image:", filename)

        im = Image.open(filename)
        width, height = im.size

        print('Width', width)
        print('Height', height)

        new_width = width * 0.5
        new_height = height * 0.5

        # Calculate the coordinates for cropping
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2

        # Crop the image
        im_cropped = im.crop((left, top, right, bottom))

        output = f"out_{i}.png"
        i += 1
        # Save the cropped image
        im_cropped.save(os.path.join(out_path, output))
