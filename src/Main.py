import ViewController as vc
import GeneticImages
import FitnessFunctions as ff
import PIL

f = ff.CircleFitnessFunction()
g = GeneticImages.GeneticImages(f, 8)

p = g.get_population()
g.step(1000)
p = g.get_population()
p[0].show()