# %% ------------------------------------------------------------------
"""
Oppgave: Erstatt "Odin" med "Vilma" i strengen.
Streng metoden "replace" kan være nyttig her.
"""

s = "Hei Odin! Hvordan går det med deg, Odin?"
# Vi bruker streng metoden "replace"
ny_streng = s.replace("Odin", "Vilma")

print(ny_streng)

# %% ------------------------------------------------------------------
"""
Oppgave: del strengen inn i en liste av strenger når et blankt
mellomrom blir funnet.
Kort sagt: hvert ord i strengen blir et element av listen.
f. eks. ["Jeg", "prøver", "å", ... "er", "ganske", "sent!"]
Streng metoden "split" kan være nyttig her.
"""

setning = "Jeg prøver å lære Python men det er kjempe vanskelig og jeg er svært trøtt fordi det allerede er ganske sent!"

# Vi bruker streng metoden "split"
list_av_strenger = setning.split(" ")

print(list_av_strenger)

# %% ------------------------------------------------------------------
"""
Oppgave: skriv ut alle elementene i en liste som er større enn eller lik 10
En for løkke og en if setning kan være nyttig her
"""

l = [2, 1, 36, 12, 4, 2, 4, -46, 59, 10, 0]

maks = 10
for tall in l:
    if tall >= maks:
        print(tall)

# %% ------------------------------------------------------------------
"""
Oppgave: Finn maksimum i en liste med kun positive tall
En for løkke og en if setning kan være nyttig her
"""

l = [2, 1, 36, 12, 4, 2, 4, 46, 59, 10, 0]

# Initialiser en maks verdi
maks = 0
# Iterer over tallene i listen
for tall in l:
    # Hvis tallet er større enn den nåværende maks, så blir det den nye maks
    if tall > maks:
        maks = tall

print(maks)