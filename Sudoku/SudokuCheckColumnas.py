
def checkColumnas(sudoku):
    primeraFila = sudoku[0]
    numeroDeFilas = len(primeraFila) - 1

    for numero in primeraFila:
        indexFilaActual = 0
        while indexFilaActual < numeroDeFilas:
            indexFilaSiguiente = indexFilaActual + 1

            try:
                posicionNumeroFilaSiguiente = sudoku[indexFilaSiguiente].index(numero)

            except ValueError:
                return False

            else:
                if posicionNumeroFilaSiguiente == primeraFila.index(numero):
                    return False
                else:
                    indexFilaActual += 1

    return True
