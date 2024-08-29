"""
`lineair_zoeken` vindt de locatie van een element in de lijst door gebruik te maken van een
lineair zoekalgoritme. Return de locatie van dit element.

Als een element niet gevonden kan worden, returnt de functie -1.

"""
def lineair_zoeken(lijst, element):
  for e in lijst:
    print(e)
  return -1
  
# assert geeft een error als het resultaat van een vergelijking `False` is. 
# Als je functie dus niet klopt zal python een error geven.

# Test dat een element gevonden kan worden
assert lineair_zoeken([1, 2, 3, 4, 5], 1) == 0

# Test dat een element aan het eind van de lijst gevonden kan worden
assert lineair_zoeken([1, 4, 3, 2], 4) == 1

# Test dat een element gevonden kan worden in een lijst met een lengte van 1
assert lineair_zoeken([1], 1) == 0

# Test dat een element zoeken in een lege lijst -1 returnt
assert lineair_zoeken([], 0) == -1

# Test dat een element zoeken dat niet bestaat in de lijst -1 returnt
assert lineair_zoeken([1, 2, 3, 4, 5, 6], 12) == -1

print("Als dit geprint wordt zijn alle tests goedgegaan")