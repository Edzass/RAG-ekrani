import time
import os

def jaut1():
    print("Tu uzmosties uz nezināmas planētas.")
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    print(".")
        # notīra ekrānu pēc spēles beigām
    os.system('cls')
    print("Tev pīkstst skābeļa maska, kas liecina par skābekļa rezervju beigušanos.")
    time.sleep(1)
    print("Tava rīcība:")
    print("1.Celties un meklēt jaunu masku.")
    print("2.Ignorēt pīkstienu un turpināt gulēt.")
    atbilde = input("Ievadi 1 vai 2: ")
    if atbilde == "1":
        print("Tu piecelies un dodies ties meklēt jaunu skābekļa masku.")
        time.sleep(0.3)
        os.system('cls')
        jaut2()
    if atbilde == "2":
        os.system('cls')
        time.sleep(0.3)
        print("Pēc brīža tu sajūti, ka skābekļa rezerves ir beigušās un tu aizrijies.")
        time.sleep(1)
        print("Spēle beigusies!")

def jaut2():
    print("Tu redzi tālumā kosmosa kuģi, kas dūmo, iespējams, tur ir vēl kāds izdzīvojušais.")
    time.sleep(1)
    print("Tava rīcība:")
    print("1.Doties uz kosmosa kuģi (10min).")
    print("2.Doties meklēt palīdzību uz pilsētu-vadoties pēc tālumā mirgojošām gaismiņām (20min).")
    atbilde = input("Ievadi 1 vai 2: ")
    if atbilde == "1":
        os.system('cls')
        print("Tu redzi, ka kuģis ir pilnībā iznīcināts, un tu nevari atrast nevienu izdzīvojušo.")
        time.sleep(1)
        os.system('cls')
        print("TOMĒR")
        time.sleep(1)
        os.system('cls')
        print("Tu ieraugi interesantu somu.")
        jaut3()
    if atbilde == "2":
        os.system('cls')
        time.sleep(0.3)
        print("Tu nevari iejiet pilsētā, jo tā ir aizsargāta ar enerģijas lauku.")
        time.sleep(1)
        print("Spēle beigusies!")

def jaut3():
    print("Tava rīcība:")
    print("1.Ieskatīties somā.")
    print("2.Meklēt pēc negadījuma videoklipa- kuģa melnajā kastē.")
    atbilde = input("Ievadi 1 vai 2: ")
    if atbilde == "1":
        os.system('cls')
        print("Tur atrodas jauns skābekļa baloniņš un pārtikas krājumi.")
        time.sleep(0.6)
        print("Turpinājums sekos...")
    if atbilde == "2":
        os.system('cls')
        time.sleep(0.3)
        print("Tev izdodas atrast melno kasti.")
        time.sleep(1)
        os.system('cls')
        print("Tur ir redzams, ka draugs ir veicis sabotāžu.")
        time.sleep(1)
        print("Turpinājums sekos...")


jaut1()
