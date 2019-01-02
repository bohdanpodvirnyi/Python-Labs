import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_name = 'test.jpg'

# just open
image = Image.open(image_name)
arr = np.asarray(image)
plt.imshow(arr)
plt.show()

# more contrast
image = Image.open(image_name)
arr = np.asarray(image)
plt.imshow(arr, vmin=135, vmax=189)
plt.show()

# red
image = Image.open(image_name).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='Reds_r')
plt.show()

# green
image = Image.open(image_name).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='Greens_r')
plt.show()

# blue
image = Image.open(image_name).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='Blues_r')
plt.show()

# black and white
image = Image.open(image_name).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='gray')
plt.show()
