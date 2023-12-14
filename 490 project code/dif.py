# import module 
from PIL import Image, ImageChops 
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <image1_file> <image2_file>")
    sys.exit(1)

image1_file = sys.argv[1]
image2_file = sys.argv[2]
  
# assign images 
img1 = Image.open(image1_file) 
img2 = Image.open(image2_file) 
  
# finding difference 
diff = ImageChops.difference(img1, img2) 
  
# showing the difference 
diff.show() 