If you want to just the programs without viewing my outputs, download "just the programs" folder

Most programs have the command line usage: 
/[program.py] image.png [number of loops]

Happy moshing!

----List of Programs----
com.py has a loop to half the size of an image. by default, it does this 5 times.

conv.py has a loop to convert an jpg > webp > jpg, a given number of times [my personal favorite]

convqtable.py is the same as conv.py, but has an added qtable parameter for the JPEG

convresize.py is the same as conv.py, but doubles the size of the image when saving as JPEG and shrinks by half when saving as WEBp

dil.py uses the dilate function of the pillow library on an image

dif.py uses .spot function of pillow library to compare 2 images

exp.py has a loop to double the size of an image. by default, it does this 5 times.

gen.py has a loop to save a jpeg 600 at a random quality between 10-100 each time

gendec.py is the same thing but instead of random quality, quality starts at 100 and decreases by 10 every 100th loop

genrand.py saves a JPEG in a loop, but at a random quality level between 10 and 100 each time

gensubsample.py is the same as gendec.py but with an added subsampling parameter for the JPEG

rotate.sh: saves a jpeg x number of times rotating 90 every generation. found on wikimedia commons uploaded by user Burmy https://commons.wikimedia.org/wiki/File:JPEG_Generation_Loss_rotating_90_(stitch_of_0,100,200,500,900,2000_times).png

vid.py is a program to make a video of each generated frame from a program