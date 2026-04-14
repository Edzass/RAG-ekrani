varonis = {"vards" : 2 , "hp" : 100 , "speks" : 50 , "zelts" : 100}

def paradi_datus(tels):
    print(f"Spēlētāja vārds: {tels['vards']}, HP: {tels['hp']}, ZELTS: {tels['zelts']}")

paradi_datus(varonis)
varonis["zelts"] += 50
paradi_datus(varonis)
    