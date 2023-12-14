from PIL import ImageFilter, Image

for i in range(1, 5):
    img = Image.open('image.jpg')
    img = img.filter(ImageFilter.MaxFilter(3))
    img.save('image.jpg', optimize=True, quality=90)