class FitnessFunctionInterface:



    def calc_fitness(self, m) -> float:
        '''
        Calculates a fitness value for a given member of a population.
        
        Arguments:
        m -> Image : Member of a the image population
        '''

    
    def is_neg(self) -> bool:
        '''
        Flag to inform GeneticImages if the given fitness function return negative values
        '''