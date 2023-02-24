from FitnessFunctionInterface import FitnessFunctionInterface
from PIL import Image
import random

class GeneticImages:
    '''
    This class uses Genetic Algorithms to generate a population of images
    that will evolve to a given fitness function.
    '''

    def __init__(self, f: FitnessFunctionInterface, p: int):
        self.population = []
        self.mixNumber = 2
        self.mutationRate = 0.01
        self.evolutionStep = 0
        self.fitnessFunction = f.calcFitness

        for i in range(p):
            m = Image.new(mode="RGB", size= ( 200, 200 ), color= (255 , 255, 255))

            for x in range(200):
                for y in range(200):
                    m.putpixel(xy = (x,y), value = self.__randPix())
            
            self.population.append(m)


    def getPopulation(self):
        return self.population

    def getFittest(self):
        return self.population[len(self.population) - 1]

    def getStep(self):
        return self.evolutionStep
    
    def setPopulationSize(self):
        pass

    def setFitnessFunction(self):
        pass

    def __calcFittness(self, m: Image) -> float:
        return self.fitnessFunction(m)
    
    def __selectParent(self):
        pass

    def __crossMembers(self):
        pass

    def __mutate(self):
        pass

    def __step(self):
        pass

    def __randPix(self):
        return (random.randint(0,255) , random.randint(0,255), random.randint(0,255) )


