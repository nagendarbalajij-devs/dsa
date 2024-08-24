def main():
    s = Solution()
    test_cases = [
        (4,),
        (1,), 
    ]

    for tc in test_cases:
        print(s.totalNQueens(*tc))
    
class Solution:
    res = 0
    def totalNQueens(self, n: int) -> int:
        self.res = 0
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