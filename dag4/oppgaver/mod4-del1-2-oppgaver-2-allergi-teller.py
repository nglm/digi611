"""
Oppgave: Skriv en funksjon som tar som parameter en liste over alle matrestriksjonene til deltakerne på et arrangement og:

- for hver allergi beregner antallet personer som har denne
spesifikke allergien.
- returnerer en ordbok som inneholder antallet personer allergiske
for hver allergi.

Hint: Det finnes ulike måter å løse denne oppgaven på. En av dem
inkluderer å bruke (påkalle) vår tidligere funksjon fra
`mod4-del1-oppgaver-2-allergi.py`. En annen måte inkluderer å bruke en
if-setning med sekvensoperasjonen "in". I tillegg, i begge tilfeller
kan det være nyttig (men ikke obligatorisk) å bruke et sett
"""

# En list over matrestriksjoner fra deltakerregistreringen
mat_restriksjoner = [
    "egg", "nøtter", "kjøtt", "svinn", "fisk",
    "laktose", "gluten",  "fisk", "laktose", "gluten", "kjøtt",
    "nøtter", "melk", "svinn", "svinn", "egg",
    "laktose", "fisk", "melk", "egg", "egg", "melk", "svinn",
    "fisk", "nøtter", "nøtter", "melk", "fisk", "laktose",
    "nøtter", "gluten", "gluten", "kjøtt",
    "kjøtt"
]