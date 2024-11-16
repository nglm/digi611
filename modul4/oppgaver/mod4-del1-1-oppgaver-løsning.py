# %% --------------------------------------------------------------------------

"""
Oppgave: Opprett en ordnet liste av tall, mellom to tall (for eks. 50 og 100)
det vil si: [50, 51, 52, ..., 98, 99, 100]
Hint:
- En for løkke med range kan være nyttig her
- Den foranderlige sekvens (på stedet) metoden "append" kan være nyttig her.
"""

# Opprett en tom liste
liste = []

# Iterere over de to ønskede tallene med en for løkke med range
# (Husk at det siste tallet ikke er inkludert! Dersom skriver vi "101")
for tall in range(50, 101):
    # Legg til tall ved slutten av listen vår med den på-stedet metoden "append"
    # Husk at siden det er en "på-stedet" metoden, skjer endringene direkte på
    # variabelen den påkalles fra, og ikke på en returverdi.
    liste.append(tall)

print(liste)


# %% --------------------------------------------------------------------------

"""
Vi antar at vi har en students karakterer lagret i en ordbok. Denne ordboken består da av fag-karakterer par.

Oppgave 1: Skriv en funksjon som beregner gjennomsnittskarakteren til en student.
Hint: Vi har allerede løst en oppgave som beregner dette når karakterene var lagret i en liste. Vi må nå tilpasse denne løsningen til en ordbok.

Oppgave 2: Skriv en annen funksjon som returnerer faget der studenten har den beste karakteren. Det vil si at vi må finne den beste karakteren, og det tilhørende faget.
Hint: Vi har allerede løst en oppgave som finner maksimum i en liste med kun positive tall. Vi må nå tilpasse denne løsningen til en ordbok, og i tillegg må vi lagre faget som samsvarer med den beste karakteren.
"""

ordbok_karakterer = {
    "Matematikk" : 12,
    "Historie": 15,
    "Kemi": 19,
    "Informatikk": 16,
    "Litteratur": 8,
}

def gjennomsnitt_karakter(karakterer):
    # Opprette en variabel som skal beregne total summen, en karakter etter
    # den andre
    summen = 0
    # Vi itererer over fag og karakterer
    # Merk at vi bruker ikke variabelen "fag" her
    for fag, karakter in karakterer.items():
        # Vi oppdaterer summen
        summen = summen + karakter
    # Beregn gjennomsnittet
    gjennomsnitt = summen / len(karakterer)
    return gjennomsnitt

gjennomsnitt = gjennomsnitt_karakter(ordbok_karakterer)

print(gjennomsnitt)

def best_fag(karakterer):
    # Opprette en variabel som skal huske den nåværende beste karakteren
    best_k = 0
    # Opprette en variabel som skal huske det nåværende beste faget
    best_f = ""
    # Vi itererer over fag og karakterer
    for fag, karakter in karakterer.items():
        # Hvis karakteren er bedre enn den beste karakteren vi har sett
        # så langt, da bør vi oppdatere den den beste karakteren og faget
        if karakter > best_k:
            best_k = karakter
            best_f = fag
    return best_f

fag = best_fag(ordbok_karakterer)

print(fag)
