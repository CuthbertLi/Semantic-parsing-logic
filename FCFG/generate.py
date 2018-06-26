import os

sentences = [
    'Alice is happy',
    'Bob is in the kitchen',
    'Charlie is in a garden',

    'Every student at STU is smart',
    'Some boys in the garden are sad',
    'All girls are beautiful',
    'No student is married',

    'Alice is not happy',
    'All persons are not sad',

    'A dog barks',
    'All dogs bark',
    'The dog in the garden barks',

    'Alice sees Bob',
    'Alice does know Bob',
    'Alice chases Bob in the garden',
    'All persons in Shanghai know STU',

    'Alice is in the garden with Bob'
]

os.system("python3 ./convert.py" + ' "' +"Head" + '"')

for sentence in sentences:
    os.system("python3 ./convert.py" + ' "' +sentence + '"')

os.system("python3 ./convert.py" + ' "' +"End" + '"')