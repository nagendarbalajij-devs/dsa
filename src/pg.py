from collections import deque
from typing import Counter, List
import math


def main():
    s = Solution()
    print(s.totalNQueens(6))
    print(s.totalNQueens(7))
    print(s.totalNQueens(8))
    print(s.totalNQueens(9))

    # print(s.solveNQueens(1))

def matrix_print(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

class Solution:
    res = 0
    def totalNQueens(self, n: int) -> int:
        
        c_set = set()
        ps_set = set()
        ng_set = set()

        def backtrack(r):
            if r == n:
                self.res+=1
                return
            
            for c in range(n):
                if c in c_set or (r+c) in ps_set or (r-c) in ng_set:
                    continue
                    
                c_set.add(c)
                ps_set.add(r+c)
                ng_set.add(r-c)

                backtrack(r+1)

                c_set.remove(c)
                ps_set.remove(r+c)
                ng_set.remove(r-c)
        
        backtrack(0)

        return self.res        
        
main()