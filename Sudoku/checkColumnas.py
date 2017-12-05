
def checkColumnas(sudoku):
    assert isinstance(sudoku, list), "Sudoku no es una lista."
    numeroDeFilas = len(sudoku)
    filaActual = 0
    for fila in sudoku:
        for numero in fila:
            filaSiguiente = filaActual + 1
            while filaSiguiente < numeroDeFilas:
                try:
                    posicionNumeroFilaSiguiente = sudoku[filaSiguiente].index(numero)
                except ValueError:
                    return False
                else:
                    if posicionNumeroFilaSiguiente == fila.index(numero):
                        return False
                    else:
                        filaSiguiente += 1
        filaActual += 1
    return True


if __name__ == '__main__':
    import CasosTest

    for element in sorted(CasosTest.__dict__):
        if element.startswith('__'):
            pass
        else:
            print(element, '->', checkColumnas(CasosTest.__dict__[element]))
