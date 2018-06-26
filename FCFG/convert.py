from nltk import load_parser
import sys
def isVariable(i, fol):
    if fol[i - 1] == '(' and fol[i + 1] == ')':
        return True
    
    if fol[i - 1] == '(' and (fol[i + 1] == ',' or fol[i + 1] == '='):
        return True
    
    if (fol[i - 1] == ',' or fol[i - 1] == '=') and fol[i + 1] == ')':
        return True
    
    if fol[i - 1] == 'exists' or fol[i - 1] == 'all':
        return True
    
    return False

def replaceNum(i, fol):
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in fol[i]:
        if char in num:
            return fol[i].replace(char, '_' + char)
    return fol[i]


def outputHead():
	print("\\documentclass{article}")
	print("\\usepackage[utf8]{inputenc}")
	print("\\usepackage{listings}")
	print("\\usepackage{xcolor}")
	print("\\usepackage{graphicx, fancyhdr, amsmath, amssymb, amsthm, subfig}")
	print("\\usepackage{indentfirst}")
	print("\\usepackage{pdfpages}")
	print("\\usepackage{dirtree}")
	print("\\usepackage{lastpage, hyperref}")
	print("\\begin{document}")
	return

def outputEnd():
	print("\\end{document}")
	return


# parser = load_parser('./grammar.fcfg')

# sentences = [
#     'Alice is happy',
#     'Bob is in the kitchen',
#     'Charlie is in a garden',

#     'Every student at STU is smart',
#     'Some boys in the garden are sad',
#     'All girls are beautiful',
#     'No student is married',

#     'Alice is not happy',
#     'All persons are not sad',

#     'A dog barks',
#     'All dogs bark',
#     'The dog in the garden barks',

#     'Alice sees Bob',
#     'Alice does know Bob',
#     'Alice chases Bob in the garden',
#     'All persons in Shanghai know STU',

#     'Alice is in the garden with Bob'
# ]

def convert(sentence):
    #print(sentence)
    tokens = sentence.split()
    parser = load_parser('./grammar.fcfg')
    trees = parser.parse(tokens)
    for tree in trees:
        fol = (tree.label()['SEM'])
        #print(ans)
        fol = str(fol)
        break
    print("%" + fol)
    try:
        fol
    except:
        print("Unsupported sentence")
        return

    fol = fol.replace('.', ' ')
    fol = fol.replace('(', ' ( ')
    fol = fol.replace(')', ' ) ')
    fol = fol.replace(',', ' , ')
    fol = fol.replace('-', ' - ')
    fol = fol.replace('- >', '->')
    fol = fol.split()
    #print(fol)

    print(sentence)
    print("$$")

    for i in range(len(fol)):
        if fol[i] == "all":
            print("\\forall",end=' ')
        
        elif fol[i] == "exists":
            print("\\exists",end=' ')
        
        elif isVariable(i, fol):
            print(replaceNum(i, fol),end=' ')
        
        elif fol[i] == '-':
            print("\\neg",end=' ')

        elif fol[i] == '&':
            print("\\wedge",end=' ')
        
        elif fol[i] == '->':
            print("\\Rightarrow",end=' ')
        
        elif fol[i] == '(' or fol[i] == ')' or fol[i] == ',':
            print(fol[i],end=' ')
        
        else:
            print("\\text{",end=' ')
            print(fol[i],end=' ')
            print('}',end=' ')

    print("\n$$")
    print('\\newline')

def verbose(sentence):
    tokens = sentence.split()
    parser = load_parser('./grammar.fcfg',trace=1)
    trees = parser.parse(tokens)
    for tree in trees:
        fol = (tree.label()['SEM'])
        print("\nResult:\n" + str(fol))
        break


if __name__ == "__main__":
    sentence = sys.argv[1]
    if "-v" in sys.argv:
        verbose(sentence)
    elif sentence == "Head":
        outputHead()
    elif sentence == "End":
        outputEnd()
    else:
        convert(sentence)
