from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

image1 = Image.open("paris/paris_b.jpg")
image2 = Image.open("paris/paris_c.jpg")
image1 = Image.open("mosaic2.jpg")
plt.imshow(image1)
points1 = plt.ginput(15,timeout = 0, show_clicks=True)
plt.imshow(image2)
points2 = plt.ginput(15, timeout = 0, show_clicks=True)
'''
with open('paris2-3_15points.npy', 'wb') as f:
    np.save(f, np.array(points1))
    np.save(f, np.array(points2))
'''