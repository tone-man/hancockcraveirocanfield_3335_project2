import View as v
import GeneticImages
import FitnessFunctions as ff
import MutationFunctions as mut
import PIL

#Decide a fitness function to use
f = ff.CircleFitnessFunction()

#Select mutator methods
m = []

m.append(mut.SwapMutator(0.01))
m.append(mut.NearSwapMutator(0.01, 2))
#Create a geneticImage object
g = GeneticImages.GeneticImages(f, m, 8)

#Use GUI to work with it
v.initGUI(g)