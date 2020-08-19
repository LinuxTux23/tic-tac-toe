# Python Tic Tac Toe created by Benedikt Lohse

gameField = {
    'A': {
        '1': 'A1',
        '2': 'A2',
        '3': 'A3'
    },
    'B': {
        '1': 'B1',
        '2': 'B2',
        '3': 'B3'
    },
    'C': {
        '1': 'C1',
        '2': 'C2',
        '3': 'C3'
    },
}


def printInstructions():
    print('Game Field Addresses:')
    print('---------------------')
    print('[ A1 ] [ A2 ] [ A3 ]')
    print('[ B1 ] [ B2 ] [ B3 ]')
    print('[ C1 ] [ C2 ] [ C3 ]')
    print('---------------------')

def printGameField():
    print('Current Game Field Values:')
    print('---------------------')

    i = 0

    while i > 3:
        for row in gameField:
            print('[ ' + str(gameField[str(row)][str(i)]) + ' ]'
                  '[ ' + str(gameField[str(row)][str(i)]) + ' ]'
                  '[ ' + str(gameField[str(row)][str(i)]) + ' ]')
        i += 1

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


def insertInputToGrid(row, column, input):
    gameField[row][column] = input


printInstructions()

#print('Its Your turn !\n')
#answer = str(input('Address: '))

#if validateInput(answer):
#    print('OK')
#else:
#    print('Address not valid !')

#printGameField()

print('Start')

column = 1

#while row <= 3:
#    for column in gameField.keys():
#        print('[ ' + str(gameField[str(column)][str(row)]) + ' ]')
#    row += 1


for row in gameField.keys():

    while column <= 3:
        print('[ ' + str(gameField[str(row)][str(column)]) + ' ]')
        column += 1


# Test Insert into Grind Function
insertInputToGrid('A', '1', 'test')
print(gameField['A']['1'])



