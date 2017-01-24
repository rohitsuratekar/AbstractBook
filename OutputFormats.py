from GeneralModels import *

title_attributes = ["se"]
author_attributes = []
affiliation_attributes = ["sc", "i"]
abstract_attribute = ["in"]
presenting_author_attribute = "b"
reference_attribute = ["in"]


def format_author(author_string, is_presenting):
    """
    Formats single author
    :param author_string: Name
    :param is_presenting: is presenting author
    :return: formatted string
    """
    if is_presenting:
        return get[presenting_author_attribute](author_string)
    else:
        for a in author_attributes:
            author_string = get[a](author_string)
        return author_string


def format_superscript(number):
    """
    Formats superscript
    :param number: integer
    :return: formatted string
    """
    if len(str(number)) == 0:
        return ""
    else:
        return get['ts'](str(number))


def format_affiliation(uni_string):
    """
    Formats affiliations
    :param uni_string: University/Institute name
    :return: formatted string
    """
    for a in affiliation_attributes:
        uni_string = get[a](uni_string)
    return uni_string


def get_author_superscript(author: Author, abstract: Abstract):
    """
    Gets superscript for author (if needed)
    :param author: Author
    :param abstract: Complete Abstract class
    :return: formatted string
    """
    if abstract.from_single_institute:
        return ""
    else:
        return abstract.unique_institutes.index(author.affiliation) + 1  # +1 to start index from 1


def get_university_list(abstract: Abstract):
    """
    Gets string with all universities
    :param abstract: Abstract class
    :return: Formatted string
    """
    if abstract.from_single_institute:
        return format_affiliation(abstract.unique_institutes[0])
    else:
        all_uni = ""
        for i in range(len(abstract.unique_institutes)):
            all_uni = all_uni + format_superscript(i + 1) + format_affiliation(
                abstract.unique_institutes[i]) + ",\\\\"
        return all_uni.rstrip(',\\\\')


def get_author_string(abstract: Abstract):
    """
    Complete author list
    :param abstract: Abstract class
    :return: Author string
    """
    all_authors = ""
    for author in abstract.authors:
        all_authors = all_authors + format_author(author.name, author.is_presenting_author) + format_superscript(
            get_author_superscript(author, abstract)) + ", "
    return all_authors.rstrip(", ")


def get_output_format(abstract: Abstract):
    abstract_text = abstract.abstract
    abstract_title = abstract.title
    references = ""

    for a in title_attributes:
        abstract_title = get[a](abstract_title)
    for a in abstract_attribute:
        abstract_text = get[a](abstract_text)

    if abstract.has_references:
        for r in abstract.references:
            references += "\\item " + r
        references = "\\begin{enumerate}  \\itemsep0em \\small" + references + "\\end{enumerate}"

    for a in reference_attribute:
        references = get[a](references)

    return r"%s \begin{center} %s \par %s \end{center} \sloppy %s %s" % (
        abstract_title, get_author_string(abstract), get_university_list(abstract), abstract_text, references)


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
