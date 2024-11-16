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

