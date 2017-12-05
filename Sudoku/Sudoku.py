# Archivo principal desde donde ejecutar el programa

import esCuadrado, checkNumerosValidos, checkFilas, checkColumnas

def check_sudoku(sudoku):

    return esCuadrado.esCuadrado(sudoku) and checkNumerosValidos.checkNumerosValidos(sudoku) \
           and checkFilas.checkFilas and checkColumnas.checkColumnas(sudoku)


if __name__ == '__main__':
    import CasosTest

    for element in sorted(CasosTest.__dict__):
        if element.startswith('__'):
            pass
        else:
            print(element, '->', check_sudoku(CasosTest.__dict__[element]))
