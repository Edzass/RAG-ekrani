import time, sys
def druka_lenam(teksts):
    for simbols in teksts:
        print(simbols, end="", flush=True)
        time.sleep(0.05) # Pauze starp burtiem (sekundēs)
    print() # Beigās pāriet jaunā rindā

def apraksti_vietu(nosaukums, apraksts):
    print("=============")
    print(nosaukums.upper())
    druka_lenam(apraksts)
    print("=============")

apraksti_vietu("Tumss mežs", "Meža ekosistēmā ietipst dažādi seni koki un dabiskas dzīvotnes.")
apraksti_vietu("Zala pļava", "Pļavas ekosistēmā ietilpst daudzveidīgs augu kāsts. Bieži var vērot dažādus putnus, piemēram, Dzērves.")