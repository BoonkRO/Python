
def checkFilas(sudoku):
    posicion = 0
    for fila in sudoku:
        for numero in fila:
            if numero in fila[posicion + 1:]:
                return False
            else:
                posicion += 1

    return True

