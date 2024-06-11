# In[1]: ----------------------------------------


# Her skriver vi ut 2 strenger og det vil være ett mellomrom mellom dem
print("Hallo Verden!", "Jeg lærer Python!")
# Hvis vi kaller på funksjonen igjen, blir det et linjeskift mellom
# den første og den andre
print("Jeg er 32 år gammel.")


# In[2]: ----------------------------------------


# opprett variabler som innholder tekst
melding1 = "Hallo Verden! Jeg lærer Python!"
melding2 = "Jeg er 32 år gammel."
# Skriv ut variablene
print(melding1, melding2)


# In[3]: ----------------------------------------


navn = "Odin"
alder = 32

# med f-strenger kan vi plassere variabelverdier inne i strengen
melding1 = f"Hallo {navn}! Jeg lærer Python!"
melding2 = f"Jeg er {alder} år gammel."
print(melding1, melding2, f"Hvor gammel er du, {navn}?")


# In[4]: ----------------------------------------


navn = "Odin"
alder = 32

# Brukeren må gi oss et navn når de kjører koden
navn = input("Hva heter du? ")
melding1 = f"Hallo {navn}! Jeg lærer Python!"
melding2 = f"Jeg er {alder} år gammel."

# Vi ser at navn (og alder) har en forskjellig verdi nå
print(melding1, melding2)
alder = input(f"Hvor gammel er du, {navn}? ")


# In[5]: ----------------------------------------


# Definer prisene
pris_frokost = 149.90
pris_rom = 1000

# Skriv ut priser på en strukturert måte
# Med \n kan vi spesifisere at vi vil ha et linjeskift
melding = f"***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n"
print(melding)

n_personer = 3
print(f"Dere er {n_personer} personer.")

# Beregne den totale prisen for natten
pris = pris_rom + n_personer*pris_frokost
print(f"Da bør dere betale {pris}Kr.")


# In[6]: ----------------------------------------


pris_frokost = 149.90
pris_rom = 1000
melding = f"***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n"
print(melding)

# Nå ber vi brukeren om å angi antall personer
n_personer = input("Hvor mange personer er dere?")
print(f"Dere er {n_personer} personer.")

# /!\ Det utløser en feilmelding /!\:
# "TypeError: can't multiply sequence by non-int of type 'float'"
pris = pris_rom + n_personer*pris_frokost
print(f"Da bør dere betale {pris}Kr.")


# In[7]: ----------------------------------------


# La oss opprette noen variabler før vi sjekker typen deres
pris_frokost = 149.90
pris_rom = 1000
melding = f"***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n"
n_personer = input("Hvor mange personer er dere?")

# Vi ser at de har ulike typer!
print(f"type(pris_frokost):                {type(pris_frokost)}")
print(f"type(pris_rom):                    {type(pris_rom)}")
print(f"type(pris_frokost + pris_rom):     {type(pris_frokost + pris_rom)}")
print(f"type(melding):                     {type(melding)}")

# Også ga vi et heltall men typen er streng!
print(f"type(n_personer):                  {type(n_personer)}")


# In[8]: ----------------------------------------


# Her konverterer vi et heltall (int) til et flyttall (float)
print(f"float(pris_rom)):   {float(pris_rom)}")

# Vær forsiktig når du konverterer flyttall til heltall!
# int(149.90) = 149!
print(f"{pris_frokost} != {int(pris_frokost)}")

# Vær forsiktig når du konvertere et uttrykk
# Utrykket evalueres før det konverteres!
print(f"{4+7} er lik {str(4+7)} men {'4+7'} er forskjellig.")


# In[9]: ----------------------------------------


# Det er ikke alltid mulig og konvertere en variabel
float("3.0")     # Ja
# /!\ Det utløser en feilmelding /!\:
int("3.0")       # Nei
# /!\ Det utløser en feilmelding /!\:
float("Hello")   # Nei


# In[10]: ----------------------------------------


pris_frokost = 149.90
pris_rom = 1000
melding = f"***Priser***\nFrokost: {pris_frokost} \nRom. {pris_rom}\n"
print(melding)

# Nå konverterer vi strengen som input funksjonen returnerer til et heltall
n_personer = int(input("Hvor mange personer er dere?"))
print(f"Dere er {n_personer} personer.")

pris = pris_rom + n_personer*pris_frokost
print(f"Da bør dere betale {pris}Kr.")

