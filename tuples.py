""" Quick implementation of tuples """
president = [
    ("Geroge Washinton", 1797),
    ("John Adams", 1797),
    ("Thomas Jeffson", 1801),
    ("James Madison", 1809)
]

for prez, year in president:
    print("In {1}, {0} toke office".format(prez, year))