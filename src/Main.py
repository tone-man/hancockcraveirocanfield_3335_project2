import View as v
import GeneticImages
import FitnessFunctions as ff
import MutationFunctions as mut
import PIL

f = ff.CircleFitnessFunction()

m = []
m.append(mut.FlipMutator(0.1))
m.append(mut.DuplicateMutator(0.1, 5))

g = GeneticImages.GeneticImages(f, m, 8)

v.initGUI(g)