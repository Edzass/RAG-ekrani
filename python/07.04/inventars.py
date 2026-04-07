def generet_dargumus(limenis):
    """Funkcija ģenerē dārgumus."""
    import random
    
    somLiel = 20
    m=["Zelts", "Zobens", "Nekas"]


    if random.randint(1, 100)<=limenis*10:
        return m[0]
    else:
        return random.choice(m);


def inventera_izvade(inventars):
    print("Inventārs:" + str(inventars))