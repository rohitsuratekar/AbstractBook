import os

from GeneralModels import Abstract, Author, format_string
from OutputModel import get_output_format

folderNames = ["Abstracts/", "AbstractsSpeakers/"]
saveFileNames = ["all_abstracts.tex", "all_speakers.tex"]


for nameIndex in range(len(folderNames)):

    abstractFolder = folderNames[nameIndex]

    AllAbstracts = []

    for filename in os.listdir(abstractFolder):
        currentFile = "%s%s" % (abstractFolder, filename)
        # Encoding-Decoding did not worked , hence just ignore :P I tried :D
        with open(currentFile, 'r', errors="ignore") as myFile:
            data = myFile.read().replace('\n', '').replace("}", "")
            # Get all elements with greater than size 3, this is to remove all hidden characters in text file
            objects = list(filter(lambda k: len(k) > 3, data.split("{")))
            # File should at least contains title and abstract
            title = format_string(objects[0])
            abstractText = format_string(objects[len(objects) - 1])
            authorList = []
            if len(objects) > 2:  # If at least 1 author is given
                for i in objects[1:len(objects) - 1]:
                    authObject = list(filter(None, i.replace("]", "").split("[")))  # Get all non empty objects
                    if len(authObject) > 1:  # If author affiliation is given
                        # If more than one affiliation
                        all_institutes = []
                        if len(authObject) > 2:
                            for institute in authObject[1:]:
                                all_institutes.append(institute.strip().replace("&", "\&"))
                        else:
                            all_institutes.append(authObject[1].strip().replace("&", "\&"))
                        authorList.append(Author(authObject[0].strip(), all_institutes))
                    else:  # If author affiliation is not given
                        authorList.append(Author(authObject[0].strip(), ["Not Available"]))
            else:  # If no author is given
                authorList.append(Author("Unknown", ["Not Available"]))

            AllAbstracts.append(Abstract(title, authorList, abstractText))

    with open(saveFileNames[nameIndex], 'w') as f:
        for a in AllAbstracts:
            print(get_output_format(a), file=f)
            print(r"\\\\", file=f)
