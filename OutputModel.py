"""
Available Output arguments
b : \textbf{}
i : \textit{}
s : {\small }
f : {\footnotesize }
sc: {\scriptsize }
t : {\tiny }
l :{\large }
xl: {\Large }
h :{\huge }
xh : {\Huge }
q: \quad (after string)
qq: \qquad (after string)
bq : \quad (before string)
bqq: \qquad (before string)
in : \indent

To use new line after text use "n" at the end
To use new lines before text use "n" at the start
Use indent ("in") at the start of line

"""

title_attributes = ["b", "n"]
author_attributes = ["s", "n"]
affiliation_attributes = ["sc", "i", "n", "n"]
abstract_attribute = ["in", "n"]


def get_output_format(abstract):
    """Outputs string in latex format
    :param abstract: Abstract class from GeneralModel.py
    """
    author_list = []
    institute_name_list = []
    for author in abstract.authors:
        if author.affiliation.strip() not in institute_name_list:
            institute_name_list.append(author.affiliation.strip())

        author_list.append(AuthorNames(author.name, institute_name_list.index(author.affiliation.strip())))

    author_string = ""
    for auth in author_list[:-1]:
        author_string = author_string + auth.name + r"\textsuperscript{" + str(auth.index) + "}, "
    author_string = author_string + author_list[-1].name + r"\textsuperscript{" + str(author_list[-1].index) + "}"

    institute_string = ""
    for i in range(len(institute_name_list) - 1):
        institute_string = institute_string + r"\textsuperscript{" + str(i) + "} " + institute_name_list[i] + r"\\"

    institute_string = institute_string + r"\textsuperscript{" + str(len(institute_name_list) - 1) + "} " + \
                       institute_name_list[-1]

    title_string = abstract.title
    abstract_string = abstract.abstract
    for t in title_attributes:
        title_string = get[t](title_string)
    for a in author_attributes:
        author_string = get[a](author_string)
    for ins in affiliation_attributes:
        institute_string = get[ins](institute_string)
    for ab in abstract_attribute:
        abstract_string = get[ab](abstract_string)

    return r"%s%s%s%s" % (title_string, author_string, institute_string, abstract_string)


class AuthorNames:
    """ Simple object to represent author and its superscript
    """
    name = "Author Name"
    index = 0

    def __init__(self, name=None, index=None):
        self.name = name
        self.index = index


def bold(text):
    return r"\textbf{%s}" % text


def italics(text):
    return r"\textit{%s}" % text


def small(text):
    return r"{\small %s}" % text


def footnotesize(text):
    return r"{\footnotesize %s}" % text


def scriptsize(text):
    return r"{\scriptsize %s}" % text


def tiny(text):
    return r"{\tiny %s}" % text


def large(text):
    return r"{\large %s}" % text


def extra_large(text):
    return r"la: {\Large %s}" % text


def huge(text):
    return r"{\huge %s}" % text


def extra_huge(text):
    return r"{\Huge %s}" % text


def new_line(text):
    return r"%s \\ " % text


def tab_after(text):
    return r"%s \quad " % text


def tab_before(text):
    return r"\quad %s " % text


def extra_tab_after(text):
    return r"%s \qquad " % text


def extra_tab_before(text):
    return r"\qquad %s " % text


def indent(text):
    return r"\indent %s " % text


get = {
    "b": bold,
    "i": italics,
    "s": small,
    "f": footnotesize,
    "sc": scriptsize,
    "t": tiny,
    "l": large,
    "xl": extra_large,
    "h": huge,
    "xh": extra_huge,
    "n": new_line,
    "q": tab_after,
    "bq": tab_before,
    "qq": extra_tab_after,
    "bqq": extra_tab_before,
    "in": indent
}
