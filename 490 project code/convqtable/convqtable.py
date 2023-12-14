from PIL import Image
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <image_file> <num_iterations>")
    sys.exit(1)

image_file = sys.argv[1]
num_iterations = int(sys.argv[2])

for i in range(1, num_iterations + 1):
    # Convert from the given image file
    image = Image.open(image_file).convert('RGB')
    image.save('image.webp', 'webp', optimize=True, quality=10)

    # Convert back to the image format (JPEG) from the webp file
    image = Image.open('image.webp').convert('RGB')
    image.save(image_file, "JPEG2000", codeblock="4x4", optimize=True, quality=50)

    if i % 20 == 0:  # Create a copy for every 5th image (can change)
        image_copy = image.copy()
        image_copy.save(f'Image_{i}.jp2', "JPEG2000", optimize=True, quality=50)
        print(i)
