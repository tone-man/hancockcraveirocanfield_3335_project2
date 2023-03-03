from FunctionInterfaces import MutationFunctionInterface
from PIL import Image
import random

class Mutator(MutationFunctionInterface):
    
    def __init__(self, r):
        '''
        Creates an abstract mutator
        '''
        self.rate = r
    
    def mutate(self, m):
        raise NotImplementedError()
    
    def get_rate(self):
        return self.rate
    
    def set_rate(self, r):
        self.rate = r
        
    
class FlipMutator(Mutator):
    '''
    Flips pixels randomly
    '''
    def __init__(self, r: float):
        super().__init__(r)
        
    def mutate(self, m: Image) -> None:
          
        for x in range(m.size[0]):
            for y in range(m.size[1]):
                r = random.random()
                
                #if pix gets lucky
                if r < self.rate:
                    pix = m.getpixel(xy=(x, y))

                    #Non white pixels -> white
                    if pix[0] != 255 or pix[1] != 255 or pix[2] != 255:
                        m.putpixel(xy=(x, y), value=(255,255,255))
                    else:
                        m.putpixel(xy=(x, y), value=(random.randint(0,255) , random.randint(0,255), random.randint(0,255) ))
                        
class RangeSwapMutator(Mutator):
    '''
    Swaps two arbitrary pixels within r
    '''
    def __init__(self, r, _range):
        super().__init__(r)
        self._range = _range
    
    def mutate(self, m: Image) -> None:
        #Shifts pixels in random spots
        
        for x in range(m.size[0]):
            for y in range(m.size[1]):
            
                r = random.random()
                if(r < self.rate):
                    
                    pix = m.getpixel(xy=(x,y))
                    x2 = random.randint(-self._range, self._range) + x
                    y2 = random.randint(-self._range, self._range) + y
                    
                    xy2 = self.__wrap((x2, y2), m.size)
        
                    tmp = m.getpixel(xy=xy2)
                    m.putpixel(xy=xy2, value=pix)
                    m.putpixel(xy=(x, y), value=tmp)

    def get_range(self):
        return self.shift_range
    
    def set_range(self, _range):
        self.shift_range = _range
        
    def wrap(self, xy, wh):
        '''
        Wraps values around image, so -1 -> im.size() - 2 
        '''
        x = xy[0]
        y = xy[1]
        
        if(xy[0] < 0 or xy[0] >= wh[0]):
            x = xy[0] % wh[0]
        if(xy[1] < 0 or xy[1] >= wh[1]):
            y = xy[1] % wh[1]
        return (x, y)
        
        
class SwapMutator(Mutator):
    ''' 
    Swaps a white pixel with a colored pixel
    
    WARNING: USE THIS IF YOU KNOW WHITE PIXELS EXIST, OTHERWISE NEVER HALTS
    '''
    def __init__(self, r):
        super().__init__(r)
    
    def mutate(self, m: Image):
        
        for x in range(m.size[0]):
            for y in range(m.size[1]):
                
                r = random.random()
                if(r < self.rate):
                    
                    xy1 = (x , y)
                    xy2 = None
                    pix = m.getpixel(xy=xy1)
                    pix2 = None
                    
                    #If pix is not white
                    if pix[0] != 255 or pix[1] != 255 or pix[2] != 255: 
                              
                        xy2 = ( random.randint(0, m.size[0] - 1) , random.randint(0, m.size[1] - 1) )
                        pix2 = m.getpixel(xy=xy2)
                        
                        while(pix2[0] != 255 and pix2[1] != 255 and pix2[2] != 255):
                            xy2 = ( random.randint(0, m.size[0] - 1) , random.randint(0, m.size[1] - 1) )
                            pix2 = m.getpixel(xy=xy2)
                            
                    #If pix is white
                    else:
                        xy2 = ( random.randint(0, m.size[0] - 1) , random.randint(0, m.size[1] - 1) )
                        pix2 = m.getpixel(xy=xy2)
                        
                        while(pix2[0] == 255 and pix2[1] == 255 and pix2[2] == 255):
                            xy2 = ( random.randint(0, m.size[0] - 1) , random.randint(0, m.size[1] - 1) )
                            pix2 = m.getpixel(xy=xy2)
                    
                    m.putpixel(xy=xy2, value=pix)
                    m.putpixel(xy=xy1, value=pix2)

class NearSwapMutator(RangeSwapMutator):
    '''
    Like Swap Mutator, but takes additional Radius r. Swaps a white pixel with a non-white pixel

    '''
    def __init__(self, r, range):
        super().__init__(r, range)
        
    def mutate(self, m: Image):
        
        for x in range(m.size[0]):
            for y in range(m.size[1]):
                r = random.random()
                
                #if pix gets lucky
                if r < self.rate:
                    
                    xy1 = (x, y)
                    xy2 = None
                    pix = m.getpixel(xy=xy1)
                    pix2 = None
                    attempts = 0 #counter to break from while loop
                    max_attempts = pow(self._range, 2)
                    
                    #If pix is not white
                    if (pix[0] != 255 or pix[1] != 255 or pix[2] != 255):       
                        
                        x2 = random.randint(-self._range, self._range) + x
                        y2 = random.randint(-self._range, self._range) + y
                        xy2 = super().wrap((x2, y2), m.size)
                        pix2 = m.getpixel(xy=xy2)
                        
                        while(attempts < max_attempts and pix2[0] != 255 and pix2[1] != 255 and pix2[2] != 255):
                            x2 = random.randint(-self._range, self._range) + x
                            y2 = random.randint(-self._range, self._range) + y
                            xy2 = super().wrap((x2, y2), m.size)
                            pix2 = m.getpixel(xy=xy2)
                            attempts += 1
                            
                    #If pix is white
                    else:
                        x2 = random.randint(-self._range, self._range) + x
                        y2 = random.randint(-self._range, self._range) + y
                        xy2 = super().wrap((x2, y2), m.size)
                        pix2 = m.getpixel(xy=xy2)
                        
                        while(attempts < max_attempts and pix2[0] == 255 and pix2[1] == 255 and pix2[2] == 255):
                            x2 = random.randint(-self._range, self._range) + x
                            y2 = random.randint(-self._range, self._range) + y
                            xy2 = super().wrap((x2, y2), m.size)
                            pix2 = m.getpixel(xy=xy2)
                            attempts += 1
                    
                    m.putpixel(xy=xy2, value=pix)
                    m.putpixel(xy=xy1, value=pix2)
