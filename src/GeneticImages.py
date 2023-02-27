from FitnessFunctionInterface import FitnessFunctionInterface
from PIL import Image
import random

class GeneticImages:
    '''
    This class uses Genetic Algorithms to generate a population of images
    that will evolve to a given fitness function.
    '''

    def __init__(self, f: FitnessFunctionInterface, p: int):
        self.population = [None] * p #List of dictionaries
        self.fitness = [None] * p #parrallel array of fitness values
        self.pop_size = p
        self.mix_number = 2
        self.mutation_rate = 0.01
        self.evolution_step = 0
        self.fitness_func = f
        self.IMAGE_SIZE = 200
        
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
    
    #def setPopulationSize(self):
        #pass

    #def setFitnessFunction(self):
        #pass

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
        
        return composite
            

    def __mutate(self, c: Image):
        
        for i in range(10):
            x = random.randint(0, 199)
            y = random.randint(0, 199)
        
            c.putpixel(xy=(x,y), value = (255, 255, 255))

    def __step(self):
        population2 = [] #new array to hold offspring 

        #calculate fitness for members
        for m in range(self.pop_size):
            self.fitness[m] = (self.__calc_fittness(self.population[m]))

        #check fitness is valid for weighting
        if(self.fitness_func.is_neg()):
            self.__fix_fittness()
        print("Fitness :", self.fitness)
        
        #weight fitness for roulette selection
        weights = self.__calc_weights()
        print("Weights :", weights)
        
        #check to see if elitism is enabled
        if self.elitism_enabled:
            sort_fit = sorted(self.fitness)
            
            for x in range(self.pop_size - 1 , (self.pop_size - 1) - self.elite_count, -1):
                #Get Fitness value
                f_val = sort_fit[x]
                #Find value in the fitness array, this isnt perfect and needs work
                print(f_val, self.fitness.index(f_val))
                population2.append(self.population[self.fitness.index(f_val)])
            
        while len(population2) < self.pop_size:
            parents = self.__select_parents(weights)
            c = self.__cross_members(parents)
            self.__mutate(c)

            population2.append(c)

        self.population = population2    
        self.evolution_step += 1


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
