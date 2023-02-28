from PIL import Image

class FitnessFunctionInterface:
    '''
    Interface to create custom Fitness Functions to use for GeneticImages.
    '''

    def calc_fitness(self, m) -> float:
        '''
        Calculates a fitness value for a given member of a population.
        
        Arguments:
        m -> Image : Member of the image population
        
        Returns  float: fitness value
        '''
        raise  NotImplementedError('')

    
    def is_neg(self) -> bool:
        '''
        Flag to inform GeneticImages if the given fitness function return negative values
        
        Returns boolean: true if fitness can be negative, false otherwise
        '''
        raise NotImplementedError('')

class MutationFunctionInterface:
    '''
    Inteface to create custom mutation functions to use for GeneticImages
    '''
    def mutate(self, m) -> Image:
        '''
        Manipulates the genetic code of an image.
        
        Arguments:
        m -> Image: Member of the image population
        
        Returns Image: altered image
        '''
        raise NotImplementedError()