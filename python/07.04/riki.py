
import time

def pauze_pirms_teksta(teksts, sekundes):
    """Izdrukā tekstu pēc gaidīšanas."""
    print(f"Pauze pirms teksta: {sekundes} sekundes")
    time.sleep(sekundes)
    print(teksts)