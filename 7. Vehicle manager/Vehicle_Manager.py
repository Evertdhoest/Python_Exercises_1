# Class aanmaken
class voertuig:
    # Inhoud objecten bepalen
    def __init__(self, merk, model, afstand, onderhoud):
        self.merk = merk
        self.model = model
        self.afstand = afstand
        self.onderhoud = onderhoud

# Lijst met voertuigen opnoemen
def voertuigenlijst(voertuigen):
        # Als de lijst leeg is
    if voertuigen == []:
        print("")
        print("Er zit geen voertuig in het programma.")
        print("")
    else:
    # Opsomming indien er al voertuigen in de lijst staan
        for index, voertuig in enumerate(voertuigen):
            print("")
            print (voertuig.merk + " " + voertuig.model + " met " + voertuig.afstand + " kilometers en laatste onderhoud op " + voertuig.onderhoud)

# Nieuw voertuig methode
def nieuw_voertuig_toevoegen(voertuigen):
    merk = input("Wat is het merk van het voertuig: ")
    model = input("Welk model is het voertuig: ")
    afstand = input("Hoeveel kilometers heeft het voertuig: ")
    onderhoud = input("Wanneer was het onderhoud: ")

    nieuw_voertuig = voertuig(merk=merk, model=model, afstand=afstand, onderhoud=onderhoud)
    voertuigen.append(nieuw_voertuig)

    print("")
    print("Dit voertuig werd toegevoegd aan Voertuigbeheer3000.")

# Methode kilometers aanpassen
def kilometers_aanpassen(voertuigen):
    print("kies het nummer van het voertuig dat u wil aanpassen: ")

    for index, voertuig in enumerate(voertuigen):
        print(str(index) + " . " + voertuig.merk + " " + voertuig.model)

    print("")
    voertuigkeuze = input("Welk voertuig wenst u aan te passen? (voer nummer in): ")
    gekozen_voertuig = voertuigen[int(voertuigkeuze)]

    nieuwe_afstand = input("Voeg een nieuwe kilometerstand in: ")
    gekozen_voertuig.afstand = nieuwe_afstand

    print ("")
    print ("De nieuwe kilometerafstand is toegevoegd.")
    print("")

# Methode Onderhoudsdatum wijzigen
def onderhoud_aanpassen(voertuigen):
    print("kies het nummer van het voertuig dat u wil aanpassen: ")

    for index, voertuig in enumerate(voertuigen):
        print(str(index) + " . " + voertuig.merk + " " + voertuig.model)

    print("")
    voertuigkeuze = input("Welk voertuig wenst u aan te passen? (voer nummer in): ")
    gekozen_voertuig = voertuigen[int(voertuigkeuze)]

    nieuwe_onderhoudsdatum = input("Kies een nieuwe onderhoudsdatum: ")
    gekozen_voertuig.onderhoud = nieuwe_onderhoudsdatum

    print("")
    print ("Datum toegevoegd.")
    print("")



# Uitvoeren programma
def main():
    print("Welkom bij Voertuigbeheer3000")

    kia_ceed = voertuig(merk="Kia", model="Cee'd", afstand="93000", onderhoud="01/08/2018")

    voertuigen = [kia_ceed]

    # Keuzemenu
    while True:
        print("")
        print ("Kies een optie:")
        print ("1. Bekijk alle voertuigen")
        print ("2. Voeg een voertuig toe")
        print ("3. pas de kilometers aan van een voertuig")
        print ("4. Pas de onderhoudsdatum aan")
        print ("5. Verlaat het programma")
        print("")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            voertuigenlijst(voertuigen)
        elif keuze == "2":
            nieuw_voertuig_toevoegen(voertuigen)
        elif keuze == "3":
            kilometers_aanpassen(voertuigen)
        elif keuze == "4":
            onderhoud_aanpassen(voertuigen)
        elif keuze == "5":
            print("Voertuigbeheer3000 is gestopt!")
            break
        else:
            print("Gelieve een geldige keuze te maken")
            continue

if __name__ == '__main__':
    main()