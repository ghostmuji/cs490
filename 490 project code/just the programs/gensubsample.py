from PIL import Image
import os
import random

for i in range(1, 800):

    q = (100 - (i // 10))

    image = Image.open('image.jpg')
    image.save('image.jpg', qtables="web_low", optimize=True, quality=q)

    if i % 100 == 0:  # Create a copy for every 5th image (can change)
        image_copy = image.copy()
        image_copy.save(f'Image_{i}_quality{q}.jpg', optimize=True, quality=50)