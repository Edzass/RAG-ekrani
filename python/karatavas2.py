import random

vardu_saraksts= ["abols", "banans", "kirsis"]
dzivibu_skaits= 7
meklejamais_vards= ""
varda_stavoklis= []
meklētie_burti= []

atbilde = "j"




def sakums(a, b, c):
    a = b[random.randint(0, len(b)-1)]
    for x in a:
        c.append("_")
    return a , b, c


def spele(a, b, c, d):
    while a > 0:
        print(" ".join(b))
        ievade = str(input("burts")).lower()
        if ievade in c:
            print("PAREIZI")
            for i in range (len(c)):
                if ievade == c[i]:
                    b[i]=ievade
            if c == "".join(b):
                print("Uzvara!!!!")
                break
                        
        else:
            if ievade in d:
                print("Jau meklēji.")
            else:
                a -=1
                meklētie_burti.append(ievade)
        print(ievade)
        print("Dzivibu skaits:", a)
        print("Dzivibu skaits:", c)
        print("")

    return a, b, c, d

print(meklejamais_vards)
print(varda_stavoklis)


# while atbilde == "j":
# atbilde = input("Vai vēlies atkārtot? (j/n)")

sakums(meklejamais_vards, vardu_saraksts,  varda_stavoklis)
spele(dzivibu_skaits, varda_stavoklis, meklejamais_vards, meklētie_burti)
    