# Python Tic Tac Toe created by Benedikt Lohse

import os
import sys

gameField = {
    'A': {
        '1': '',
        '2': '',
        '3': ''
    },
    'B': {
        '1': '',
        '2': '',
        '3': ''
    },
    'C': {
        '1': '',
        '2': '',
        '3': ''
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

    for row in gameField:
        rowSave = row
        for col in gameField[rowSave]:
            sys.stdout.write('[ ' + gameField[rowSave][col] + ' ]')
        print('')

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


def userAddressInput():
    print('Its Your turn !\n')
    answer = str(input('Address: '))

    if validateInput(answer):
        print('OK')
        insertInputToGrid(answer[0].capitalize(), answer[1], 'X')
        os.system("cls")
    else:
        print('Address not valid !')

    printGameField()


printInstructions()

count = 0

while count < 4:
    userAddressInput()
    count += 1
