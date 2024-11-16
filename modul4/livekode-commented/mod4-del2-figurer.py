# In[1]: ----------------------------------------


# Importer biblioteket vi trenger
import matplotlib.pyplot as plt


# In[2]: ----------------------------------------


# En list over matrestriksjoner fra deltakerregistreringen
mat_restriksjoner = [
    "egg", "nøtter", "kjøtt", "svinn", "fisk",
    "laktose",  "fisk", "laktose", "kjøtt", "laktose", "kjøtt",
    "nøtter", "melk", "svinn", "egg", "nøtter", "kjøtt", "laktose",
    "fisk", "kjøtt", "laktose", "melk", "egg", "egg", "melk", "svinn",
    "fisk", "nøtter", "nøtter", "melk", "fisk", "laktose",
    "nøtter", "laktose", "laktose", "gluten", "gluten", "kjøtt",
    "kjøtt", "laktose"
]

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

teller = restriksjon_teller(mat_restriksjoner)

print(teller)


# In[3]: ----------------------------------------


# Opprett en tom figur som inneholder en tom akse
fig, ax = plt.subplots()

# Syntaksen: ax.bar(x-verdiene, y-verdiene)
ax.bar(teller.keys(), teller.values())
# plt.show() vise plottet som vi har laget
# plt.show() stopper programmet opp og venter på at vinduet med plottet skal
# lukkes før det fortsetter å kjøre resten av koden.
plt.show()


# In[4]: ----------------------------------------


# ------------ Bruk dataene våre til å lage en figur -------------------
# Opprett en tom figur som inneholder en tom akse
fig, ax = plt.subplots()

# Syntaksen: ax.bar(x-verdiene, y-verdiene)
ax.bar(teller.keys(), teller.values())

# ------------------ Legg til tekst til figuren ------------------------
# Sett x-akse etikett
ax.set_xlabel("Mat")
# Sett y-akse etikett
ax.set_ylabel("Antall personer")
# Sett tittelen til figuren
ax.set_title("Mat restriksjoner")

# ----------------------  Lagr figuren ---------------------------------
fig.savefig("mat_restriksjoner_figur")


# In[5]: ----------------------------------------


# -------------------------- Data --------------------------------------
fag = ["Matematikk", "Historie", "Kemi", "Informatikk", "Litteratur"]
karakterer = [12, 15, 19, 16, 8]

# ------------ Bruk dataene våre til å lage en figur -------------------
fig, ax = plt.subplots()
ax.bar(x=fag, height=karakterer)

# ------------------ Legg til tekst til figuren ------------------------
ax.set_xlabel("Fag")
ax.set_ylabel("Karakter")
ax.set_title("Odins karakterer")

# ----------------------  Lagr figuren ---------------------------------
fig.savefig("Odins_karakterer")


# In[6]: ----------------------------------------


# -------------------------- Data --------------------------------------
karakterer_kemi = [12, 15, 19, 16, 8]
karakterer_info = [9, 12, 18, 20, 19.5]
# Initierer en liste med [2015, 2016, 2017, 2018, 2019]
år = []
for året in range(2015,2020):
    år.append(året)

# ------------ Bruk dataene våre til å lage en figur -------------------
# Opprett en tom figur med som inneholder en tom akse
fig, ax = plt.subplots()

# Syntaksen: ax.plot(x-verdiene, y-verdiene)
ax.plot(år, karakterer_kemi, label="kemi")
# Vi kan legge til flere linjer i et gitt diagrammet
# Syntaksen: ax.plot(x-verdiene, y-verdiene, label="marken")
ax.plot(år, karakterer_info, label="info")

# ------------------ Legg til tekst til figuren ------------------------
ax.set_xlabel("År")
ax.set_ylabel("Karakter")
# For å vise bare 5 ticks som tilsvarer årene
ax.set_xticks(år)
ax.set_ylim(0, 20.5)
# Nå at vi her flere linjer og et merket for hver linje, bør vi
# legge til en figurtekst med markene.
ax.legend()
ax.set_title("Utviklingen av Odins karakterer")

# ----------------------  Lagr figuren ---------------------------------
fig.savefig("Utviklingen_Odins_karakterer")


# In[7]: ----------------------------------------


# -------------------------- Data --------------------------------------
# Lengde og vekt av babyer
gutt_lengde = [
    47.3, 49.4, 48.0, 50.7, 51.1, 50.5, 51.1, 49.3, 47.8, 49.0, 49.4,
    50.0, 47.9, 49.0, 49.0, 49.4, 47.6, 49.2, 48.5, 49.0
]
gutt_vekt = [
    3.06, 3.19, 3.1, 3.31, 3.28, 3.26, 3.3, 3.21, 3.08, 3.17, 3.18, 3.25,
    3.08, 3.14, 3.16, 3.19, 3.08, 3.17, 3.12, 3.15
]

jente_lengde = [
    49.2, 47.8, 48.7, 47.1, 47.5, 48.5, 47.0, 47.8, 47.7, 46.9, 47.5, 47.3, 47.9, 48.0, 47.7, 49.5, 48.2, 46.3, 47.5, 47.5
]
jente_vekt = [
    3.21, 3.12, 3.12, 3.04, 3.1, 3.09, 3.04, 3.07, 3.08, 2.99, 3.05, 3.1, 3.1, 3.1, 3.09, 3.18, 3.09, 3.02, 3.06, 3.06
]

# ------------ Bruk dataene våre til å lage en figur -------------------
fig, ax = plt.subplots()
ax.scatter(gutt_lengde, gutt_vekt, label="gutt")
ax.scatter(jente_lengde, jente_vekt, label="jente")

# ------------------ Legg til tekst til figuren ------------------------
ax.set_xlabel("Lengde")
ax.set_ylabel("Vekt")
ax.legend()
ax.set_title("Vekt og lengde ved fødsel")

# ----------------------  Lagr figuren ---------------------------------
fig.savefig("vekt_lengde_fødsel")

