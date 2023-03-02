from FunctionInterfaces import FitnessFunctionInterface, MutationFunctionInterface
from MutationFunctions import Mutator
from PIL import Image
import random

class GeneticImages:
    '''
    This class uses Genetic Algorithms to generate a population of images
    that will evolve to a given fitness function.
    '''

    def __init__(self, f: FitnessFunctionInterface, m: [MutationFunctionInterface], p: int):
        
        #Basic Variables
        self.IMAGE_SIZE = 200
        self.population = [None] * p #List of Images
        self.pop_size = p
        self.evolution_step = 0
                
        #Cross Breeding Variables
        self.mix_number = 2
        
        #Mutation Stuff
        self.mutators = m #array of mutators to be selected at random     
        self.mutation_rate = 0.5 #Odds of a child being born with mutation
        
        #Fitness Stuff
        self.fitness = [None] * p #parrallel array of fitness values
        self.fitness_func = f
        
        #Elitism Stuff
        self.elitism_enabled = True
        self.elite_count = int(p / 2) # defaults to half

        for i in range(self.pop_size):
            m = Image.new(mode="RGB", size= (self.IMAGE_SIZE, self.IMAGE_SIZE ), color= (255 , 255, 255))

            for x in range(200):
                for y in range(200):
                    m.putpixel(xy = (x,y), value = self.__rand_pix())
            
            self.population[i] = m

    def get_population(self):
        return self.population

    def get_fittest(self):
        return self.population[len(self.population) - 1]

    def get_step(self):
        return self.evolutionStep
    
    def step(self, n: int = 1):
        for x in range(n):
            self.__step()
            
    def is_started(self):
        if(self.evolution_step > 0):
            return True
        return False
    
    def add_mutator(self, m: Mutator):
        self.mutators.append(m)

    def __calc_fittness(self, m: Image) -> float:
        return self.fitness_func.calc_fitness(m)
    
    def __calc_weights(self) -> list:
        
        weights = []
        sum_f = 0
        
        #Summation of all fitness
        for f in range(self.pop_size):
            sum_f += self.fitness[f]
            
        #Divide fitness of individual by total fitness to get roullette selection
        for f in range(self.pop_size):
            weights.append(self.fitness[f]/sum_f)

        return weights
            
    def __select_parents(self, w) -> list:
        prob_t = [] #Construct a probability list
        sum_p = 0 #summation of all previous probabilities

        for val in w:
            sum_p += val
            prob_t.append(sum_p)
        
        parents = []
        for p in range(self.mix_number):
            parent = None
            r = random.random()

            for i in range(len(prob_t) - 1):
                if r >= prob_t[i] and r < prob_t[i + 1]:
                    parent = self.population[i]
            
            if parent == None:
                parent = self.population[len(prob_t) - 1]

            parents.append(parent)
            
        return parents

    def __cross_members(self, p: list):
        
        w = int(self.IMAGE_SIZE / self.mix_number)
        
        left = 0
        upper = 0
        right = w
        lower = self.IMAGE_SIZE
        composite = Image.new("RGB", (self.IMAGE_SIZE, self.IMAGE_SIZE), "white")

        for i in range(self.mix_number):
            crop = p[i].crop((left, upper, right, lower)) 
            composite.paste(crop, (left, upper, right, lower))
            right += w
            left += w
        
        return composite
            

    def __mutate(self, c: Image):
        
        mode = random.randint(0, len(self.mutators) - 1)
        self.mutators[mode].mutate(c)
               
    def __step(self):
        population2 = [] #new array to hold offspring 

        #calculate fitness for members
        for m in range(self.pop_size):
            self.fitness[m] = (self.__calc_fittness(self.population[m]))

        #check fitness is valid for weighting
        print("Fittness :", self.fitness)
        
        if(self.fitness_func.is_neg()):
            self.__fix_fittness()
            print("Adjusted Fittness :", self.fitness)
        
        
        #weight fitness for roulette selection
        weights = self.__calc_weights()
        
        #check to see if elitism is enabled
        if self.elitism_enabled:
            sort_fit = sorted(self.fitness)
            selected = []
            
            for x in range(self.pop_size - 1 , (self.pop_size - 1) - self.elite_count, -1):
                #Get Fitness value and find pos in normal fitness array
                f_val = sort_fit[x]
                pos = self.fitness.index(f_val)
                
                #Ensure pos has not already been added
                while selected.count(pos) > 0:
                    pos = self.fitness.index(value)
                    
                population2.append(self.population[pos])
                
        while len(population2) < self.pop_size:
            parents = self.__select_parents(weights)
            c = self.__cross_members(parents)
            
            if random.random() < self.mutation_rate:
                self.__mutate(c)

            population2.append(c)

        self.population = population2    
        self.evolution_step += 1
        
        print("Step", self.evolution_step, " Complete!")


    def __fix_fittness(self):
        low = self.fitness[0]
        
        #Find lowest fitness
        for f in self.fitness:
            low = min(f, low)
        #Flip min fitness if negative
        if low < 0:
            low *= -1
        
        #Add lowest fitness to all values
        for i in range(len(self.fitness)):
            self.fitness[i] += low
            
            #if 0 increment by negligble amount
            if self.fitness[i] == 0:
                self.fitness[i] += 0.00001
            
    def __rand_pix(self):
        return (random.randint(0,255) , random.randint(0,255), random.randint(0,255) )
    
    def __calc_dist(self, src, target):
        return math.sqrt((src[0]-target[0])**2 + (src[1]-target[1])**2)
    
    def __calc_slope(self, src, target):
        return (src[0] - target[0], src[1] - target[1])
