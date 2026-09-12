class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashTable:
                return [ hashTable[diff], i ]
            hashTable[val] = i