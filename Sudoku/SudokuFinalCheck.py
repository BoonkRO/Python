import SudokuNumeroValidos
import SudokuCheckFilas
import SudokuCheckColumnas
import TDDSudoku
import SudokuEsCuadrado


def finalCheck(sudoku):
    return SudokuEsCuadrado.esCuadrado(sudoku) and SudokuNumeroValidos.checkNumerosValidos(sudoku) \
        and SudokuNumeroValidos.checkNumerosValidos(sudoku) and SudokuCheckFilas.checkFilas(sudoku) \
        and SudokuCheckColumnas.checkColumnas(sudoku)

TDDSudoku.casosTest()