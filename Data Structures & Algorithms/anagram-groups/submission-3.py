class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                #For each check each letter and increase the count on the index
                count[ord(c) - ord('a')] += 1
            #count can change its mutable, but we need it immutable
            result[tuple(count)].append(s)
        return list(result.values())