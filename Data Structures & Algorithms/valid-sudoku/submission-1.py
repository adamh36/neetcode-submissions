class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        # Validate Rows
        # i = current row, j walks across each column in that row
        for i in range(9):
            s = set()  # fresh set for each row
            for j in range(9):
                item = board[i][j]  # board[row][col]
                if item in s:  # duplicate found in this row
                    return False
                elif item != ".":  # skip empty cells
                    s.add(item)

        # Validate Columns
        # i = current column (fixed), j walks down each row in that column
        for i in range(9):
            s = set()  # fresh set for each column
            for j in range(9):
                item = board[j][i]  # board[row][col] — j and i swapped to scan vertically
                if item in s:  # duplicate found in this column
                    return False
                elif item != ".":  # skip empty cells
                    s.add(item)

        # Validate 3x3 Boxes
        # start_position holds the top-left corner of each of the 9 boxes
        start_position = [(0,0),(0,3),(0,6),
                          (3,0),(3,3),(3,6),
                          (6,0),(6,3),(6,6)]

        for i, j in start_position:  # i = starting row, j = starting col of each box
            s = set()  # fresh set for each box
            for row in range(i, i+3):  # scan 3 rows inside the box
                for col in range(j, j+3):  # scan 3 cols inside the box
                    item = board[row][col]
                    if item in s:  # duplicate found in this box
                        return False
                    elif item != ".":  # skip empty cells
                        s.add(item)

        return True  # passed all three checks, board is valid