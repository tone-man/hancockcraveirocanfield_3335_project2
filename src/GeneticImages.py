from FitnessFunctionInterface import FitnessFunctionInterface
from PIL import Image

class GeneticImages:
    '''
    This class uses Genetic Algorithms to generate a population of images
    that will evolve to a given fitness function.
    '''
    self.population
    self.mixNumber
    self.mutationRate
    # self.combinationMode for later
    self.evolutionStep
    self.fitnessFunction

    def __init__(f: FitnessFunctionInterface, p: int):
        self.population = []
        self.mixNumber = 2
        self.mutationRate = 0.01
        self.evolutionStep = 0
        self.fitnessFunction = f.calcFittness

        for i in range(p):
            m = Image.new(mode="RGB", size= ( 200, 200 ), color= (255 , 255, 255))

            for x in range(200):
                for y in range(200):
                    m.putpixel(xy = (x,y), value = __randPix())
            
            self.population.append(m)


    def getPopulation():
        return self.population

    def getFittest():
        return self.population[len(self.population) - 1]

    def getStep():
        return self.evolutionStep
    
    def setPopulationSize():
        pass

    def setFitnessFunction():
        pass

    def __calcFittness(m: Image) -> float:
        return self.fitnessFunction(m)
    
    def __selectParent():
        pass

    def __crossMembers():
        pass

    def __mutate():
        pass

    def __step():
        pass

    def __randPix(p: int):
        return (random.randint(0,255) , random.randint(0,255), random.randint(0,255) )


