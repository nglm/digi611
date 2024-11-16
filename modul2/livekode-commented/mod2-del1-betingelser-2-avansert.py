# In[1]: ----------------------------------------


a = True
b = False

# Syntaksen f"{uttrykk = }" skiver både uttrykket og evalueringen (resultatet)
# av uttrykket
print(f"a:              {a}")
print(f"b:              {b}")
print(f"not a:          {not a}")
print(f"not b:          {not b}")
print(f"a and b:        {a and b}")
print(f"a or b:         {a or b}")
print(f"not (a or b):   {not (a or b)}")


# In[2]: ----------------------------------------


karakter = 34

def eksamen(karakter):
    print(f"Du fikk {karakter}")
    # if 1
    # k >= 50: besto
    if karakter >= 50:
        print("Du besto")
    # k <  50: strøk
    else:
        print("Du strøk")
        # - if 2
        # - k >= 25: prøv igjen
        if karakter >= 25:
            print("Du kan prøve igjen")
        # - k <  25: kan ikke prøve igjen
        else:
            print("Du kan ikke prøve igjen")


# In[3]: ----------------------------------------


eksamen(62)


# In[4]: ----------------------------------------


eksamen(32)


# In[5]: ----------------------------------------


eksamen(18)


# In[6]: ----------------------------------------


def stor_rabatt(medlem, antall_artikler):
    print(f"Medlem: {medlem} Antall artikler kjøpt: {antall_artikler}")
    if medlem and (antall_artikler >= 3):
        print("Du får 60 prosent rabatt")


# In[7]: ----------------------------------------


stor_rabatt(True, 2)
stor_rabatt(True, 3)
stor_rabatt(False, 1)
stor_rabatt(False, 4)


# In[8]: ----------------------------------------


def rabatt(medlem, antall_artikler):
    print(f"Medlem: {medlem} Antall artikler kjøpt: {antall_artikler}")
    if medlem or (antall_artikler >= 3):
        print("Du får 30 prosent rabatt")


# In[9]: ----------------------------------------


rabatt(True, 2)
rabatt(True, 3)
rabatt(False, 1)
rabatt(False, 4)


# In[10]: ----------------------------------------


def flyttebil(pakker_volum, bil_max_volum):
    mulig = bil_max_volum >= pakker_volum
    if not mulig:
        print("Vi kan ikke ta alt på en gang.")
    else:
        print("Vi kan ta alt!")
        if bil_max_volum > 3*pakker_volum:
            print("Vi bør ta en MYE mindre bil.")
        elif bil_max_volum > 2*pakker_volum:
            print("Vi bør ta en litt mindre bil.")
        else:
            print("Vi tok den riktige størrelsen.")

    return mulig

mulig = flyttebil(15, 15)


# In[11]: ----------------------------------------


mulig = flyttebil(10, 15)


# In[12]: ----------------------------------------


mulig = flyttebil(7, 15)


# In[13]: ----------------------------------------


mulig = flyttebil(3, 15)


# In[14]: ----------------------------------------


# Opprett variabelen før løkken
total = 0
i = 1
print(f"Før løkken. i: {i}, total: {total}")

# Fortsett å legge til tall sammen så lenge den totale summen er mindre enn 100.
# 0 + 1 + 2 + 3 + 4 + ... + i - 1 + i
while total < 100:

    # Oppdater total sum (knyttet til betingelsen)
    total = total + i
    print(f"Iterasjon: {i}, total: {total}")

    # Oppdater iterasjonsvariabelen
    i = i + 1

print(f"Etter løkken. i: {i}, total: {total}")

