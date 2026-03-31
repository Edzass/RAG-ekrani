import random

def generet_ienaidnieku():
    ienaidnieki = ["Skelets", "Orks", "Pūķis", "Vampīrs", "Goblins"]
    vards = random.choice(ienaidnieki)
    speks = random.randint(1, 10)
    return vards, speks

v, s = generet_ienaidnieku()
print(f"Ienaidnieks parādījies: {v} ar spēku {s}.")
