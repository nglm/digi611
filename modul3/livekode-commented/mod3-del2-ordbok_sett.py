# In[1]: ----------------------------------------


# En tom ordbok
tom_ordbok = {}
print(f"En tom ordbok: {tom_ordbok}")

# En ordbok med ulike typer informasjon om noe spesifikk
norge = {
    "land": "Norge",
    "befolkning" : 5500000,
    "språk" : ["bokmål", "nynorsk", "samisk"],
    "republikk" : False
}

# En ordbok med alltid samme type informasjon, men for flere ting.
hovedsteder = {
    "Norge" : "Oslo",
    "Danmark": "København",
    "Sverige" : "Stockholm",
}

print(f"Typen til en ordbok er:    {type(norge)}")

# Få tilgang til en verdi ved å bruke dens tilsvarende nøkkel.
print(f"Hovedstaden i Danmark er:  {hovedsteder['Danmark']}")

# Oppdater en verdi
hovedsteder["Norge"] = "Bergen"

# Opprett et nytt nøkkel-verdi par
hovedsteder["Frankrike"] = "Paris"

# Vi ser at ordboken ble oppdatert
print(hovedsteder)


# In[2]: ----------------------------------------


for (land, hovedstad) in hovedsteder.items():
    print(f'Nøkkel: {land}    |    Verdi: {hovedstad}')


# In[3]: ----------------------------------------


norge = {
    "land": "Norge",
    "befolkning" : 5500000,
    "språk" : ["bokmål", "nynorsk", "samisk"],
    "republikk" : False
}
print(norge)

# Hvor mange nøkkel-verdi par er det?
print(f"{len(norge) = }")

# Sjekk om en *nøkkel* er i ordboka
print(f"{'språk' in norge = }")
print(f"{5500000 in norge = }")

# Ta ut en verdi fra ordbok
print(f'{norge.pop("språk")}')
# Nøkkelen språk er ikke lenger i ordboka (og den tilsvarende verdien)
print(norge)
# Gjør det samme men returnere verdien "Bergen" hvis nøkkelen
# "hovedstad" ikke er i ordboka
print(f'{norge.pop("hovedstad", "Bergen")}')


# In[4]: ----------------------------------------


# /!\ Det utløser en feilmelding /!\
# Bruken "pop" uten å spesifisere standardreturverdien utløser en feil
# om nøkkelen ikke er i ordboka!
print(f'{norge.pop("hovedstad")}')


# In[5]: ----------------------------------------


mitt_sett = {12, True, 12, "DIGI", 12, True}
# Et sett en uordnet samling!
print(mitt_sett)
print("Typen til et sett er: ", {type(mitt_sett)})

# En liste over matrestriksjoner fra deltakerregistreringen
mat_restriksjoner = [
    "egg", "nøtter", "kjøtt", "svinn", "fisk",
    "laktose", "gluten",  "fisk", "laktose", "gluten", "kjøtt",
    "nøtter", "melk", "svinn", "svinn", "egg",
    "laktose", "fisk", "melk", "egg", "egg", "melk", "svinn",
    "fisk", "nøtter", "nøtter", "melk", "fisk", "laktose",
    "nøtter", "gluten", "gluten", "kjøtt",
    "kjøtt"
]

# Vi kan opprette et sett fra en liste
unike_mat_restriksjoner = set(mat_restriksjoner)
print(unike_mat_restriksjoner)


# In[6]: ----------------------------------------


# Det er mulig og beregne hvor mange elementer det er i settet
len(unike_mat_restriksjoner)

# Det er mulig å iterere gjennom et sett
for element in mitt_sett:
    print(element)

# Og å sjekke om noe er i settet
print(f"{12 in mitt_sett = }")


# In[7]: ----------------------------------------


# /!\ Det utløser en feilmelding /!\
unike_mat_restriksjoner[0]


# In[8]: ----------------------------------------


print(mat_restriksjoner)

mitt_sett = set(mat_restriksjoner)
print(mitt_sett)

# Tilbake til en list men med bare unike verdier!
min_list = list(set(mat_restriksjoner))
print(min_list)

