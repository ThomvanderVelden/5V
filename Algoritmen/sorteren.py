# Kies een sorteer algoritme en implementeer deze in de functie hieronder
# Je mag zelf kiezen: selection sort, insertion sort of bubble sort
# Selection soort is het minst moeilijk en bubble sort is het moeilijkst

def sorteer(x):
  
  return ...
  
  
# een gesorteerde lijst moet gesorteerd blijven
assert sorteer([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
# Bijna gesorteerd
assert sorteer([1, 2, 3, 4, 6, 5]) == [1, 2, 3, 4, 5, 6]
# Omgedraaid
assert sorteer([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
# random
assert sorteer([5, 2, 8, 9, 1]) == [1, 2, 5, 8, 9]
# lengte 0
assert sorteer([]) == []
# lengte 1
assert sorteer([1]) == [1]
