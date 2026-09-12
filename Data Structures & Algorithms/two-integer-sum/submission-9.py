class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i, j in enumerate(nums):
            if target - j in hashSet.keys():
                return [hashSet[target - j], i]
            hashSet[j] = i
