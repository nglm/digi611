# %% -------------------------------------------------------------------
# Åpne en fil og tilordne filen til variabelen "f"
with open("Askeladden_og_de_gode_hjelperne.txt", mode="rt") as f:
    # Les alle linjene og lagre dem i en liste
    linjene = f.read().split("\n")

# Skriv ut antall linjer i teksten
print(len(linjene))

# Skriv ut linjer son inneholder "Askeladden"
for linje in linjene:
    if "Askeladden" in linje:
        print(linje)

        # Skriv linjen men navnet mitt
        ny_linje = linje.replace("Askeladden", "Odin")
        print(ny_linje)
