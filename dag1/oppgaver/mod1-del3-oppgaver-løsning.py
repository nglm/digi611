# %% -------------------------------------------------------------------
def sirkel(r):
    # Beregn omkretsen
    omkrets = 2 * 3.14 * r
    # Beregn areal
    areal = 3.14 * r**2
    # Returner omkretsen og arealet
    return omkrets, areal

# Skriv ut direkte returverdiene
print(sirkel(1))
print(sirkel(3))
radius = 8.1
# Eller lagr returverdiene i variabler og skriv ut variablene senere
o, a = sirkel(radius)
print(f"Radius: {radius}, Omkretsen: {o}, Arealet: {a}")

# %% -------------------------------------------------------------------

def multiplikasjon():
    a = int(input("Først tall: "))
    b = int(input("Andre tall: "))
    res = a*b
    print(f"{a} * {b} = {res}")
    return a, b, res

tall1, tall2, resultat = multiplikasjon()