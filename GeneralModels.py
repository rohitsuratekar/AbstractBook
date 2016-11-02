class Author:
    """Author name and its affiliation"""
    name = "Author Name"
    affiliation = "Unknown"

    def __init__(self, name=None, affiliation=None):
        self.name = name
        self.affiliation = affiliation


class Abstract:
    """docstring for Abstract"""
    authors = []
    title = "Abstract Title"
    abstract = "Abstract Text not available"

    def __init__(self, title=None, authorList=None, abstract=None):
        self.title = title
        self.authors = list(authorList)
        self.abstract = abstract
