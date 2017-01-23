class Author:
    """Author name and its affiliation"""
    name = "Author Name"
    affiliation = ["Unknown"]
    presenting_author = False

    def __init__(self, name=None, affiliation=None, presenting=False):
        self.name = name
        self.affiliation = list(affiliation)
        self.presenting_author = presenting


class Abstract:
    """docstring for Abstract"""
    authors = []
    title = "Abstract Title"
    abstract = "Abstract Text not available"

    def __init__(self, title=None, author_list=None, abstract=None):
        self.title = title
        self.authors = list(author_list)
        self.abstract = abstract


def format_string(string):
    return string.replace("&", "\&").replace("%", "\%").replace("<", r"\textless ").replace(">", r"\textgreater ")
