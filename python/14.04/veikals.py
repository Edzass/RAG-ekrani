cenradis = {"Zobens" : 25 , "Loks" : 15 , "Vairogs" : 30, "Bruņas" : 40,}
def pirkt_lietu(nosaukums):
    if nosaukums in cenradis:     
        cena = cenradis[nosaukums]
        print(f"Tu nopirki {nosaukums} par {cena} zelta monētām.")
    else:
        print("Prece nav pieejama veikalā: 0")


pirkt_lietu(input("ievadi preces nosaukumu:"))