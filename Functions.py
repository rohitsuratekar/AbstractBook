import re


# Taken from http://stackoverflow.com/questions/41820839/convert-quotation-marks-to-latex-format-with-python
def texify_single_quote(in_string):
    # If there is a match, go through them and make sure
    # the captured group is not empty (i.e. the  '' for LaTeX double quotes)
    for match in re.finditer(r"'(.*?)'", in_string):
        if match.group(1).strip() != '':
            return re.sub(r"'(.*?)'", r"`\1'", in_string)
        else:
            # potentially a LaTeX end double-quote, ignore it!
            return in_string

    # if there is no match at all, return the string
    return in_string


def texify_double_quote(in_string):
    return re.sub(r'"(.*?)"', r"``\1''", in_string)


def format_string(string):
    string = string.replace("&", "\&").replace("%", "\%").replace("<", r"\textless ").replace(">", r"\textgreater ")
    string = texify_double_quote(string)
    string = texify_single_quote(string)
    return string
