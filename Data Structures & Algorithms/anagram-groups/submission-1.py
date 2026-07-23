#do i have to import defaultdict?
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        #Create a frequency count again, iterate to strings, then through each string
        for s in strs:
            #dictionary mmust be unmutable so give set length and increase based off of that
            count = [0] * 26

            for c in s:
                #increase based on the number conversion of the letter??
                #How do i increase the count in proper place
                #count[index] +=1 so how get index
                count[ord(c) - ord('a')] += 1
            # tuple the array. if this count pattern is seen
            my_dict[tuple(count)].append(s)
        return list(my_dict.values())