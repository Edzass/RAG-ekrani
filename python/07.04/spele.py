from inventars import generet_dargumus, izdrukat_inventaru
from riki import pauze_pirms_teksta


speletaja_limenis = 3


pauze_pirms_teksta("Gatavojies cīņai...", 2)
pauze_pirms_teksta("...CĪŅA SĀKAS!", 2)

print("Spēlētāja līmenis:", speletaja_limenis)
print("Atrastais laupījums:", generet_dargumus(speletaja_limenis))
izdrukat_inventaru(1)