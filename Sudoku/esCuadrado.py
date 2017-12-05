
def esCuadrado(sudoku):
    assert isinstance(sudoku, list), "Sudoku no es una lista."
    numeroFilas = len(sudoku)
    for fila in sudoku:
        if len(fila) != numeroFilas:
            return False
    return True


if __name__ == '__main__':
    import CasosTest

    for element in sorted(CasosTest.__dict__):
        if element.startswith('__'):
            pass
        else:
            print(element, '->', esCuadrado(CasosTest.__dict__[element]))
