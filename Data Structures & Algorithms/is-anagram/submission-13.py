class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S, T = {}, {}
        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i], 0)
            T[t[i]] = 1 + T.get(t[i], 0)
        return S == T
