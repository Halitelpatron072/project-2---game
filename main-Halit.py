import sys
from time import sleep

chiggacoins = 0

# Functie om tekst te printen in een coole stijl
def typewrite(str):
    for karakter in str:
        sleep(0.015)
        sys.stdout.write(karakter)
        sys.stdout.flush()
    sys.stdout.write('\n')

def addcoin(coins):
    global chiggacoins
    chiggacoins += coins
    typewrite(f"Je hebt {coins} chiggacoin(s) gekregen. Je hebt nu in totaal {chiggacoins} chiggacoin(s)\n\n")

def eind():
    typewrite(f"Je hebt het spel beëindigd met {chiggacoins} chiggacoin(s)")
    exit()

# Print het logo uit
print("""
░█████╗░██╗░░██╗██╗░██████╗░░██████╗░░█████╗░  ██╗███╗░░██╗░█████╗░░░░
██╔══██╗██║░░██║██║██╔════╝░██╔════╝░██╔══██╗  ██║████╗░██║██╔══██╗░░░
██║░░╚═╝███████║██║██║░░██╗░██║░░██╗░███████║  ██║██╔██╗██║██║░░╚═╝░░░
██║░░██╗██╔══██║██║██║░░╚██╗██║░░╚██╗██╔══██║  ██║██║╚████║██║░░██╗░░░
╚█████╔╝██║░░██║██║╚██████╔╝╚██████╔╝██║░░██║  ██║██║░╚███║╚█████╔╝██╗
░╚════╝░╚═╝░░╚═╝╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝  ╚═╝╚═╝░░╚══╝░╚════╝░╚═╝
© 2025 - 2025 www.Chigga.com - All Rights Reserved.
""")

input("> Druk op ENTER om verder te gaan ")

# Menu en naam input
while True:
    typewrite("1. Speel het spel, a sahbi\n2. Stop\n\n")
    menu = input("> ")

    if menu == "2":
        exit()
    elif menu == "1":
        typewrite("Wat is je naam, a sahbi?\n")
        naam = input("> ")
        typewrite(f"Ewa, {naam}")
        input("> Druk op ENTER om verder te gaan")
        typewrite("Voordat je begint, wil je fent?\n\nja\n\nnee")
        keuze = input("> ")

        # menu einde 1
        if keuze == "nee":
            typewrite("Isg\n\n")
            eind()
        elif keuze == "ja":
            typewrite("Ai\n\n")
            break
        else:
            typewrite("Ongeldige keuze")
            continue

    # Ongeldige keuze (opnieuw kiezen van dit sectie)
    else:
        typewrite("Ongeldige keuze")
        continue

# Keuze 2 (spel keuze 1)
while True:
    if keuze == "ja":
        typewrite("Je zit vast in de gevangenis van Chopped Chin,\nmaar jij wilt hier zo snel mogelijk weg.\nDus je gaat je best doen om te ontsnappen.\n")
        typewrite("Wat wil je doen?\n")
        typewrite("1. Alle laatjes onder je bed doorzoeken\n\n2. De bewaker misleiden")
        keuze2 = input("> ")

        # Keuze die leidt naar keuze3 (spel keuze 2)
        if keuze2 == "1":
            typewrite("Je hebt opeens allerlei soorten schroevendraaiers gevonden\nen je kijkt om je heen en ziet een ventilatierooster boven\nje bed. Je maakt het open en gaat erin,\ngoed gedaan, " + naam + "\n\n")
            addcoin(1)
            input("> Druk op ENTER om verder te gaan")
            break

        # Keuze die leidt naar einde 1
        elif keuze2 == "2":
            typewrite("Je deed alsof je ziek was, maar de bewaker\nhad je door.\n\n(Einde 1)\n\n")
            eind()

        # Ongeldige keuze (opnieuw kiezen van dit sectie)
        else:
            typewrite("Ongeldige keuze\n")
            continue

# Keuze 3 (spel keuze 2)
while True:
    typewrite("Je kruipt door de ventilatiegangen om een uitgang te vinden,\nmaar je hebt alleen twee ventilatieroosters gevonden. Een links en een rechts.\n")
    typewrite("Welke ga je kiezen?\n\n")
    typewrite("1. Links\n\n2. Rechts\n\n")
    keuze3 = input("> ")

    # Einde 2
    if keuze3 == "1":
        typewrite("Je hebt het linker ventilatierooster geopend en je valt weer in een cel,\nmaar je bent niet alleen...\nnee, je bent in de cel terechtgekomen van 'El yamyam'.\nJe bent dus uiteindelijk nog steeds niet ontsnapt en hij heeft je opgegeten.\n\n(Einde 2)\n\n")
        eind()

    # Keuze die je leidt naar keuze4 (spel keuze 3)
    elif keuze3 == "2":
        typewrite("Je opent het rechter ventilatierooster en je valt in een kleedkamer waar niemand is.\nJe kijkt rond en vindt een open locker met een bewakersuniform\nPRECIES jouw maat, toevallig, en je doet het aan en loopt uit de kleedkamer.\n\n")
        addcoin(1)
        input("> Druk op ENTER om verder te gaan ")
        break

    # Ongeldige keuze (opnieuw kiezen van dit sectie)
    else:
        typewrite("Ongeldige keuze\n")
        continue

# Keuze 4 (spel keuze 3)
while True:
    typewrite("Je kleedt je aan als een bewaker en loopt uit de kleedkamer,\nmaar toen zag je een bewaker die zich afvroeg wat je 's nachts hier doet\nen vroeg om je ID. Wat ga je doen?")
    typewrite("Wat ga je doen, " + naam + "?\n")
    typewrite("1. Vriendelijk zijn en over andere dingen praten\n\n2. Hem knock-out slaan\n\n3. Wegrennen")
    keuze4 = input("> ")

    # Einde 3
    if keuze4 == "1":
        typewrite("Hij vond je aardig en nam je mee naar een bar. Jullie werden beste vrienden en niemand raakte gewond.\n\n(Einde 3)\n\n")
        eind()

    # Keuze die leidt naar keuze5 (spel keuze 4)
    elif keuze4 == "2":
        typewrite("Je slaat hem knock-out en verstopt zijn\nlichaam in een donkere hoek. Je pakt zijn wapen.\n\n")
        addcoin(1)
        input("> Druk op ENTER om verder te gaan ")
        break

    # Keuze die leidt naar keuze6 (spel keuze 5)
    elif keuze4 == "3":
        typewrite("Je rent weg en je ziet dat hij achter je aanrent.\n\n")
        addcoin(1)
        input("> Druk op ENTER om verder te gaan ")
        break

    # Ongeldige keuze (opnieuw kiezen van dit sectie)
    else:
        typewrite("Ongeldige keuze\n")
        continue

# Keuze5 (spel keuze 4)
if keuze4 == "2":
    while True:
        typewrite("Je hebt de bewaker knock-out geslagen, maar nu heb je zijn wapen.\nWat ga je doen, " + naam + "?\n")
        typewrite("1. Het wapen gebruiken om een andere bewaker te doden\n\n2. Het wapen bewaren en verder gaan")
        keuze5 = input("> ")

        # Keuze die leidt naar einde 4
        if keuze5 == "1":
            typewrite("Je gebruikt het wapen en doodt de bewaker die al bewusteloos lag, maar het alarm gaat af. Ga daar zo snel mogelijk weg!\n\n")
            addcoin(1)
            break

        elif keuze5 == "2":
            typewrite("Je bewaart het wapen en besluit verder te gaan zonder te vechten.\n\n")
            addcoin(1)
            break

        # Ongeldige keuze (opnieuw kiezen van dit sectie)
        else:
            typewrite("Ongeldige keuze\n")
            continue

    # Einde 4
    if keuze5 == "1":
        typewrite("Je rent en rent en rent en vindt uiteindelijk de\nuitgang. Je opent de deur, helemaal blij\nen denkt na over wat je allemaal gaat doen als je vrij bent, maar je hebt te vroeg gejuicht,\nwant de politie is er al. Je geeft je over en gaat de bak weer in.\n\n(Einde 4)\n\n")
        eind()

    # Einde 5
    elif keuze5 == "2":
        typewrite("Je kiest om niet te schieten en je vindt een uitgang. Je loopt weg en gaat lekker naar huis als een soldaat.\n\n(Lijpe einde)\n\n")
        eind()

# Keuze6 (spel keuze 5)
elif keuze4 == "3":
    while True:
        typewrite("Je rent snel weg en je hoort de bewaker achter je roepen.\nWat ga je nu doen, " + naam + "?\n")
        typewrite("1. Je verstoppen in een kamer\n\n2. Naar de uitgang rennen\n\n3. Je verstoppen in een toilet\n\n4. Een lijpe ritueel uitvoeren")
        keuze6 = input("> ")

        # Keuze die leidt naar einde 9
        if keuze6 == "1":
            typewrite("Je verstopt je in een kamer en hoopt dat de bewaker je niet vindt.\nJe kijkt achter je en ziet IDKsterling.\nHij zegt dat hij een uitweg weet en je volgt hem.\n\n")
            addcoin(1)
            input("> Druk op ENTER om verder te gaan ")
            break

        # Einde 6
        elif keuze6 == "2":
            typewrite("Je rent naar de uitgang, maar de bewakers zitten vlak achter je en ze hebben je doodgeschoten, a sahbi.\n\n(Je bent gedood einde)")
            eind()

        # Keuze die leidt naar einde 7
        elif keuze6 == "3":
            typewrite("Je verstopt je in een toilet en je legt een dikke beuker\ndoor die pittige sucuk die je vanmiddag at.\nNa je boodschap zie je dat er een klein raampje boven het toilet zit.\nDe bewaker is er inmiddels al en trapt op de deur,\ndus je veegt af en klimt door het raam.")
            addcoin(1)
            input("> Druk op ENTER om verder te gaan ")
            break

        # Einde 8
        elif keuze6 == "4":
            typewrite("Je voert een lijpe ritueel uit en roept John'Chigga'Pork op uit de dood. Hij vermoordt iedereen en neemt je mee naar buiten. Je bent ontsnapt.\n\n(Ritueel einde)")
            eind()

        # Ongeldige keuze (opnieuw kiezen van dit sectie)
        else:
            typewrite("> Ongeldige keuze\n")
            continue

    # Einde 9
    if keuze6 == "1":
        typewrite("Je ziet dat Sterling al een gat heeft gegraven\ndat naar het riool leidt en je volgt hem.\nJe ontsnapt uiteindelijk uit de gevangenis.\n\n(Onstnapt met IDKsterling einde)\n\n")
        eind()

    # Einde 7
    elif keuze6 == "3":
        typewrite("Je hebt maar weinig tijd, " + naam + ". De bewaker probeert de deur open te trappen. Klim nu uit het raam.")
        addcoin(1)
        input("Druk op ENTER om 'uit het raam te klimmen'")
        typewrite("Je bent door het raam geklommen en je rent weg. Je bent ontsnapt.\n\n(Toiletraam ontsnapping einde)\n\n")
        eind()