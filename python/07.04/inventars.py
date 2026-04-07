def generet_dargumus(limenis):
    """Funkcija ģenerē dārgumus."""
    import random
    
    mantas=["Zelts", "Zobens", "Nekas"]


    if random.randint(1, 100)<=limenis*10:
        return mantas[0]
    else:
        return random.choice(mantas);


def izdrukat_inventaru(inventars):
    """Funkcija izdrukā inventāru."""
    mantas=["Zelts", "Zobens", "Nekas"]
    print("Inventārs:" + str(mantas[inventars]))