class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        rows = set()
        cols = set()
        diags = []
        mp = [["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                result.append(["".join(mp[i]) for i in range(n)])
                return           
            for c in range(n):
                if r not in rows and c not in cols and self.valid(r,c,diags):
                    mp[r][c] = "Q"
                    rows.add(r)
                    cols.add(c)
                    diags.append((r,c))
                    backtrack(r+1)
                    mp[r][c] = "."
                    rows.remove(r)
                    cols.remove(c)
                    diags.pop()
            return
        backtrack(0)
        return result


    def valid(self,r,c,diags):
            nr,pc = r,c
            while nr >=0:
                if (nr,pc) in diags:
                    return False
                nr -= 1
                pc -= 1
            
            nr,pc = r,c
            while nr>=0:
                if (nr,pc) in diags:
                    return False
                nr -= 1
                pc += 1
            return True
            
        
