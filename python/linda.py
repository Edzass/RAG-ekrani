import random
turpinat= "j"

# Speles funkcija, kas izpilda spēli vienu reizi
def spele():
    vardu_saraksts=["sliekas","gliemezis","magone", "lapsa"]
    dzivibas=7
    nezinamais_vards= vardu_saraksts[random.randint(0,len(vardu_saraksts)-1)]
    varda_stavoklis=[]
    mekletie_burti=[]
    for x in nezinamais_vards: varda_stavoklis.append("_")
 

    while dzivibas > 0:
        print(" ".join(varda_stavoklis))
        ievade= (input("burts:").lower())
        if ievade in nezinamais_vards:
            print("Pareizi")
            for c in range (len(nezinamais_vards)):
                if ievade == nezinamais_vards[c]:
                    varda_stavoklis[c]=ievade
                if nezinamais_vards =="".join(varda_stavoklis):
                    print("uzvara")
                    return
                
        elif ievade in mekletie_burti or ievade in varda_stavoklis:
                print("jau ievadiji")
        else:
                dzivibas-=1
                mekletie_burti.append(ievade)
        print("Dzīvību skaits", dzivibas)
        print("Ievadītie burti", mekletie_burti)
        print("")

    if dzivibu_skaits == 0:
        print("Spēle beigusies! Vārds bija:", nezinamais_vards)

# galvenais cikls, kas atkarto speli
while turpinat == "j":
    spele()
    turpinat= input("vai velies turpinat? (j/n)")
