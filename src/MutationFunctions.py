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
                        
class DuplicateMutator(Mutator):
    
    def __init__(self, r, _range):
        super().__init__(r)
        self.shift_range = _range
    
    def mutate(self, m: Image) -> None:
        #Duplicates pixels in random spots
        for x in range(m.size[0]):
            for y in range(m.size[1]):
                
                pix = m.getpixel(xy=(x,y))
                x_off = random.randint(-self.shift_range, self.shift_range)
                y_off = random.randint(-self.shift_range, self.shift_range)
                
                if x + x_off < 0 or x + x_off >= m.size[0]:
                    x_off = -x_off
                if y + y_off < 0 or y + y_off >= m.size[1]:
                    y_off = -y_off
        
                m.putpixel(xy=(x + x_off, y + y_off), value=pix)

    def getRange(self):
        return self.shift_range
    
    def setRange(self, _range):
        self.shift_range = _range
