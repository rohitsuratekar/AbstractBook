import os

from Functions import *
from OutputFormats import *

folder_list = ["Abstracts/", "AbstractsSpeakers/"]
file_names = ["all_abstracts.tex", "all_speakers.tex"]

for file_index in range(len(folder_list)):

    currentFolder = folder_list[file_index]
    save_file_name = file_names[file_index]
    all_abstracts = []
    for filename in os.listdir(currentFolder):
        currentFile = "%s%s" % (currentFolder, filename)
        with open(currentFile, 'r', errors="ignore") as myFile:
            # Get all elements separated by "{"
            # First should be title, Last should be Abstract and Rest all will be authors
            data = myFile.read().replace('\n', '').replace("}", "")
            # Get all the elements with non empty characters (or more than 3 character long)
            elements = list(filter(lambda k: len(k) > 3, data.split("{")))
            author_list = []
            for i in range(1, len(elements) - 1):
                currentAuthor = elements[i].replace("]", "").split("[")
                name = format_string(currentAuthor[0].strip().replace(",", ""))
                institute = format_string(currentAuthor[1].strip())
                is_presenting = "*" in name
                # Remove asterisk from author name
                name = name.replace("*", "")
                author_list.append(Author(name, institute, is_presenting))

            # Create abstract object
            all_abstracts.append(Abstract(format_string(elements[0]), author_list, format_string(elements[-1])))

    with open(save_file_name, 'w') as f:
        for a in all_abstracts:
            print(get_output_format(a), file=f)
            # print(r"\\\\", file=f)
