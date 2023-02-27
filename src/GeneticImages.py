from FitnessFunctionInterface import FitnessFunctionInterface
from PIL import Image
import random

class GeneticImages:
    '''
    This class uses Genetic Algorithms to generate a population of images
    that will evolve to a given fitness function.
    '''

    def __init__(self, f: FitnessFunctionInterface, p: int):
        self.population = [] #List of dictionaries
        self.fitness = [] #parrallel array of fitness values
        self.pop_size = p
        self.mix_number = 2
        self.mutation_rate = 0.01
        self.evolution_step = 0
        self.fitness_func = f.calcFitness
        self.IMAGE_SIZE = 200

        for i in range(self.pop_size):
            m = Image.new(mode="RGB", size= (self.IMAGE_SIZE, self.IMAGE_SIZE ), color= (255 , 255, 255))

            for x in range(200):
                for y in range(200):
                    m.putpixel(xy = (x,y), value = self.__rand_pix())
            
            self.population.append(m)

    def get_population(self):
        return self.population

    def get_fittest(self):
        return self.population[len(self.population) - 1]

    def get_step(self):
        return self.evolutionStep
    
    def step(self):
        self.__step()
    
    #def setPopulationSize(self):
        #pass

    #def setFitnessFunction(self):
        #pass

    def __calc_fittness(self, m: Image) -> float:
        return self.fitness_func(m)
    
    def __calc_weights(self) -> list:
        
        weights = []
        sum_f = 0
        cur_f = 0
        
        for f in range(self.pop_size):
            sum_f += self.fitness[f]

        for f in range(self.pop_size):
            weights.append(cur_f/sum_f)

        return weights
            
    def __select_parents(self, w) -> list:
        prob_t = [] #Construct a probability list
        sum_p = 0 #summation of all previous probabilities

        for val in w:
            sum_p += val
            prob_t.append(sum_p)
        
        parents = []
        for p in range(self.mix_number):
            r = random.random()

            for i in range(len(prob_t) - 1):
                if r >= prob_t[i] and r < prob_t[i + 1]:
                    parents.append(self.population[i])
        
        return parents

    def __cross_members(self, p: list):
        
        w = self.IMAGE_SIZE / self.mix_number
        
        left = 0
        upper = 0
        right = w
        lower = self.IMAGE_SIZE
        composite = Image.new("RGB", (self.IMAGE_SIZE, self.IMAGE_SIZE), "white")

        for i in range(self.mix_number):
            crop = p[i].crop((left, upper, right, lower)) 
            composite.paste(crop, (left, upper, right, lower))
            right += w
            

    def __mutate(self, c: Image):
        
        for i in range(10):
            x = random.randint(0, 200)
            y = random.randint(0, 200)
        
            c.putpixel(xy=(x,y), value = self.__rand_pix())

    def __step(self):
        population2 = [] #new array to hold offspring 

        for m in self.population: #calculate fitness for members
            fitness.append(self.__calc_fittness(m))

        weights = self.__calc_weights()

        for m in self.population:
            parents = self.__select_parents(weights)
            c = self.__cross_members(parents)
            self.__mutate(c)

            population2.append(c)

        self.population = population2    
        self.evolutionStep += 1


    def __rand_pix(self):
        return (random.randint(0,255) , random.randint(0,255), random.randint(0,255) )
