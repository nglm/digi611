# %% ------------------------------------------------------------------
"""
1. Spør brukeren om navnet deres (input() funksjonen)
2. Beregn hvor mange bokstaver det er i navnet deres (len() sekvens funksjonen)
3. Skriv ut hvor mange bokstaver det er i navnet deres (print() funksjonen)
4. Hent ut den første bokstaven i navnet deres (bruk sekvens indeksering)
5. Skriv ut den første bokstaven i navnet deres (print() funksjonen)
6. Sjekk om det forekommer bokstaven "a" i navnet deres (bruk "in" sekvens operator)
7. Skriv ut om det forekommer bokstaven "a" i navnet deres (print() funksjonen)
"""

# 1 --
navn = input("Hva heter du? ")
# 2 --
n_bokstav = len(navn)
# 3 --
print(f"Det er {n_bokstav} bokstaver i navnet ditt")
# 4 --
først_bokstav = navn[0]
# 5 --
print(f"Den første bokstaven er {først_bokstav}")
# 6 --
svar = "a" in navn
# 7 --
print(f"Er 'a' i navnet ditt? {svar}")

# %% -------------------------------------------------------------------
"""
1. Skriv ut hvor mange elementer det er i listen (len() og print() funksjoner)
2. Skriv ut den første karakteren i listen (indeksering og print())
3. Skriv ut om det forekommer karakteren 0 i listen ("in" operator og print())
4. Spør brukeren om å angi en ny karakter (input())
5. Legg til karakteren på slutten av listen (bruk den på stedet foranderlig
sekvens metoden "append()")
6. Skriv ut listen (print())
"""

karakterer = [3, 4, 5, 6, 8, 12, 10]

# 1 --
n_karakterer = len(karakterer)
print(f"Det er {n_karakterer} karakterer i listen")

# 2 --
print(f"Den første karakteren er {karakterer[0]}")
# 3 --
print(f"Fikk du karakteren 0? {0 in karakterer}")
# 4 --
ny_karakter = int(input("Gi en ny karakter" ))
# 5 --
karakterer.append(ny_karakter)
# 6 --
print(karakterer)


