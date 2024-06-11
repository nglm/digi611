# In[1]: ----------------------------------------


min_streng = "Hallo, verden!"
min_liste = [2024, 0.1, "DIGI", True, None]
print(f"{min_liste = }")
print(f"{min_streng = }")

print("Iterere over en streng:")
for bokstav in min_streng:
    # Vi har tilgang til bokstavene i strengen
    print(bokstav)

print("Iterere over en liste:")
for element in min_liste:
    # Vi har tilgang til elementene i listen
    print(element)


# In[2]: ----------------------------------------


def iterere_gjennom_sekvens(sekvens):
    # Denne koden fungerer med strenger og lister!
    for element in sekvens:
        print(f"{element}")

print("Iterere over en streng:")
iterere_gjennom_sekvens(min_streng)
print("Iterere over en liste:")
iterere_gjennom_sekvens(min_liste)


# In[3]: ----------------------------------------


print("Med range(5)")
# Syntaksen: range(slutt)
# (sluttverdien er ikke inkludert, sekvensen stopper rett før)
for x in range(5):
    print(x)

print("Med range(3, 6)")
# Syntaksen: range(start, slutt)
for x in range(3, 6):
    print(x)

print("Med range(10,20,2)")
# Syntaksen: range(start, slutt, steg)
for x in range(10,20,2):
    print(x)


# In[4]: ----------------------------------------


min_streng = "Hallo, verden!"
min_liste = [2024, 0.1, "DIGI", True, None]
print(f"{min_liste = }")
print(f"{min_streng = }")

def iterere_gjennom_sekvens_range(sekvens):
    # Hvor lang er sekvensen? Bruk "len()" funksjon
    lengde = len(sekvens)
    # Denne koden fungerer med strenger og lister!
    for i in range(lengde):
        print(f"Indeks {i} : {sekvens[i]}")

iterere_gjennom_sekvens_range(min_streng)
iterere_gjennom_sekvens_range(min_liste)


# In[5]: ----------------------------------------


karakterene = [12, 8, 15, 6, 10, 12, 3, 0, 19, 36]

# -------- 1. Beregne den totale summen -----------

# 1.3: Initialisere variabelen som skal
# - hjelpe oss å huske summen så langt i for-løkken
# - gi oss den totale summen etter løkken
total_sum = 0
# 1.1:  Iterere
for karakter in karakterene:
    # 1.2 Legge til
    total_sum = total_sum + karakter

# ---- 2. Dele summen på antallet karakterer -------

# 2.1 Beregne antallet karakterer
lengde = len(karakterene)
# 2.2 Beregne antallet karakterer
gjennomsnittet = total_sum / lengde

print(gjennomsnittet)


# In[6]: ----------------------------------------


min_streng = "Hallo, verden!"
min_liste = [2024, 0.1, "DIGI", True, None]
print(f"{min_liste = }")
print(f"{min_streng = }")

def iterere_gjennom_sekvens_while(sekvens):
    # Hvor lang er sekvensen
    lengde = len(sekvens)

    # Initialiser indeksvariabel for å *huske* hvor vi er i sekvensen
    i_element = 0

    while i_element < lengde:
        print(f"Indeks {i_element} : {sekvens[i_element]}")

        # Oppdater indeksvariabelen
        i_element = i_element + 1

iterere_gjennom_sekvens_while(min_streng)
iterere_gjennom_sekvens_while(min_liste)

