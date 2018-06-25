from nltk import load_parser

parser = load_parser('./grammar.fcfg')
sentence = 'Every student at STU is smart'
#print(sentence)
tokens = sentence.split()
trees = parser.parse(tokens)
for tree in trees:
    fol = (tree.label()['SEM'])
    #print(ans)
    fol = str(fol)
    break
#print(fol)
try:
    fol
except:
    print("Unsupported sentence")
    exit()

fol = fol.replace('.', ' ')
fol = fol.replace('(', ' ( ')
fol = fol.replace(')', ' ) ')
fol = fol.replace(',', ' , ')
fol = fol.replace('-', ' - ')
fol = fol.replace('- >', '->')
fol = fol.split()
#print(fol)

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

outputHead()
print(sentence)
print("$$")

for i in range(len(fol)):
    if fol[i] == "all":
        print("\\forall")
    
    elif fol[i] == "exists":
        print("\\exists")
    
    elif isVariable(i, fol):
        print(replaceNum(i, fol))
    
    elif fol[i] == '-':
        print("\\neg")

    elif fol[i] == '&':
        print("\\wedge")
    
    elif fol[i] == '->':
        print("\\Rightarrow")
    
    elif fol[i] == '(' or fol[i] == ')' or fol[i] == ',':
        print(fol[i])
    
    else:
        print("\\text{")
        print(fol[i])
        print('}')

print("$$")
outputEnd()