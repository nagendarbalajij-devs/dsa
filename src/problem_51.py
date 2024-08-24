import string
from typing import List


def main():
    s = Solution()
    test_cases = [
        (4,),
        (1,), 
    ]

    for tc in test_cases:
        print(s.solveNQueens(*tc))
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess_board = [["."] * n for i in range(n)]
        res = []

        c_set = set()
        ps_set = set()
        ng_set = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in chess_board])
                return
            
            for c in range(n):
                if c in c_set or (r+c) in ps_set or (r-c) in ng_set:
                    continue
                    
                c_set.add(c)
                ps_set.add(r+c)
                ng_set.add(r-c)
                chess_board[r][c] = "Q"

                backtrack(r+1)

                c_set.remove(c)
                ps_set.remove(r+c)
                ng_set.remove(r-c)
                chess_board[r][c] = "."
        
        backtrack(0)

        return res   
        