# Playground

# Test for loop to print data from dictionary

data = {
    'cat0': {
        'opt1': 'True',
        'opt2': 'False'
    },
    'cat1': {
        'opt1': 'False',
        'opt2': 'True'
    }
}

for cat in data:
    currCat = cat
    print('\n' + currCat)
    for opt in data[currCat]:
        print(' -' + data[currCat][opt])
