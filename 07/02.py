'''
  Diogo Costa
  2020-04-03

  Description:
    Dictionaries within disctionaries
'''

party_items = {
    "Bob": {
        "patties": 30,
        "croquettes": 40,
        'chips': 1,
        'boiled eggs': 20
    },
    'Alice': {
        'beers': 10,
        'soda': 20,
        'wine': 2
    },
    'Peter': {
        'roast chickens': 3,
        'sardines': 50
    }
}

print(party_items)

print(party_items["Bob"]["patties"])  # 30
print(party_items["Alice"]["soda"])  # 20

print(len(party_items))  # 3
print(len(party_items["Bob"]))  # 4
