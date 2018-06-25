## Supported sentences (examples):
    [Name] is in/at the [place]
    [Name] is [Adj]
    Alice is happy
    Bob is in the kitchen

    Every/Some/No [Noun] is/are
    Every student at STU is smart
    Some boys in the garden are drunk
    No student is married

    Alice chases Bob
    Alice chases the dog
    The dog (in the garden) barks

    Alice does know Bob
    Every person knows STU
    ...


- More names, places and adjs should be added in `grammar.fcfg`

- Name: `PropN[-LOC,NUM=sg,SEM=<\P.P(Alice)>] -> 'Alice'`

- Place: `N[NUM=sg,SEM=<\x.garden(x)>] -> 'garden'`

- ADJ: `Adj[SEM=<\x.happy(x)>] -> 'happy'`

- Verb: `TV[NUM=sg,SEM=<\X y.X(\x.see(y,x))>,tns=pres] -> 'sees'`

    `TV[NUM=pl,SEM=<\X y.X(\x.see(y,x))>,tns=pres] -> 'see`

    `IV[NUM=sg,SEM=<\x.walk(x)>,tns=pres] -> 'walks'`

    `IV[NUM=pl,SEM=<\x.walk(x)>,tns=pres] -> 'walk'`

- Other Noun: `N[NUM=sg,SEM=<\x.student(x)>] -> 'student'`

    `N[NUM=pl,SEM=<\x.student(x)>] -> 'students'`

- 'and' is not suported yet due to the complicated rules