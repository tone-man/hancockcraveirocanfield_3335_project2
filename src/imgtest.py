from PIL import Image  
import random
import math
#testing PIL here
width = 200
height = 200
center = (width/2, height/2)
dfc = []
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
#check if pixels are white
for x in range(width):
    for y in range(height):
        if img.getpixel((x,y)) != (255,255,255):
            d = math.sqrt((x-center[0])**2 + (y-center[1])**2)
            dfc.append(d)
dfc.sort()
fits = []
n = 5
for i in ([n*x for x in range(10,21)]):
  dlen = len(dfc)
  num = dfc.count(i)
  fitnesshere = num - (dlen - num)
  fits.append(fitnesshere)
  
fitness = max(fits)
print(fitness)