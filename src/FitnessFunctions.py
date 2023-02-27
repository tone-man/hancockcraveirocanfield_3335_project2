from FitnessFunctionInterface import FitnessFunctionInterface
from PIL import Image
import math

class CircleFitnessFunction(FitnessFunctionInterface):

    def calc_fitness(self, m : Image) -> float:
        dfc = []
        fits = []
        sz = m.size
        center = (sz[0]/2, sz[1]/2)
        for x in range(sz[0]):
            for y in range(sz[1]):
                if m.getpixel((x,y)) != (255,255,255):
                    d = math.sqrt((x-center[0])**2 + (y-center[1])**2)
                    dfc.append(d)
        dfc.sort()
        for i in ([5*x for x in range(10,21)]):
            dlen = len(dfc)
            num = dfc.count(i)
            fitnesshere = num - (dlen - num)
            fits.append(fitnesshere)
        
        fitness = max(fits)
        
        return fitness
    
    def is_neg(self):
        return True