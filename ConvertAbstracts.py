import os
import GeneralModels as g

abstractFolder = "Abstracts/"
for filename in os.listdir(abstractFolder):
    currentFile = "%s%s" % (abstractFolder, filename)
    with open(currentFile, 'r') as myFile:
        data = myFile.read().replace('\n', '').replace("}", "")
        objects = data.split("{")
        title = objects[1]
        authors = objects[2]
        a1 = g.Author(objects[2], "SomeName")
        abstract1 = g.Abstract(title, [a1], objects[len(objects) - 1])
        print(abstract1.authors[0].name)
