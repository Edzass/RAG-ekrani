def ir_dzivs(hp):
    if hp > 0:
        return True
    else:
        return False
mana_veseliba = 45

if ir_dzivs(mana_veseliba):
    print("Turpini cīņu!")
else:    print("Spēle beigusies!")