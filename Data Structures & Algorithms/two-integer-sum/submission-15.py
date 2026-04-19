class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Use a hashmap with numbers and diffences
        known = {}
        #Loop must have both index, value
        for i, num in enumerate(nums):
            diff = target - num
            if diff in known:
                return[known[diff], i]
            known[num] = i
        