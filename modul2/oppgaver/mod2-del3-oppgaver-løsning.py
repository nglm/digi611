# %% ------------------------------------------------------------------
"""
Hovedmål: Opprett en ordnet liste av tall, mellom to tall (for eks. 50 og 100)
e.g [50, 51, 52, ..., 98, 99, 100]

Mer detaljert instruksjoner:
1. Opprett en tom liste
2. Bruk en for-løkke med range() for å iterere over tallene mellom 50 og 100
3. I for-løkken: bruk den på stedet foranderlig sekvens metoden "append()" for å
legg til den nåværende tallet på slutten av listen
4. Etter løkken: skriv ut listen
"""

# Vi begynner fra en tom liste
l = []

# Vi legger til tallene på slutten av listen en etter en.
# Husk at det siste tallet ikke er inkludert i "range"
for tall in range(50, 101):
    # Vi bruker den foranderlige sekvens (på stedet) metoden "append"
    l.append(tall)
print(l)

# %% ------------------------------------------------------------------
"""
Hovedmål: Be brukeren om å gi oss en karakter så lenge de ikke skriver -1.

Mer detaljert instruksjoner:
1. Opprett en tom liste
2. Opprett en variabel "karakter" som er et vilkårlig tall gitt at det
ikke er -1 (kan være f.eks. 0)
3. Bruk en while-løkke som fortsetter så lenge karakter != -1
4. I while-løkken: Skriv ut listen
5. I while-løkken: Be brukeren om å gi oss en karakter som blir lagret
i "karakter" variabelen (bruk input() og int() funksjoner)
6. I while-løkken: Bruk den på stedet foranderlig sekvens metoden "append()" for
å legg til den nåværende karakteren på slutten av listen
7. (Valgfri) Fjern -1 fra slutten av listen (bruk de på stedet foranderlig
sekvens metoder pop() eller remove())
8. (Valgfri) Etter løkken: Skriv ut listen
"""

# Vi begynner fra en tom liste
l = []
# Vi begynner med et vilkårlig tall som ikke er -1
karakter = 0

# Vi fortsetter så lenge karakter != -1
while karakter != -1:
    print(f"Karakterene så langt: {l}")
    karakter = int(input("Skriv en ny karakter. "))
    l.append(karakter)

l.pop()
print(l)
