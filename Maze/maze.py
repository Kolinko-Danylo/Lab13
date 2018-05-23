# Implements the Maze ADT using a 2-D array.
from Maze.arrays import Array2D
from Maze.lliststack import Stack


class Maze:
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = " *"
    PATH_TOKEN = " x"
    TRIED_TOKEN = " o"

    # Creates a maze object with all cells marked as open.
    def __init__(self, num_rows, num_cols):
        self._mazeCells = Array2D(num_rows, num_cols)
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maze.
    def num_rows(self):
        return self._mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols(self):
        return self._mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def setWall(self, row, col):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart(self, row, col):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition(row, col)

    # Sets the exit cell position.
    def setExit(self, row, col):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition(row, col)

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath(self):
        print(self._startCell.row, self._startCell.col)
        print(self._exitCell.row, self._exitCell.col)
        path_stack = Stack()
        current = self._startCell
        while not self._exitFound(current.row, current.col):
            print(current.row, current.col)
            temp_ind = 0
            for i in [-1, 1]:
                if self._validMove(current.row + i, current.col):
                    temp_ind = _CellPosition(current.row + i, current.col)
                    break
                elif self._validMove(current.row, current.col + i):
                    temp_ind = _CellPosition(current.row, current.col + i)
                    break
            self._markTried(current.row, current.col)
            if temp_ind:
                path_stack.push(current)
                current = temp_ind
                continue

            try:
                current = path_stack.pop()
            except (KeyError, AssertionError):
                return False

        try:
            while True:
                path_elem = path_stack.pop()
                self._markPath(path_elem.row, path_elem.col)
        except (KeyError, AssertionError):
            self._markPath(self._exitCell.row, self._exitCell.col)
            pass

        return True



    # Resets the maze by removing all "path" and "tried" tokens.
    def reset(self):
        self._mazeCells.clear()
        self._startCell = None
        self._exitCell = None

    # Prints a text-based representation of the maze.
    def draw(self):
        print("MAZE:")
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                print(self._mazeCells[i, j] if self._mazeCells[i, j]is not None else '  ', end='')
            print()

    # Returns True if the given cell position is a valid move.
    def _validMove(self, row, col):
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried(self, row, col):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath(self, row, col):
        self._mazeCells[row, col] = self.PATH_TOKEN


# Private storage class for holding a cell position.
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
