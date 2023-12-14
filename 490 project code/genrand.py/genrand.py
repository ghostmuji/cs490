from PIL import Image
import os
import random

for i in range(1, 50):

    q = random.randint(10, 50)
    image = Image.open('blorbo.jpg')
    image.save('blorbo.jpg', optimize=True, quality=q)

    if i % 100 == 0:  # Create a copy for every 5th image (can change)
        image_copy = image.copy()
        image_copy.save(f'blorbo_{i}_quality{q}.jpg', optimize=True, quality=10)