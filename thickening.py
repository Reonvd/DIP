import numpy as np
from skimage import morphology, io

# Load the binary image
image = io.imread('mypic.jpg', as_gray=True)

# Threshold the image to obtain a binary representation
threshold = 0.5
binary_image = image > threshold

# Define the structuring element for dilation
selem = morphology.square(3)  # Example: 3x3 square structuring element

# Perform thickening (dilation)
thickened_image = morphology.dilation(binary_image, selem)

# Save the thickened image
io.imsave('thickened_image.png', thickened_image.astype(np.uint8) * 255)
