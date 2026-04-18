class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap = [0]*26
        tmap = [0]*26

        for i in range(len(s)):
            smap[ord('a')-ord(s[i])] += 1
            tmap[ord('a')-ord(t[i])] += 1
        return smap == tmap