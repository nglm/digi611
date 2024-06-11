# %% --------------------------------------------------------------------------
"""
Oppgave: Skriv en funksjon som:
- tar som parameter en liste over alle matrestriksjonene til deltakerne på et
arrangement, og en streng som representeres en gitt allergi (som for eksempel "nøtter")
- og beregner og returnerer antall personer som har denne spesifikke
matrestriksjonen. Det vil si en funksjon som beregner antall
forekomster av denne restriksjonen i listen.

Hint:
- En for løkke og en if setning kan være nyttige her.
"""

# En list over matrestriksjoner fra deltakerregistreringen
mat_restriksjoner = [
    "egg", "nøtter", "kjøtt", "svinn", "fisk",
    "laktose", "gluten",  "fisk", "laktose", "gluten", "kjøtt",
    "nøtter", "melk", "svinn", "svinn", "egg",
    "laktose", "fisk", "melk", "egg", "egg", "melk", "svinn",
    "fisk", "nøtter", "nøtter", "melk", "fisk", "laktose",
    "nøtter", "gluten", "gluten", "kjøtt",
    "kjøtt"
]

restriksjon = "nøtter"

def allergi_teller(allergier, allergi):
    # Opprette en variabel som skal telle hvor mange personer
    # har allergien "allergi"
    teller = 0
    # Iterere over allergiene
    for mat in allergier:
        # Hvis den nåværende allergien er allergien vi er
        # interest i, så øker vi antallet
        if mat == allergi:
            teller = teller + 1
    return teller

print(allergi_teller(mat_restriksjoner, restriksjon))

# %% --------------------------------------------------------------------------
"""
Oppgave: Skriv en funksjon som tar som parameter en liste over alle matrestriksjonene til deltakerne på et arrangement og:

- for hver allergi beregner antallet personer som har denne
spesifikke allergien.
- returnerer en ordbok som inneholder antallet personer allergiske
for hver allergi.

Hint: Det finnes ulike måter å løse denne oppgaven på. En av dem
inkluderer å bruke (påkalle) vår tidligere funksjon fra
`mod4-del1-oppgaver-2-allergi.py`. En annen måte inkluderer å bruke en
if-setning med sekvensoperasjonen "in". I tillegg, i begge tilfeller
kan det være nyttig (men ikke obligatorisk) å bruke et sett
"""

# En list over matrestriksjoner fra deltakerregistreringen
mat_restriksjoner = [
    "egg", "nøtter", "kjøtt", "svinn", "fisk",
    "laktose", "gluten",  "fisk", "laktose", "gluten", "kjøtt",
    "nøtter", "melk", "svinn", "svinn", "egg",
    "laktose", "fisk", "melk", "egg", "egg", "melk", "svinn",
    "fisk", "nøtter", "nøtter", "melk", "fisk", "laktose",
    "nøtter", "gluten", "gluten", "kjøtt",
    "kjøtt"
]


# --------------- Løsning 1 (Uten å bruke oppgaven før) ---------------
def restriksjon_teller(restriksjoner):
    """
    Teller hvor mange personer har en gitt restriksjon, for hver restriksjon

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

# --------------- Løsning 2 (ved å bruke oppgaven før) ---------------
def restriksjon_teller(restriksjoner):
    """
    Teller hvor mange personer har en gitt restriksjon, for hver restriksjon

    Returnere en ordbok som teller antallet personer med en gitt
    restriksjon for hver restriksjon i listen.
    """
    # Opprette en ordbok som kommer til å telle hvor mange personer
    # har en gitt restriksjon
    teller = {}

    # Få mat uten duplikater
    unike_mat = set(restriksjoner)
    # Hent ut hver mat restriksjon i listen over restriksjoner
    for mat in unike_mat:
        teller[mat] = allergi_teller(restriksjoner, mat)
    return teller

teller = restriksjon_teller(mat_restriksjoner)

print(teller)