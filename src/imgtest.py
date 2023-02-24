from PIL import Image  
import random
#testing PIL here
width = 200
height = 200
center = (width/2, height/2)
numpixels = 0
random.seed(random.randint(0,100000))
img  = Image.new( mode = "RGB", size = (width, height) )
#set each pixel to a random color
for x in range(width):
    for y in range(height):
        #generate a random color
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        img.putpixel( (x,y), (r, g, b) )
#check if pixels are white at a radius of 10 from the center
for x in range(width):
    for y in range(height):
        if (x-center[0])**2 + (y-center[1])**2 < 10**2:
            if img.getpixel( (x,y) ) != (255,255,255):
                numpixels += 1

print ("Number of pixels not white at radius 10 from center: ", numpixels)
img.show()
