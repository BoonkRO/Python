
def checkFilas(sudoku):
    assert isinstance(sudoku, list), "Sudoku no es una lista."
    for fila in sudoku:
        posicionNumero = 0
        for numero in fila:
            if numero in fila[posicionNumero + 1:]:
                return False
            else:
                posicionNumero += 1
    return True


if __name__ == '__main__':
    import CasosTest

    for element in sorted(CasosTest.__dict__):
        if element.startswith('__'):
            pass
        else:
            print(element, '->', checkFilas(CasosTest.__dict__[element]))