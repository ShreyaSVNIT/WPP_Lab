from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    cols = set()
    posDiag = set() # positive diagonals (r + c)
    negDiag = set() # negative diagonals (r - c)
    res = []
    board = [['.'] * n for _ in range(n)]

    def backtrack(r):

        # if all the queens are placed, save the board.
        if r == n:

            #convert board into list of strings
            res.append(["".join(row) for row in board])
            return

        for c in range(n):

            #check if the column or diagonals are already occupied
            if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                continue

            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

             #backtrack: remove the queen and free the spot
            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res


n = int(input("Enter the value of N: "))
solutions = solveNQueens(n)
print(f"Total solutions: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(row)
    print()

#we try placing a queen row-by-row.
#before placing, we check if that column or diagonal is already attacked.
#if it's safe, we place the queen and move to the next row.
#nce we reach the end (row == n), we’ve found a valid solution.
#backtrack to explore all possible configurations.

