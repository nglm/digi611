# In[1]: ----------------------------------------


def pris_hotell():
    pris_frokost = 149.90
    pris_rom = 1000
    print(f"\n***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n")

    n_personer = int(input("Hvor mange personer er dere?"))
    print(f"Dere er {n_personer} personer.")

    pris = pris_rom + n_personer*pris_frokost
    print(f"Da bør dere betale {pris}Kr.")


# In[2]: ----------------------------------------


print("Hallo!")

def pris_hotell():
    pris_frokost = 149.90
    pris_rom = 1000
    print(f"\n***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n")

    n_personer = int(input("Hvor mange personer er dere?"))
    print(f"Dere er {n_personer} personer.")

    pris = pris_rom + n_personer*pris_frokost
    print(f"Da bør dere betale {pris}Kr.")

# "Velkommen!" er skrevet ut før teksten i funksjonen!
print("Velkommen!")

# Husk å *kalle på* en funksjon for at koden kjøres:
pris_hotell()

print("Ha det!")


# In[3]: ----------------------------------------


def pris_hotell():
    pris_frokost = 149.90
    pris_rom = 1000
    print(f"\n***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n")

    n_personer = int(input("Hvor mange personer er dere?"))
    print(f"Dere er {n_personer} personer.")

    pris = pris_rom + n_personer*pris_frokost
    print(f"Da bør dere betale {pris}Kr.")

# Reise 1
pris_hotell()

# Reise 2
# Nå kan vi bruke kodeblokken en gang til ved å kalle på funksjon igjen!
pris_hotell()


# In[4]: ----------------------------------------


# Her legger vi to parametre til funksjonen
def pris_hotell(pris_frokost, pris_rom):

    print(f"\n***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n")
    n_personer = int(input("Hvor mange personer er dere?"))

    pris = pris_rom + n_personer*pris_frokost
    print(f"Da bør dere betale {pris}Kr.")

    # Og vi returnerer prisen
    return pris

# Pengene før vi reiser
pengene_mine = 5000


# /!\ Det utløser en feilmelding /!\:
# argumentet mangler! Vi må gi et argument for hver parameter
# i funksjonsdefinisjon
pris_hotell()
# /!\ Det utløser en feilmelding /!\:
# pris er ikke definert utenfor funksjonen!
print(f"Etter din første reise har du {pengene_mine - pris}")


# In[6]: ----------------------------------------


# Her legger vi en parameter til funksjonen
def pris_hotell(pris_frokost, pris_rom):

    print(f"\n***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n")
    n_personer = int(input("Hvor mange personer er dere?"))

    pris = pris_rom + n_personer*pris_frokost
    print(f"Da bør dere betale {pris}Kr.")

    # Og vi returnerer prisen
    return pris

pengene_mine = 5000

# Nå **må vi** gi to argumenter når vi kaller på funksjonen
# Og **kan vi** få tak i resultatet
# Reise 1
pris_reise1 = pris_hotell(149.9, 1000)
pengene_mine = pengene_mine - pris_reise1
print(f"Etter din første reise har du {pengene_mine}")

# Reise 2 (med rabatt på romprisen)
pris_reise2 = pris_hotell(149.9, 800)
pengene_mine = pengene_mine - pris_reise2
print(f"Etter din andre reise har du {pengene_mine}")

