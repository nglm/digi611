# In[1]: ----------------------------------------


print("32 > 18:  ", 32 > 18)

alder = 32

# Opprett en boolsk variabel
voksen = alder >= 18
print(f"variabelen voksen,  verdien: {voksen},  type: {type(voksen)}")


# In[2]: ----------------------------------------


alder = 32

if alder >= 18:
    # Kodeblokken her kjøres hvis betingelsen er usann
    print("Du er en voksen")

print("Utenfor if-kodeblokken: alltid kjøres")


# In[3]: ----------------------------------------


alder = 16

if alder >= 18:
    # Kodeblokken her kjøres hvis betingelsen er usann
    print("Du er en voksen")
else:
    # Kodeblokken her kjøres hvis betingelsen var usann
    print("Du er et barn")
print("Utenfor kodeblokkene")


# In[4]: ----------------------------------------


alder = 16

# En if-elif struktur
if alder >= 18:
    print("Du er en voksen")
elif alder > 12:
    print("Du er en tenåring")


# In[5]: ----------------------------------------


alder = 4

# En if-elif-else struktur
if alder >= 18:
    print("Du er en voksen")
elif alder > 12:
    print("Du er en tenåring")
else:
    print("Du er et barn")


# In[6]: ----------------------------------------


alder = 4

#  En if-elif-elif-else struktur
if alder >= 18:
    print("Du er en voksen")
elif alder > 12:
    print("Du er en tenåring")
elif alder < 5:
    print("Du er et småbarn")
else:
    print("Du er et barn")


# In[7]: ----------------------------------------


alder = 16

if alder >= 18:
    print("Du er en voksen")
elif alder > 5:
    print("Du er et barn")
    # Kodeblokken her aldri kjøres fordi:
    # hvis denne elif-betingelsen er sann, så var den elif betingelsen før!
elif alder > 12:
    print("Du er en tenåring")
else:
    print("Du er et småbarn")


# In[8]: ----------------------------------------


# Opprett variabelen før løkken
tall = 1000

# Fortsett å dele på 2 så lenge tallet er større enn 1
while tall > 1:

    # Oppdater variabelen knyttet til betingelsen
    # Del på 2
    tall = tall / 2
    print(tall)


# In[9]: ----------------------------------------


# Opprett variabelen før løkken
tekst = "Hei"
# Fortsett å be brukeren om å gi oss en streng så lenge de ikke skriver "Ha det"
while tekst != "Ha det":

    print(tekst)

    # Oppdater variabelen knyttet til betingelsen
    # Be brukeren om å skrive noe
    tekst = input("Skriv hva som helst. Skriv 'Ha det' for å slutte programmet")

