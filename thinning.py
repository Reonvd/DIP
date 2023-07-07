import numpy as np
from skimage import morphology, io

# Load the binary image
image = io.imread('binary_image.png', as_gray=True)

# Threshold the image to obtain a binary representation
threshold = 0.5
binary_image = image > threshold

# Perform thinning (skeletonization)
thinned_image = morphology.skeletonize(binary_image)

# Save the thinned image
io.imsave('thinned_image.png', thinned_image.astype(np.uint8) * 255)
