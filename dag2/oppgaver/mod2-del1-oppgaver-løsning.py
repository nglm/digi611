# %% -------------------------------------------------------------------

alder = int(input("Hvor gammel er du?" ))

if alder >= 18:
    print("Du er en voksen")
else:
    print("Du er ikke en voksen")


# %% -------------------------------------------------------------------

# Alternativ 1: med "and" operator
def butikk_1(klokken):

    # Opprett en boolsk variabel med "and" som sjekker hvorvidt butikken er åpen
    åpen = (klokken >= 8) and (klokken <= 18)

    # Skriv ut Åpen eller Stengt
    if åpen:
        print("Åpent")
    else:
        print("Stengt")

    # Returner boolsk variabel
    return åpen

# Alternativ 2: med 2 nøstede if setninger og print setning ved slutten
def butikk_2(klokken):

    # Er det for tidlig?
    if klokken < 8:
        åpen = False
    # Det er ikke for tidlig
    else:
        # Er det for sent?
        if klokken > 18:
            åpen = False
        # Det er ikke for sent
        else:
            åpen = True

    # Skriv ut Åpen eller Stengt
    if åpen:
        print("Åpent")
    else:
        print("Stengt")
    return åpen

# Alternativ 3: med 2 nøstede "if" setninger og "print" inni den nøstede "if"
def butikk_3(klokken):
    if klokken < 8:
        åpen = False
        print("Stengt")
    else:
        if klokken > 18:
            åpen = False
            print("Stengt")
        else:
            åpen = True
            print("Åpent")
    return åpen

kl = int(input("Hva er klokka?" ))

butikk_1(kl)
butikk_2(kl)
butikk_3(kl)