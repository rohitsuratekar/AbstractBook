import os
from GeneralModels import Abstract, Author

abstractFolder = "Abstracts/"

AllAbstracts = []

for filename in os.listdir(abstractFolder):
    currentFile = "%s%s" % (abstractFolder, filename)
    with open(currentFile, 'r') as myFile:
        data = myFile.read().replace('\n', '').replace("}", "")
        objects = list(filter(None, data.split("{")))  # Get all non empty objects
        # File should at least contains title and abstract
        title = objects[0]
        abstractText = objects[len(objects) - 1]
        authorList = []
        if len(objects) > 2:  # If at least 1 author is given
            for i in objects[1:len(objects) - 1]:
                authObject = list(filter(None, i.replace("]", "").split("[")))  # Get all non empty objects
                if len(authObject) > 1:  # If author affiliation is given
                    authorList.append(Author(authObject[0].strip(), authObject[1].strip()))
                else:  # If author affiliation is not given
                    authorList.append(Author(authObject[0].strip(), "Not Available"))
        else:  # If no author is given
            authorList.append(Author("Unknown", "Not Available"))

        AllAbstracts.append(Abstract(title, authorList, abstractText))

print(AllAbstracts)
