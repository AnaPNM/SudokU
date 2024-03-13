class Sudoku:
    def _init_(self, board=None):
        self.board = board  # Inicializa el objeto Sudoku con un tablero dado.

    def is_valid(self, row, col, num):
        # Verifica si es válido colocar un número en una celda específica según las reglas del Sudoku.
        row_set = set(self.board[row])
        col_set = set(self.board[i][col] for i in range(9))
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        grid_set = set(self.board[start_row + i][start_col + j] for i in range(3) for j in range(3))
        
        return num not in row_set and num not in col_set and num not in grid_set