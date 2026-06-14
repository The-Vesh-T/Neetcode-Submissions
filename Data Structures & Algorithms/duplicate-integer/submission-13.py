class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a set
        dupe = set()
        
        for num in nums:
            if num in dupe:
                return True
            dupe.add(num)
        return False