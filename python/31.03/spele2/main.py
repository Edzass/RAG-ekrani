import kauja
import grafika

speletaja_hp = 20
orka_hp = 30

while speletaja_hp > 0 and orka_hp > 0:

    input("Spied Enter, lai uzbruktu!")

    orka_hp -= kauja.speletaja_uzbrukums()
    print(f"Tu nodari {kauja.speletaja_uzbrukums()} bojājumus pretiniekam!")
    speletaja_hp -= kauja.ienaidnieka_uzbrukums()
    print(f"Orks nodara tev {kauja.ienaidnieka_uzbrukums()} bojājumus!")

    grafika.zimet_hp("Spēlētājs", speletaja_hp)
    grafika.zimet_hp("Orks", orka_hp)

if speletaja_hp <= 0:
    print("Tu zaudēji!")
else:  
    print("Tu uzvarēji!")

