class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Given 2 strings, check if they have same characters but jumble order
        #Turn into list, then sort, then compare
        #Sort method does first two automatically
        return sorted(s) == sorted(t)