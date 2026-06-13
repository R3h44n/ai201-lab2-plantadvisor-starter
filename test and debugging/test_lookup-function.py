import sys
from ..tools import lookup_plant

print(lookup_plant("SNAKE PLANT"))     # strip+lower → matches display name?
print()
print(lookup_plant("devil's ivy"))      # alias → pothos? (verify in plants.json)
print()
print(lookup_plant("Monstera deliciosa"))  # scientific name path
print()
print(lookup_plant("  pothos  "))       # whitespace
print()
print(lookup_plant("frangipani"))        # not found → check the message reads as an instruction
print()