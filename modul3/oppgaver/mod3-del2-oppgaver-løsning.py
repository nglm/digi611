"""
1. Legg til en nøkkel-verdi par der nøkkelen er "hovedstad" og nøkkelen "Oslo"
2. Oppdater den "land"-"Norge" par slik at det blir en "land"-"Norway" par.
"""

# %% -------------------------------------------------------------------

norge = {
    "land": "Norge",
    "befolkning" : 5500000,
    "språk" : ["bokmål", "nynorsk", "samisk"],
    "areal" : 300000
}

norge["hovedstad"] = "Oslo"
norge["land"] = "Norway"

# %% -------------------------------------------------------------------

"""
Hovedmål:
Skriv ut nøklene til en ordbok én etter én, sammen med typen til deres tilsvarende verdi. Bruk en for løkke og den ordbok metoden "item"

Utskrift eksempel:

Nøkkelen: land. Typen til verdien: <class 'str'>
Nøkkelen: befolkning. Typen til verdien: <class 'int'>
Nøkkelen: språk. Typen til verdien: <class 'list'>
Nøkkelen: areal. Typen til verdien: <class 'int'>

Detaljert instruksjoner:
1. Bruk en for løkke (husk å bruke ordbok metoden "items()" for å få tak
i nøkkelen og verdien)
2. I løkken: bruk print() og type() funksjoner
"""

# %% -------------------------------------------------------------------

norge = {
    "land": "Norge",
    "befolkning" : 5500000,
    "språk" : ["bokmål", "nynorsk", "samisk"],
    "areal" : 300000
}

for nøkkel, verdi in norge.items():
    print(f"Nøkkelen: {nøkkel}. Typen til verdien: {type(verdi)}")

# %% -------------------------------------------------------------------
"""
Oppgave: Beregn unionen av disse to listene over allergier (sørg for
at det er ingen duplikater i resultatet) og resultatet må være en liste.
- Sett typen og konvertering med list() eller set() kan være nyttige.
- Det kan være nyttig å slå sammen 2 lister med sekvens operasjonen "+"
- Det ka nvære nyttig å beregne unionen av to sett med sett metoden "union"
  (Se https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
"""

mat_restriksjoner_1 = [
    "egg", "nøtter", "kjøtt", "svinn", "fisk",
    "laktose", "fisk", "laktose", "kjøtt", "svinn", "egg",
    "nøtter", "svinn", "svinn", "egg",
    "laktose", "fisk", "egg", "egg", "svinn",
    "fisk", "nøtter", "nøtter", "fisk", "laktose",
    "nøtter", "kjøtt",
    "kjøtt",
]


mat_restriksjoner_2 = [
    "egg", "nøtter", "kjøtt", "fisk", "gluten", "kjøtt",
    "gluten", "fisk", "melk", "gluten", "kjøtt",
    "nøtter", "melk", "egg", "fisk", "melk", "gluten",
    "melk", "fisk", "melk", "egg", "egg", "melk", "gluten", "kjøtt",
    "fisk", "nøtter", "nøtter", "melk", "fisk", "melk",
    "nøtter", "gluten", "gluten", "kjøtt", "gluten", "kjøtt",
]

# Alternativ 1
mengde = set(mat_restriksjoner_1 + mat_restriksjoner_2)
liste = list(mengde)
print(liste)

# Alternativ 2
mengde_1 = set(mat_restriksjoner_1)
mengde_2 = set(mat_restriksjoner_2)
mengde = mengde_1.union(mengde_2)
liste = list(mengde)
print(liste)
