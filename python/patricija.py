import random

print("Sveiks! ")
print("Tu spēlēsi spēli karātavas")
print("IEGAUMĒ")
print("Tev ir 7 dzīvības")
atbilde="j"

# Speles funkcija, kas izpilda spēli vienu reizi 
def spele():
    vardu_saraksts=["koks", "kaķis", "zaķis"]
    atrodamais_vards=vardu_saraksts[random.randint (0,len(vardu_saraksts)-1)]
    varda_stavoklis= []
    mekletie_burti= []
    

    for x in atrodamais_vards:
        varda_stavoklis.append("_")


    dzivibu_skaits=7    
    while dzivibu_skaits > 0:
        print(" ".join(varda_stavoklis))
        ievade = str(input("burts:"))

        if ievade in atrodamais_vards:
            print("PAREIZI")
            for b in range(len(atrodamais_vards)):
                if ievade == atrodamais_vards[b]:
                    varda_stavoklis[b]=ievade
                if atrodamais_vards =="".join(varda_stavoklis):
                    print("Uzvara!!!")
                    print("Meklējamais vārds bija:", atrodamais_vards)
                    return
                    
        
            if ievade in mekletie_burti or ievade in varda_stavoklis:
                print("Jau ievdīts burts :", ievade)
            else:
                dzivibu_skaits -=1
                mekletie_burti.append(ievade)
        print("Atlikušais dzivibu skaits:", dzivibu_skaits)
        print("Izmantotie burti:", mekletie_burti)
        print("")
        
    if dzivibu_skaits == 0:
        print("Spēle beigusies! Vārds bija:", atrodamais_vards)

# galvenais cikls, kas ļauj spēlēt atkrtoties 
while atbilde == "j":
    spele()
    atbilde = input("Vai vēlies atkārtot spēli? (j/n)")