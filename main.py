from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

image1 = Image.open("cv.jpg")
image2 = Image.open("paris/paris_b.jpg")
plt.imshow(image1)
points1 = plt.ginput(2,timeout = 0, show_clicks=True)
plt.imshow(image2)
points2 = plt.ginput(10, timeout = 0, show_clicks=True)

with open('paris1-2_10points2.npy', 'wb') as f:
    np.save(f, np.array(points1))
    np.save(f, np.array(points2))
