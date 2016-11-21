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
se : \section{}
ts : \textsuperscript{}

To use new line after text use "n" at the end
To use new lines before text use "n" at the start
Use indent ("in") at the start of line

"""

title_attributes = ["se"]
author_attributes = []
affiliation_attributes = ["sc", "i"]
abstract_attribute = ["in"]


def get_output_format(abstract):
    """Outputs string in latex format
    :param abstract: Abstract class from GeneralModel.py
    """
    author_list = []
    institute_name_list = []
    for author in abstract.authors:
        current_author_insti = []
        for institute in author.affiliation:
            if institute not in institute_name_list:
                institute_name_list.append(institute.strip())
                current_author_insti.append(institute_name_list.index(institute.strip()))
            else:
                current_author_insti.append(institute_name_list.index(institute.strip()))

        author_list.append(AuthorNames(author.name, current_author_insti))

    author_string = ""
    # +1 is added to start numbering from 1
    for auth in author_list[:-1]:
        author_insti_list = ""
        for s in auth.indexes[:-1]:
            author_insti_list = author_insti_list + str(s + 1) + ","

        author_insti_list += str(auth.indexes[-1] + 1)
        author_string = author_string + auth.name + get["ts"](author_insti_list) + ", "

    # For last author
    author_insti_list = ""
    for s in author_list[-1].indexes[:-1]:
        author_insti_list = author_insti_list + str(s + 1) + ","

    author_insti_list += str(author_list[-1].indexes[-1] + 1)
    author_string = author_string + author_list[-1].name + get["ts"](author_insti_list)

    institute_string = ""
    for i in range(len(institute_name_list) - 1):
        institute_string = institute_string + get["ts"](str(i + 1)) + institute_name_list[i] + r"\linebreak"

    institute_string = institute_string + get["ts"](str(len(institute_name_list))) + \
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

    return r"%s \begin{center} %s \par %s \end{center} \sloppy %s" % (
        title_string, author_string, institute_string, abstract_string)


class AuthorNames:
    """ Simple object to represent author and its superscript
    """
    name = "Author Name"
    indexes = [0]

    def __init__(self, name=None, indexes=None):
        self.name = name
        self.indexes = list(indexes)


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


def section(text):
    return r"\section{%s}" % text


def superscript(text):
    return r"\textsuperscript{%s}" % text


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
    "in": indent,
    "se": section,
    "ts": superscript
}
