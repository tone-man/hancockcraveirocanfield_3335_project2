import ViewController as vc
import GeneticImages
import FitnessFunctions as ff
import PIL

f = ff.CircleFitnessFunction()
g = GeneticImages.GeneticImages(f, 8)

p = g.getPopulation()

p[0].show()