import numpy as np

from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black pixels) with yellow pixels
# Homogeneous data types in array
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)
print("\nNew data\n")

# Make a red patch on rows 1 & 2 (3 is not included)
# data[row,column]
data[0:3, 0:2] = [255, 156, 244]
data[3:4, 1:4] = [45, 3, 244]

img = Image.fromarray(data, 'RGB')
img.save('image.png')