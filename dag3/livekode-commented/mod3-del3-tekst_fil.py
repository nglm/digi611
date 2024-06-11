# In[1]: ----------------------------------------


# Åpne en fil og tilordne filen til variabelen "f"
with open("Askeladden_og_de_gode_hjelperne.txt", mode="rt") as f:
    # Les alle linjene og lagre dem i en liste
    linjene = f.read().split("\n")
    print(f)

# Nå er filen lukket, vi kan ikke lenger bruke "f", men "linjene" er
# fortsatt definert
print(linjene[0])

# Teller hvor mange linjer i teksten
print(f"Teksten har {len(linjene)} linjer.")

# Teller hvor mange tegner i teksten
n_tegn = 0
for linje in linjene:
    n_tegn = n_tegn + len(linje)
print(f"Teksten har {n_tegn} tegner.")


# In[2]: ----------------------------------------


# /!\ Det utløser en feilmelding /!\
# utenfor "with"-konteksten er filen lukket!
f.read().split("\n")


# In[3]: ----------------------------------------


# Skrive ut innholdet i en tekstfil (5 første linjer)
for linje in linjene[:5]:
    print(linje)


# In[4]: ----------------------------------------


# Skrive alt med store bokstaver
# Skrive ut innholdet i en tekstfil (5 første linjer)
for i_linje in range(5):
    linjene[i_linje] = linjene[i_linje].upper()
    print(linjene[i_linje])


# In[5]: ----------------------------------------


with open("store_bokstaver.txt", mode="wt") as f:
    # Skriv alle linjene i filen "store_bokstaver.txt"
    f.writelines(linjene)


# In[6]: ----------------------------------------


navn = input("Hva er navnet ditt?")
adressen = input("Hva er adressen din?")

with open("adresser.txt", mode="at") as f:
    print(f"Du heter {navn} og adressen din er: {adressen}")
    # Skriv navnet og adressen i filen"
    f.writelines(f"Navn:     {navn.upper()}\n")
    f.writelines(f"Adressen: {adressen.upper()}\n")
    # Skriv et skilletegn i filen mellom navn-adresse par
    f.writelines("_"*60 + "\n")


# In[7]: ----------------------------------------


# Filen åpnes i "read"-modus (r) og den forventes å være en tekstfil (t)
with open("adresser.txt", mode="rt") as f:
    linjene = f.read().split("\n")

for i_linje in range(len(linjene)):
    # Finn indeksen til alle linjene som inneholder "BERGEN"
    if "BERGEN" in linjene[i_linje]:
        # Skriv ut navnet
        print(linjene[i_linje-1])
        # Og adressen
        print(linjene[i_linje])

