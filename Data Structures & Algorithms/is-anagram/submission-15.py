class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #Create a frequency per each letter 
        S, T = {}, {}
        for c in range(len(s)):
            #Link letter to the count, increment if seen
            S[s[c]] = 1 + S.get(s[c], 0)
            T[t[c]] = 1 + T.get(t[c], 0)
        return S ==T
