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
    typewrite(f"Je hebt {coins} chiggacoin(s) gekregen. Je hebt in totaal nu {chiggacoins} chiggacoin(s)\n\n")

def eind():
    typewrite(f"Je hebt de spel beindigd met {chiggacoins} chiggacoin(s)")
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

input("> Press ENTER to continue ")

# menu en naam input
while True:
    typewrite("1. Play game a sahbi\n2. Quit\n\n")
    menu = input("> ")

    if menu == "2":
        exit()
    elif menu == "1":
        typewrite("Wat is je Naam a sahbi?\n")
        naam = input("> ")
        typewrite(f"ewa, {naam}")
        input("> Press ENTER to continue")
        typewrite("voordat je begint, wil je fent?\n\nja\n\nnee")
        keuze = input("> ")
        
        
        #random keuze (keuze 1)
        if keuze == "nee":
            typewrite("isg\n\n")
            eind()
        elif keuze == "ja":
            typewrite("ai\n\n")
            break
        else:
            typewrite("Ongeldige operatie")
            continue
    
    #ongeldige keuze(opnieuw kiezen van dit sectie)
    else:
        typewrite("Ongeldige operatie")
        continue

# Keuze 2(spel keuze 1)
while True:
    if keuze == "ja":
        typewrite("Je zit vast in de gevangenis van Chopped Chin,\nmaar jij wilt hier zo snel mogelijk weg.\nDus jij gaat je best proberen om te ontsnappen.\n")
        typewrite("Wat wil je doen?\n")
        typewrite("1. Al je laatjes doorzoeken onder je bed\n\n2. Bewaker misleiden")
        keuze2 = input("> ")

        #keuze die leidt naar keuze3(spel keuze 2)
        if keuze2 == "1":
            typewrite("Je hebt opeens uit het niets allerlei soorten schroevendraaiers\ngevonden en je kijkt om je heen en je ziet een ventilatierooster boven\nje bed en je maakt het open en je gaat erin,\ngoed gedaan " + naam + "\n\n")
            addcoin(1)
            input("> Press ENTER to continue")
            break
        
        #keuze die leidt naar einde(Slechte leugenaar)
        elif keuze2 == "2":
            typewrite("Je deed alsof je ziek was en de bewaker\n had je door.\n\n(Slechte leugenaar)\n\n")
            eind()
           
        #ongeldige keuze(opnieuw kiezen van dit sectie)
        else:
            typewrite("Ongeldige keuze\n")
            continue

# Keuze 3(spel keuze 2)
while True:
    typewrite("Je kruipt door de ventilatie gangen om een uitgang te vinden,\nmaar je hebt alleen maar 2 ventilatieroosters gevonden. een links en een rechts.\n")
    typewrite("welke ga je kiezen?\n\n")
    typewrite("1. Links\n\n2. Rechts\n\n")
    keuze3 = input("> ")

    #einde(YamYam)
    if keuze3 == "1":
        typewrite("Je hebt de linker ventilatierooster geopend en je valt weer in een cel,\nmaar je bent niet alleen...\nnee, je bent in het cel terecht gekomen van 'El yamyam'\nJe bent dus uiteindelijk nog steeds niet ontsnapt en hij heeft je opgevreten.\n\n(Yamyam einde)\n\n")
        eind()
    
    #keuze die je leidt naar keuze4(spel keuze 3)
    elif keuze3 == "2":
        typewrite("Je opent de rechter ventilatierooster en je valt in een kleedkamer en niemand is er.\nJe kijkt rond en je vind een open locker met bewaker uniform\nPRECIES jouw maat toevallig en je doet het aan en loopt uit de kleedkamer.\n\n")
        addcoin(1)
        input("> Press ENTER to continue ")
        break
    
    #ongeldige keuze(opnieuw kiezen van dit sectie)
    else:
        typewrite("Ongeldige keuze\n")
        continue

# Keuze 4(spel keuze 3)
while True:
    typewrite("Je kleed aan als een bewaker en je loopt uit de kleedkamer enzo,\nmaar toen zag je een bewaker en hij vroeg zich af wat je doet in de nacht hier doet\nen vroeg voor je id. Wat ga je doen?")
    typewrite("wat ga je doen" + naam +"?\n")
    typewrite("1. vriendelijk zijn en over andere dingen praten\n\n2. Hem knockout slaan slaan\n\n3. Wegrennen")
    keuze4 = input("> ")

    #einde(Happy)
    if keuze4 == "1":
        typewrite("Hij vond je aardig en nam je mee naar een bar en jullie waren beste vrienden en niemand was gewond.\n\n(Happy einde)\n\n")
        eind()
    
    #keuze die leidt naar keuze5(spel keuze 4)
    elif keuze4 == "2":
        typewrite("Je slaat hem in elkaar en je verstopt zijn\nlichaam in een donkere hoek en je pakt zijn wapen\n\n")
        addcoin(1)
        input("> Press ENTER to continue ")
        break
    
    #keuze die leidt naar keuze6(spel keuze 5)
    elif keuze4 == "3":
        typewrite("Je rent weg en je ziet dat hij achter je aanrent\n\n")
        addcoin(1)
        input("> Press ENTER to continue ")
        break
    
    #ongeldige keuze(opnieuw kiezen van dit sectie)
    else:
        typewrite("Ongeldige keuze\n")
        continue

#keuze5(spel keuze 4)
if keuze4 == "2":
    while True:
        typewrite("Je hebt de bewaker in elkaar geslagen, maar nu heb je zijn wapen.\nWat ga je doen" + naam +"?\n")
        typewrite("1. Wapen gebruiken om een andere bewaker te doden\n\n2. Wapen bewaren en verder gaan")
        keuze5 = input("> ")

        #keuze die leidt naar einde(Dikke pech)
        if keuze5 == "1":
            typewrite("Je gebruikt het wapen en doodt de bewaker die al onbewusteloos lag, amar de alarm ging af. Ga daar zo snel mogelijk weg!\n\n")
            addcoin(1)
            break
        
        
        elif keuze5 == "2":
            typewrite("Je bewaart het wapen en besluit verder te gaan zonder te vechten.\n\n")
            addcoin(1)
            break
        
        #ongeldige keuze(opnieuw kiezen van dit sectie)
        else:
            typewrite("Ongeldige keuze\n")
            continue

#einde(Dikke pech)
if keuze5 == "1":
    typewrite("Je rent en rent en rent en uiteindelijk de\nuitgang gevonden. Je doet de deur open helemaal blij\nen denkt wat je allemaal gaat doen als je vrij bent, maar je hebt te vroeg gejuicht,\nwant de politie is er al. JE geeft je over en je gaat de bak weer in.\n\n(Dikke pech einde)\n\n")
    eind()

#einde(Lijpe einde)
if keuze5 == "2":
    typewrite("Je kiest om niet te schieten en je vind een uitgang en je loopt weg en je gaat lekker naar huis als een soldaat\n\n(Lijpe einde)\n\n")
    eind()

#keuze6(spel keuze 5)
if keuze4 == "3":
    while True:
        typewrite("Je rent snel weg en je hebt de bewaker achter je horen roepen.\nWat ga je nu doen" + naam +"?\n")
        typewrite("1. Verstoppen in een kamer\n\n2. Naar de uitgang rennen\n\n3. verstoppen in een toilet\n\n4. Lijpe ritueel doen snel")
        keuze6 = input("> ")

        #keuze die leidt naar einde(IDKsterling)
        if keuze6 == "1":
            typewrite("Je verstopt je in een kamer en hoopt dat de bewaker je niet vindt\nen je kijkt achter je en je ziet IDKsterling\nen hij zegt dat hij een uitweg weet en je gaat hem dus volgen\n\n")
            addcoin(1)
            input("> Press ENTER to continue ")
            break
        
        #einde(Gedood)
        elif keuze6 == "2":
            typewrite("Je rent naar de uitgang, maar de bewakers zijn dicht achter je en ze hebben je helemaal doodgeschoten a sahbi.\n\n(Je bent gedood einde)")
            eind()
        
        #keuze die leidt naar einde(toilet)
        elif keuze6 == "3":
            typewrite("Je verstopt je un een toilet en je legt een dikke beuker\ndoor die pittige sucuk die je vanmiddag at\nen na je boodschap zie je dat er een kleine raampje zit boven de toilet.\nDe bewaker is er inmiddels al voor trapt op de deur,\ndus je veegt af en je klimt door de raam")
            addcoin(1)
            input("> Press ENTER to continue ")
            break
        
        #einde(ritueel)
        elif keuze6 == "4":
            typewrite("Je doet een lijpe ritueel en je roept John'Chigga'Pork op van zijn dood en hij vermoord iedereen en neemt je mee naar buiten en je bent ontsnapt.\n\n(Ritueel einde)")
            eind()
            
        #ongeldige keuze(opnieuw kiezen van dit sectie)
        else:
            typewrite("> Ongeldige keuze\n")
            continue

#einde(IDKsterling)
if keuze6 == "1":
    typewrite("Je ziet dat Sterling al een gat heeft gegraven\ndie leidt naar de riool en je volgt hem dus.\nJe ontsnapt uiteindelijk uit de gevangenis.\n\n(Onstnapt met IDKsterling einde)\n\n")
    eind()

#einde(toilet)    
if keuze6 == "3":
    typewrite("Je hebt maar weinig tijd" + naam +". De bewaker probeert die deur open te trappen. klim nu uit het raam")
    addcoin(1)
    input("Press ENTER to 'klim uit het raam'")
    typewrite("Je bent door de raam geklommen en je rent weg en je bent ontsnapt.\n\n(Toiletraam ontsnapping einde)\n\n")
    eind()