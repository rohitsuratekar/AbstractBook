import os
from GeneralModels import Abstract, Author
from OutputModel import get_output_format

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
                    # If more than one affiliation
                    all_institutes = []
                    if len(authObject) > 2:
                        for institute in authObject[1:]:
                            all_institutes.append(institute.strip())
                    else:
                        all_institutes.append(authObject[1].strip())
                    authorList.append(Author(authObject[0].strip(), all_institutes))
                else:  # If author affiliation is not given
                    authorList.append(Author(authObject[0].strip(), ["Not Available"]))
        else:  # If no author is given
            authorList.append(Author("Unknown", ["Not Available"]))

        AllAbstracts.append(Abstract(title, authorList, abstractText))

with open("all_abstracts.tex", 'w') as f:
    for a in AllAbstracts:
        print(get_output_format(a), file=f)
        print(r"\\\\", file=f)
