gameField = {
    'A': {
        '1': 0,
        '2': 0,
        '3': 0
    },
    'B': {
        '1': 0,
        '2': 0,
        '3': 0
    },
    'C': {
        '1': 0,
        '2': 0,
        '3': 0
    },
}


def printInstructions():
    print('Game Field Addresses:')
    print('---------------------')
    print('[ A1 ] [ A2 ] [ A3 ]')
    print('[ B1 ] [ B2 ] [ B3 ]')
    print('[ C1 ] [ C2 ] [ C3 ]')
    print('---------------------')


def searchKeyInGameField(row, column):
    row = str(row)
    column = str(column)

    for rowKey in gameField:
        rowKeySave = rowKey

        for columnKey in gameField[rowKeySave]:
            if rowKeySave == row.capitalize() and str(columnKey) == column:
                return True

    return False


def validateInput(answer):
    if len(answer) <= 2:
        if searchKeyInGameField(answer[0], answer[1]):
            return True
        else:
            return False
    else:
        return False

printInstructions()

print('Its Your turn !\n')
answer = str(input('Address: '))

if validateInput(answer):
    print('OK')
else:
    print('Address not valid !')





