from PIL import Image
import sys
import os
import subprocess

subprocess.run([
    'ffmpeg', '-y', '-framerate', '30', '-i', os.path.join('output', 'Image_%d.jpg'),
    '-c:v', 'libx264', '-r', '30', 'output_video.mp4'
])