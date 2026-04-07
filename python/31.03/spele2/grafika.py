def zimet_hp(vārds, hp):
    if hp < 0:
         hp = 0
    print(vārds + ": " + "█" * hp)