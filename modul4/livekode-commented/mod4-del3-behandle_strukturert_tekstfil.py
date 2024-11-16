# In[1]: ----------------------------------------


# Importer biblioteket vi trenger
import matplotlib.pyplot as plt


# In[2]: ----------------------------------------


# Lese filen som en vanlig tekst fil
with open("allergier.txt", mode="rt") as f:
    linjer  = f.read().split("\n")

# Se den første linjen
print(linjer[0])
# Del linjen mellom det som står før ":" og det som står etter
print(linjer[0].split(":"))


# In[3]: ----------------------------------------


# Se en annen linje, som har flere allergier
print("Hele linje:", linjer[6])

# Del linjen mellom det som står før ":" og det som står etter
delt_linje = linjer[6].split(":")
# Navnet er det første elementet
navn = delt_linje[0]
# Og allergiene (som en lang streng) er det andre elementet
streng_allergier = delt_linje[1]
# Del strengen igjen, inn i en liste av strenger, der hvert element
# tilsvarer én allergi.
liste_allergier = streng_allergier.split(", ")

print(f"Navn: {navn}. Allergier: {liste_allergier}")


# In[4]: ----------------------------------------


# Initialiser en tom ordbok
navn_og_allergier = {}

for linje in linjer:
    # Del hver linje ved ":" for å separere navnet fra allergiene.
    delt_linje = linje.split(":")

    # Navnet er det første elementet og allergiene det andre
    navn = delt_linje[0]
    streng_allergier = delt_linje[1]

    # Del strengen igjen, inn i en liste av strenger, der hvert element
    # tilsvarer én allergi.
    liste_allergier = streng_allergier.split(", ")

    # Legge til en navn-allergi par i ordboka med navnet som nøkkel og
    # liste av allergier som verdi
    navn_og_allergier[navn] = liste_allergier

print(navn_og_allergier)


# In[5]: ----------------------------------------


# Initialiser en tom liste
alle_allergiene = []

for linje in linjer:
    # Del hver linje ved ":" for å separere navnet fra allergiene.
    delt_linje = linje.split(":")

    # Navnet er det første elementet og allergiene det andre
    streng_allergier = delt_linje[1]

    # Liste av allergier for denne personen
    liste_allergier = streng_allergier.split(", ")

    # Slå sammen de allergiene så langt med den nåværende liste av allergier
    # Vi bruker den sekvens operasjonen "+"
    alle_allergiene = alle_allergiene + liste_allergier


# In[6]: ----------------------------------------


def restriksjon_teller(restriksjoner):
    """
    Telle hvor mange personer har en gitt restriksjon.

    Returnere en ordbok som teller antallet personer med en gitt
    restriksjon for hver restriksjon i listen.
    """
    # Opprette en ordbok som kommer til å telle hvor mange personer
    # har en gitt restriksjon
    teller = {}

    # Hent ut hver mat restriksjon i listen over restriksjoner
    for mat in restriksjoner:
        # Hvis vi allerede har funnet denne restriksjonen, øker vi antallet
        if mat in teller:
            teller[mat] = teller[mat] + 1
        # Ellers, oppretter vi en ny nøkkel, og initialiserer verdien til 1
        else:
            teller[mat] = 1
    return teller

teller = restriksjon_teller(alle_allergiene)

print(teller)


# In[7]: ----------------------------------------


fig, ax = plt.subplots()

# Syntaksen: plt.bar(x-verdiene, y-verdiene)
ax.bar(x=list(teller.keys()), height=teller.values())
# Sett x-akse etikett
ax.set_xlabel("Mat")
# Sett y-akse etikett
ax.set_ylabel("Antall personer")
# Sett tittelen til figuren
ax.set_title("Mat restriksjoner")
# Lagre figuren
fig.savefig("mat_restriksjoner_figur")


# In[8]: ----------------------------------------


with open("karakterer.csv", mode="rt") as f:
    linjer  = f.read().split("\n")


# In[9]: ----------------------------------------


# Ta den første linjen
linje0 = linjer[0]
print(linje0)

# Del strengen inn i en liste av strenger
delt_linje0 = linje0.split(";")
print(delt_linje0)

# Hent ut alt bortsett fra det første elementet
liste_fag = linjer[0].split(";")[1:]
# Det gir oss listen av fag
print(liste_fag)


# In[10]: ----------------------------------------


# Opprett en tom liste av students navn
liste_navn = []

# Iterer over radene men fra den andre raden
for linje in linjer[1:]:

    # Del strengen inn i en liste av strenger
    delt_linje = linje.split(";")

    # Hent ut det første elementet
    navn = delt_linje[0]

    # Legg til navnet på slutten av listen
    liste_navn.append(navn)

print(liste_navn)


# In[11]: ----------------------------------------


student = "Jakob"

def finn_student_linje(linjer, navn):
    """
    Finn linjen i filen som tilsvarer studenten.

    Hvis studenten ikke er i filen, blir "" returnert.
    """
    student_linje = ""
    for linje in linjer:
        if navn in linje:
            student_linje = linje
    return student_linje

# Skriv linjen (+ linjen med fag) i en ny fil
with open(f"{student}_karakterer.csv", mode="wt") as f:
    # Den første linjen med fag er den samme som før
    f.writelines(linjer[0] + "\n")

    # Og vi bare skrive linjen som tilsvarer studenten
    student_linje = finn_student_linje(linjer, student)
    f.writelines(student_linje + "\n")


# In[12]: ----------------------------------------


# Listen av fag er den første raden, men uten den første kolonnen.
liste_fag = linjer[0].split(";")[1:]
liste_karakterer = student_linje.split(";")[1:]

# Hver karakter er en streng av en flyttall, ikke en flyttall!
# Vi må konvertere først!
for i in range(len(liste_karakterer)):
    liste_karakterer[i] = float(liste_karakterer[i])

# Nå kan vi gjenbruke vår kode som lager en figur
# (Vi trenger en større figur, så derfor bruker vi "figsize")
fig, ax = plt.subplots(figsize=(15, 5))
ax.bar(liste_fag, liste_karakterer)
ax.set_xlabel("Fag")
ax.set_ylabel("Karakter")
ax.set_title(f"{student} karakterer")
fig.savefig(f"{student}_karakterer")

