class Sudoku:
    def _init_(self, board=None):
        if board is None:
            self.board = [[0] * 9 for _ in range(9)]  # Tablero vacío si no se proporciona ninguno.
        else:
            self.board = board  # Inicializa el objeto Sudoku con un tablero dado.
       
    def is_valid(self, row, col, num):
        # Verifica si es válido colocar un número en una celda específica según las reglas del Sudoku.
        row_set = set(self.board[row])
        col_set = set(self.board[i][col] for i in range(9))
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        grid_set = set(self.board[start_row + i][start_col + j] for i in range(3) for j in range(3))
        
        return num not in row_set and num not in col_set and num not in grid_set

    def find_empty(self):
        # Encuentra la próxima celda vacía en el tablero.
        return {(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0}

    def solve(self):
        empty_cells = self.find_empty()

        if not empty_cells:
            return True  # Si no hay celdas vacías, el Sudoku está resuelto.
        
        (row, col) = empty_cells.pop()

        for num in range(1, 10):
            # Intenta colocar un número en la celda y luego resuelve recursivamente.
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0  # Revierte si la solución no es válida.

        return False

    def display(self):
        # Muestra el tablero del Sudoku en la consola.
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def is_solved(self):
        # Verifica si el Sudoku está completamente resuelto.
        return all(self.board[i][j] != 0 for i in range(9) for j in range(9))
    
        return True
    def _repr_(self):
        return f"Sudoku({self.board})"
    
    def __check_duplicates(self, lst):
        # Método privado para verificar duplicados en una lista.
        unique = set()
        for item in lst:
            if item != 0:
                if item in unique:
                    return False
                unique.add(item)
        return True




board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku = Sudoku(board)
print("Sudoku original:")
sudoku.display()

while not sudoku.is_solved():
    row = int(input("Ingrese el número de fila (1-9): ")) - 1
    col = int(input("Ingrese el número de columna (1-9): ")) - 1
    num = int(input("Ingrese el número (1-9) para colocar en esa celda: "))

    if not sudoku.is_valid(row, col, num):
        print("¡Número inválido! Por favor, ingrese otro número.")
    else:
        sudoku.board[row][col] = num
        print("Sudoku actualizado:")
        sudoku.display()
        

print("\n¡Felicidades! Has resuelto el Sudoku correctamente:")
sudoku.display()
