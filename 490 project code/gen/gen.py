from PIL import Image
import os
import random

for i in range(1, 1001):

    q = random.randint(70, 80)
    image = Image.open('image.jpg')
    image.save('image.jpg', optimize=True, quality=q)

    if i % 100 == 0:  # Create a copy for every 5th image (can change)
        image_copy = image.copy()
        image_copy.save(f'Image_{i+500}.jpg', optimize=True, quality=80)