class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashTable:
                return [hashTable[diff], i]
            hashTable[v] = i
            