import random

vardu_saraksts= ["ābols", "banāns", "ķirsis"]
dzivibu_skaits= 7
meklejamais_vards= vardu_saraksts[random.randint(0, len(vardu_saraksts)-1)]
varda_stavoklis= []
meklētie_burti= []

for x in meklejamais_vards:
    varda_stavoklis.append("_")

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
   
    print("Dzivibu skaits:", dzivibu_skaits)
    print("Izmantotie burti:", meklētie_burti)
    print("")
    
print(meklejamais_vards)
print(varda_stavoklis)