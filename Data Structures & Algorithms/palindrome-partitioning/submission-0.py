class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isp(i,j):
            if i==j:
                return True
            
            l,r = i,j
            while l <=r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        res = []
        def backtrack(i,c):
            if i == len(s):
                res.append(c[:])
                return
            
            for en in range(i,len(s)):
                if isp(i,en):
                    c.append(s[i:en+1])
                    backtrack(en+1,c)
                    c.pop()
        backtrack(0,[])
        return res