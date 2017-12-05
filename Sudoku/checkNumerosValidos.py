
def sonEnteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int):
                return False
    return True


def numerosEnRango(sudoku):
    numerosValidos = range(0, len(sudoku) + 1)
    for fila in sudoku:
        for numero in fila:
            if numero not in numerosValidos:
                return False
    return True


def checkNumerosValidos(sudoku):
    return sonEnteros(sudoku) and numerosEnRango(sudoku)


if __name__ == '__main__':
    import CasosTest

    for element in sorted(CasosTest.__dict__):
        if element.startswith('__'):
            pass
        else:
            print(element, '-> ', checkNumerosValidos(CasosTest.__dict__[element]))
