from PIL import Image 

im = Image.open('frame_2.jpg')
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

# Save the cropped image
im_cropped.save('cropped_Chicken.png')