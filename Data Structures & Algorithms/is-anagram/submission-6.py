class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Hash table with and keep track of each letter?
        countS, countT = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            #Letter : amount
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
