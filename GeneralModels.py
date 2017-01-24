class Author:
    """Author name and its affiliation"""
    name = "Author Name"
    affiliation = ["Unknown"]
    is_presenting_author = False
    email = "unknown"

    def __init__(self, name=None, affiliation=None, presenting=None, email=None):
        self.name = name
        self.affiliation = affiliation
        self.is_presenting_author = presenting or False
        self.email = email or "unknown"


class Abstract:
    """docstring for Abstract"""
    authors = []
    title = "Abstract Title"
    abstract = "Abstract Text not available"
    from_single_institute = True
    has_references = False
    references = []
    unique_institutes = []

    def __init__(self, title=None, author_list=None, abstract=None):
        self.title = title
        self.authors = list(author_list)
        self.abstract = abstract
        self.references = []
        # Check if all authors are from same university
        unique_institutes_dic = {}
        for a in author_list:
            unique_institutes_dic[a.affiliation] = a.affiliation

        self.from_single_institute = len(unique_institutes_dic) == 1

        # Get list of unique universities
        self.unique_institutes = sorted([v for k, v in unique_institutes_dic.items()])

        # Check for references (if any)
        if "#" in abstract:
            self.has_references = True
            all_ref = abstract.split("#")
            self.abstract = all_ref[0]
            for ref in range(1, len(all_ref)):
                self.references.append(all_ref[ref].strip())
