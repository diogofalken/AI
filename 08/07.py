'''
  Diogo Costa
  2020-04-17

  Description:
    Create a program that based on the received list of items prints the total number of each number

    Bob: 
        - patties: 30;
        - croquettes: 40;
        - chips: 1;
        - boiled eggs: 20
    
    Alice: 
        - beers: 10;
        - soda: 20;
        - wine: 2;
    
    Ted: 
        - chips: 5;
        - boiled eggs: 3;
        - soda: 2;
'''

dictItems = {
    "Bob": {
        'patties': 30,
        'croquettes': 40,
        'chips': 1,
        'boiled eggs': 20,
    },
    "Alice": {
        "beers": 10,
        "soda": 20,
        "wine": 2,
    },
    "Ted": {
        "chips": 5,
        "boiled eggs": 3,
        "soda": 2,
    }
}

sumItems = {}
for x in dictItems:
    for y in dictItems[x]:
        if y not in sumItems:
            sumItems[y] = 0
        sumItems[y] += dictItems[x][y]

print(sumItems)