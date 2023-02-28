from FunctionInterfaces import FitnessFunctionInterface
from PIL import Image
import math

class CircleFitnessFunction(FitnessFunctionInterface):

    def calc_fitness(self, m : Image) -> float:
        pix = [] #Array of non-white pixel distances
        sz = m.size
        center = (sz[0]/2, sz[1]/2)
        band_size = 20 #amount of pixels in a given circle
        fitness = None
        
        #Calculate distance of all non-white pixels
        for x in range(sz[0]):
            for y in range(sz[1]):
                if m.getpixel((x,y)) != (255,255,255):
                    d = math.sqrt((x-center[0])**2 + (y-center[1])**2)
                    pix.append(d)   
                            
        #Sort to search
        pix.sort()
        
        #Calculate Fitness at given Bands
        for i in range(10, 50, band_size):
            all_pix = len(pix)
            num = 0 #number of pixels in a given band
            
            for dist in pix:    
                if dist >= i and dist < (i + band_size):
                    num += 1
            
            #calculate approximation of num pixels to fill this ring        
            approx_col = math.pi * (pow(i + band_size, 2) - pow(i ,2))
            int(approx_col)
            
            #approximate number of pixels that should be outside this ring
            approx_white = (m.size[0] * m.size[1]) - approx_col
                    
            cur_fit = (num / approx_col) - ((all_pix - num) / approx_white)
            #print("Band:", i, "Values: ", all_pix, num, cur_fit)
            
            if not fitness:
                fitness = cur_fit

            fitness = max(fitness, cur_fit)
        
        return fitness
    
    def is_neg(self):
        return True