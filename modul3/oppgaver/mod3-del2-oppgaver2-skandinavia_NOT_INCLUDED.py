"""
Oppdater ordboken "skandinavia" ved å iterere over listen "skandinaviske_land"
slik at "skandinavia" ordboken inkluderer all informasjon om landene.
Dvs at etter løkken, bør "skandinavia" innholder:
{
    'land': ['Norge', 'Sverige', 'Danmark'],
    'befolkning': 21300000,
    'språk': ['bokmål', 'nynorsk', 'samisk', 'svensk', 'dansk'],
    'areal': 790000
}

"""

# %% -------------------------------------------------------------------

# En ordbok for hvert skandinavisk land
norge = {
    "land": "Norge",
    "befolkning" : 5500000,
    "språk" : ["bokmål", "nynorsk", "samisk"],
    "areal" : 300000
}

sverige = {
    "land": "Sverige",
    "befolkning" : 10000000,
    "språk" : ["svensk"],
    "areal" : 450000
}

danmark = {
    "land": "Danmark",
    "befolkning" : 5800000,
    "språk" : ["dansk"],
    "areal" : 40000
}

# En liste over ordbøker som representerer hvert skandinavisk land
skandinaviske_land = [norge, sverige, danmark]

# Initialiser "skandinavia" ordboken
skandinavia = {
    "land" : [],
    "befolkning" : 0,
    "språk" : [],
    "areal" : 0
}
