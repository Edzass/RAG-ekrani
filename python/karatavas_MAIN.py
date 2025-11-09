import random

vardu_saraksts = ["ābols", "banāns", "ķirsis", "melone", "apelsīns", "zemene", "vīnoga"]
atbilde = "j"

dzivibu_skaits = 6
meklejamais_vards = ""
varda_stavoklis = []
meklētie_burti = []
karatavas_attels = []

# Funkcija, kas attēlo karātavas skici atbilstoši atlikušo dzīvību skaitam
def attels():
    global dzivibu_skaits
    if dzivibu_skaits == 5:
        print("""
        +---+
        |   |
            |
            |
            |
            |
        =========
        """)
    elif dzivibu_skaits == 4:
        print("""
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """)
    elif dzivibu_skaits == 3:
        print("""
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """)
    elif dzivibu_skaits == 2:
        print("""
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """)
    elif dzivibu_skaits == 1:
        print("""
        +---+
        |   |
        O   |
       /|   |
       /    |
            |
        =========
        """)
    elif dzivibu_skaits == 0:
        print("""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """)
    return

# Funkcija, kas atiestata spēles mainīgos, ja spēle tiek atkārtota
def vertibas():
    global dzivibu_skaits, varda_stavoklis, meklētie_burti, meklejamais_vards
    dzivibu_skaits = 6
    meklejamais_vards = ""
    varda_stavoklis = []
    meklētie_burti = []
    return

# Funkcija, kas uzskāk spēli, izvēloties nejaušu vārdu no saraksta un sagatavo spēles mainīgos
def sakums():
    global meklejamais_vards, varda_stavoklis, meklētie_burti, dzivibu_skaits
    meklejamais_vards = vardu_saraksts[random.randint(0, len(vardu_saraksts)-1)]
    for x in meklejamais_vards:
        varda_stavoklis.append("_")
    return

# Galvenā spēles funkcija, kas satur ciklu, kurā notiek spēles gaita
def spele():
    global dzivibu_skaits, varda_stavoklis, meklētie_burti, meklejamais_vards
    while dzivibu_skaits > 0:
            print(" ".join(varda_stavoklis))
            ievade = str(input("Ievades burts: ")).lower()

            if len(ievade) != 1:
                print("Lūdzu ievadi tikai vienu burtu!")
                

            if ievade in meklejamais_vards and ievade not in varda_stavoklis:
                print("PAREIZI")
                for i in range (len(meklejamais_vards)):
                    if ievade == meklejamais_vards[i]:
                        varda_stavoklis[i]=ievade
                if meklejamais_vards == "".join(varda_stavoklis):
                    print("Uzvara!!!!")
                    print("Meklējamais vārds bija:", meklejamais_vards.upper())
                    break
                            
            elif ievade in meklētie_burti or ievade in varda_stavoklis:
                print("Jau meklēji burutu:", ievade)
            else:
                dzivibu_skaits -=1
                meklētie_burti.append(ievade)
                attels()
            
            print("Dzivibu skaits:", dzivibu_skaits)
            print("Nederīgie burti:", meklētie_burti)
            print("")


# Programmas cilks, kas izpilda funkcijas, lai spēle funkcionētu un būtu iespēja to atkārtot
while atbilde == "j":
    sakums()
    spele()
    atbilde = input("Vai vēlies atkārtot spēli? (j/n)")
    vertibas()

