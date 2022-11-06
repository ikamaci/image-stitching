from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

image1 = Image.open("paris/paris_a.jpg")
image2 = Image.open("paris/paris_b.jpg")
plt.imshow(image1)
points1 = plt.ginput(5,timeout = 0, show_clicks=True)
plt.imshow(image2)
points2 = plt.ginput(5, timeout = 0, show_clicks=True)

with open('paris1-2.npy', 'wb') as f:
    np.save(f, np.array(points1))
    np.save(f, np.array(points2))