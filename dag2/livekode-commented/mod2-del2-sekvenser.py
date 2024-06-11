# In[1]: ----------------------------------------


# En tom liste
tom_liste = []
# En liste med forskjellige typer
min_liste = [2024, 0.1, True, None, "DIGI"]
print(min_liste)

print("Typen til en liste er: ", {type(min_liste)})


# In[2]: ----------------------------------------


min_liste = [2024, 0.1, True, None, "DIGI"]

lengden = len(min_liste)
print(f"Listen har {lengden} elementer")

# Indeksering begynner med indeks 0, ikke 1
print(f"Det første elementet i listen min er: {min_liste[0]}")
# Det er femte (siste) elementet
print(f"Det siste elementet i listen min er:  {min_liste[lengden-1]}")
# /!\ Det utløser en feilmelding /!\: Det er ingen element ved indeks 5
print(f"Det er ingen element ved indeks 5:    {min_liste[lengden]}")


# In[3]: ----------------------------------------


min_liste = [2024, 0.1, "DIGI", True, None]
min_streng = "Hei hei, verden!"

# Syntaksen f"{uttrykk = }" skiver både uttrykket og evalueringen (resultatet)
# av uttrykket
print(f"{min_liste = }")
print(f"{min_streng = }")

# Vi kan endre verdiene i listen
min_liste[1] = "ny_verdi"
print(min_liste)
# Men vi kan ikke endre verdiene i streng
# /!\ Det utløser en feilmelding /!\: en streng er uforanderlig
min_streng[1] = "e"
print(min_streng)


# In[4]: ----------------------------------------


min_liste = [2024, 0.1, "DIGI", True, None]
min_streng = "Hei hei, verden!"
print(f"{min_liste = }")
print(f"{min_streng = }")

print("\n --- Lengden på sekvensen ---")
# "len()": hvor mange elementer finnes det i en sekvens
print(f"{len(min_liste) = }")
print(f"{len(min_streng) = }")

print("\n --- Konkatenering av sekvenser --- ")
# " + ": konkatenering av 2 sekvenser
l = min_liste + ["Hei", 0]
print(f'min_liste + ["Hei", 0]: {l}')
s = min_streng + ":)"
print(f'min_streng + ":)": {s}')

print("\n --- Sjekk om noe er i sekvensen --- ")
# " in ": Sjekk om noe er i sekvensen
print(f"{None in min_liste = }")
print(f"{'h' in min_streng = }")   # 'H' er i strengen men ikke 'h'!

print("\n --- Indeksering, segment --- ")
# Trekk ut flere elementer fra en sekvens
# Syntaksen: [start:]
print(f"{min_streng[5:] = }")
# Syntaksen: [start:slutt]
print(f"{min_liste[1:4] = }")
print(f"{min_streng[5:11] = }")
# Syntaksen: [start:slutt:steg]
print(f"{min_streng[1:11:2] = }")

# "index()": finn plassering til noe i sekvensen
print(f"{min_liste.index(True) = }")
# Merk at kun indeksen til den første 'e' returneres
print(f"{min_streng.index('e') = }")

print("\n --- min og max --- ")
print(f"{min([12, -2, 0.1]) = }")
print(f"{max(min_streng) = }")


# In[5]: ----------------------------------------


# /!\ Det utløser en feilmelding /!\:
# Hvis elementet ikke er i listen utløser index() en feil!
print(f"{min_streng.index('i') = }")

# /!\ Det utløser en feilmelding /!\:
# en streng konkateneres bare med en streng og en list bare med en list!
print(f"{[0, 'Hallo'] + 'verden'}")

# /!\ Det utløser en feilmelding /!\: kan ikke sammenligne streng og tall
print(f"{min(min_liste) = }")


# In[6]: ----------------------------------------


min_streng = "Hei hei, verden!"
vennene = ["Nora", "Odin", "Morten" ]
print(f"{min_streng = }")
print(f"{vennene = }")

print("\n --- Erstatte en understreng i strengen ---")
# "replace()": Erstatte alle 'e' med en 'i'
print(f"{min_streng.replace('e', 'i') = }")
# Ingenting skjer fordi bokstaven ikke var i strengen
print(f"{min_streng.replace('w', 'A') = }")
# Det fungerer også med sekvenser av tegn
print(f"{min_streng.replace('ver', 'klo') = }")

print("\n --- Erstatte en understreng i strengen ---")
# "split()": dele strengen inn i en liste med strenger
print(f"{min_streng.split(' ') = }")
print(f"{min_streng.split(',') = }")

print("\n --- Sjekke om strenger begynner/slutter med ---")
print(f"{min_streng.startswith('hei') = }")
print(f"{min_streng.endswith('!') = }")

print("\n --- Skrive med bare store/små bokstaver ---")
# "upper()": Skrive med bare store bokstaver
print(f"{min_streng.upper() = }")
# "lower()": Skrive med bare små bokstaver
print(f"{min_streng.lower() = }")
# Man kan kombinere flere metoder
print(f"{min_streng.lower().startswith('hei') = }")

print("\n --- Slår en list sammen til en streng ---")
# Slå sammen hvert element av vennene men en "og " innimellom
print(f"{' og '.join(vennene) = }")


# In[7]: ----------------------------------------


min_liste = [2024, '!', "DIGI", True, None]
print(f"{min_liste = }")

print("\n --- Legge til et element på slutten (på stedet) ---")
# Vær forsiktig! "append" metoden er en "på stedet metode (in-place method)"
# Det skriver ut None, det betyr at returverdien til "append" metoden er "None"
# Det er fordi det er en "på stedet metode" som ikke returner listen, men endrer
# listen direkte
print(f"{min_liste.append(42) = }")
# Det skriver ut listen med det nye elementet
print(f"{min_liste = }")

print("\n --- Legge til et element på en gitt indeks (på stedet) ---")
# Legg "42" på indeks 1 (dvs den andre posisjonen)
# Vær forsiktig! "insert" er også en "på stedet metode "
print(f"{min_liste.insert(1, 42) = }")
print(f"{min_liste = }")

print("\n --- Fjern et gitt element fra sekvensen (på stedet) ---")
# Merk at kun den første 42 ble fjernet!
# remove er også en "på stedet metode"
print(f"{min_liste.remove(42) = }")
print(f"{min_liste = }")

print("\n --- Fjern elementet som ligger på en gitt indeks (på stedet) ---")
# pop er en på stedet metode (fordi endringene skjer direkte på listen,
# men den returnerer fortsatt noe: elementet som ble fjernet)
print(f"{min_liste.pop(2) = }")
print(f"{min_liste = }")


# In[8]: ----------------------------------------


# /!\ Det utløser en feilmelding /!\:
# Hvis elementet ikke er i listen utløser index() en feil!
print(f"{min_liste.remove(100) = }")


# In[9]: ----------------------------------------


karakterene  = [1, 8, 3, 0, 10, 1]
vennene = ["Nora", "Odin", "Morten" ]
print(f"{karakterene = }")
print(f"{vennene = }")

print("\n --- Sortere en list (på stedet) ---")
print(f"{karakterene.sort() = }")
print(f"{karakterene = }")

# sort metoden har en parameter "reverse" som bestemmer hvorvidt
# listen må sorteres i økende rekkefølge eller motsatt vei.
print(f"{vennene.sort(reverse=True) = }")
print(f"{vennene = }")


# In[10]: ----------------------------------------


min_liste = [2024, 0.1, "DIGI", True, None]
print(f"{min_liste = }")

# /!\ Det utløser en feilmelding /!\:
# Kan ikke sammenligne str med list og med bool!
min_liste.sort()


# In[11]: ----------------------------------------


# Legg noe til på slutten av listen
pakkene = [1, 8, 3, 0, 10, 1]
print(pakkene)
siste_pakke = int(input("Hva er volumet til den neste pakken din?"))
pakkene.append(siste_pakke)
print("En pakke var lagt til på slutten", pakkene)

# Sett noe inn i listen på en gitt indeks
ny_pakke = int(input("Angi volumet som skall settes inn på tredjeplassen."))
# Husk at tredjeplassen tilsvarer indeksen 2
pakkene.insert(2, ny_pakke)
print("En pakke var settes inn på tredjeplassen", pakkene)

# Fjern et element fra listen
pakkene.remove(ny_pakke)
print("Pakken på tredjeplassen ble fjernet", pakkene)

# Sortere en liste
pakkene.sort(reverse=False)
print("Listen ble sortert", pakkene)

