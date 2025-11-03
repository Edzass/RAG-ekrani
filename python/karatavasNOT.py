import random

vardu_saraksts= ["abols", "banans", "kirsis"]
dzivibu_skaits= 7
meklejamais_vards= ""
varda_stavoklis= []
meklētie_burti= []

atbilde = "j"




def sakums(meklejamais_vards, vardu_saraksts, varda_stavoklis):
    meklejamais_vards = vardu_saraksts[random.randint(0, len(vardu_saraksts)-1)]
    for x in meklejamais_vards:
        varda_stavoklis.append("_")
    return vardu_saraksts, meklejamais_vards, varda_stavoklis


def spele(dzivibu_skaits, varda_stavoklis, meklejamais_vards, meklētie_burti):
    while dzivibu_skaits > 0:
        print(" ".join(varda_stavoklis))
        ievade = str(input("burts")).lower()
        if ievade in meklejamais_vards:
            print("PAREIZI")
            for i in range (len(meklejamais_vards)):
                if ievade == meklejamais_vards[i]:
                    varda_stavoklis[i]=ievade
            if meklejamais_vards == "".join(varda_stavoklis):
                print("Uzvara!!!!")
                break
                        
        else:
            if ievade in meklētie_burti:
                print("Jau meklēji.")
            else:
                dzivibu_skaits -=1
                meklētie_burti.append(ievade)
        print(ievade)
        print("Dzivibu skaits:", dzivibu_skaits)
        print("Dzivibu skaits:", meklētie_burti)
        print("")

    return dzivibu_skaits, meklejamais_vards, varda_stavoklis, meklētie_burti

print(meklejamais_vards)
print(varda_stavoklis)


# while atbilde == "j":
# atbilde = input("Vai vēlies atkārtot? (j/n)")

sakums(meklejamais_vards, vardu_saraksts,  varda_stavoklis)
spele(dzivibu_skaits, varda_stavoklis, meklejamais_vards, meklētie_burti)
    