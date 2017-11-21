
def checkNumerosValidos(sudoku):
    assert isinstance(sudoku, list), "Sudoku debe ser una lista"
    # precondiciones

    for fila in sudoku:
        for numero in fila:
            assert isinstance(numero, int), numero + " no es un numero"

    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:
        for numero in fila:
            if numero not in numerosValidos:
                return False

        return True
