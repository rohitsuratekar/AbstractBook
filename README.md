# AbstractBook
This is simple script created to make Abstract Book of any conference/meeting/report in unified Latex format. Only think you have to do it to save abstract in single text file in given format. This script can be extrapolated to any other template based text mining. 

## Features
(1) Applies unified format for all abstracts <br>
(2) Common built in customizations <br>
(3) DYI properties (if needed) <br>
(4) Can be extrapolated to any other text format

## Text file format
Use single text file for single abstract. Use following format
e.g. abstract1.txt

    {title}
    {Author Name [Affiliation]}
    {Author2 Name [Affiliation1] [Affiliation2]}
    {Abstract Text}
    
DO NOT curly brackets { } anywhere in your text. Replace them with something else if needed.

## Steps
(1) Save all the abstracts in the folder "Abstracts" with above format <br>
(2) Use default format or change output format from " OutputModel.py " <br>
(2) Run the " ConvertAbstracts.py " with Python 3+ <br>
(3) It will produce Latex file "all_abstracts.tex" with unified format

## Built in latex commands
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
