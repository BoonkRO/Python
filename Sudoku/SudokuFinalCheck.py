import SudokuEsCuadrado
import SudokuNumerosValidos
import SudokuCheckFilas
import SudokuCheckColumnas
import TDDSudoku



def finalCheck(sudoku):
    return SudokuEsCuadrado.esCuadrado(sudoku) and SudokuNumeroValidos.checkNumerosValidos(sudoku) \
        and SudokuCheckFilas.checkFilas(sudoku) and SudokuCheckColumnas.checkColumnas(sudoku)


TDDSudoku.functForTDD(True, finalCheck, "correcto")
