## CYK (https://github.com/TUCircle/CYK)
- Start the programm with `python cyk.py "abba"`.
- You will see a table inside your console for the word "abba" with the given rules inside the config.py file.
- If you want to change the rules you need to change the `config.py` file which is in the same directory.
- If you want you can print the table as a latex table with `python cyk.py "abba" --latex`
- White spaces are not supported if you don't have a rule about white space.

# Dependency parsing
## 1. spaCy (said to be recommended) (https://spacy.io)
- `pip install spacy`
- Download language model: `python -m spacy download en`
- Example(visualized):
    ```python
    import spacy
    from spacy import displacy

    nlp = spacy.load('en')
    doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers")
    displacy.serve(doc, style='dep')
    ```
    then opening a browser on [localhost:5000](localhost:5000) will see the result.

    `displacy.render(doc, style='dep')` will return a rendered HTML markup instead.

- More examples on https://spacy.io/usage/linguistic-features#section-dependency-parse
## 2. NLTK (need java)
- Download [The Stanford CoreNLP parser](https://nlp.stanford.edu/software/lex-parser.shtml#Download).
- Download [language model](http://nlp.stanford.edu/software/corenlp.shtml) for your desired language (e.g. [english language model](http://nlp.stanford.edu/software/stanford-english-corenlp-2018-02-27-models.jar))
- `pip install nltk`
- Example (for python3):
    ```python
    from nltk.parse.stanford import StanfordDependencyParser

    path_to_jar = '[path_to]\stanford-parser-full-2018-02-27\stanford-parser.jar'
    path_to_models_jar = '[path_to]\stanford-english-corenlp-2018-02-27-models.jar'

    dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

    result = dependency_parser.raw_parse('I shot an elephant in my sleep')
    dep = result.__next__()

    print(list(dep.triples()))
    ```
    output:
    ```python
    [(('shot', 'VBD'), 'nsubj', ('I', 'PRP')), (('shot', 'VBD'), 'dobj', ('elephant', 'NN')), (('elephant', 'NN'), 'det', ('an', 'DT')), (('shot', 'VBD'), 'nmod', ('sleep', 'NN')), (('sleep', 'NN'), 'case', ('in', 'IN')), (('sleep', 'NN'), 'nmod:poss', ('my', 'PRP$'))]
    ```

- For python2, replace `__next__()` with `next()`.


## NLTK + spaCy
``` python
import spacy
from nltk import Tree


en_nlp = spacy.load('en')

doc = en_nlp("The quick brown fox jumps over the lazy dog.")

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
```
Which outputs:
```
        jumps
  ________|______________
 |        |             over
 |        |              |
 |       fox            dog
 |    ____|_____      ___|____
 .  The quick brown the      lazy
 ```
 
 - For changing the token representation you can do this:
    ```python
    def tok_format(tok):
        return "_".join([tok.orth_, tok.tag_])


    def to_nltk_tree(node):
        if node.n_lefts + node.n_rights > 0:
            return Tree(tok_format(node), [to_nltk_tree(child) for child in node.children])
        else:
            return tok_format(node)
    ```
    Which results in:
    ```           
                jumps_VBZ
      _____________|________________________
     |             |                     over_IN
     |             |                        |
     |           fox_NN                   dog_NN
     |     ________|________         _______|_______
    ._. The_DT  quick_JJ brown_JJ the_DT         lazy_JJ
    ```

- Other approaches available on https://stackoverflow.com/a/40320647
