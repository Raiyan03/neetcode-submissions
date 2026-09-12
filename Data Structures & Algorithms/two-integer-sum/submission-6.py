class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashTable.keys():
                return [hashTable[diff], index]
            hashTable[num] = index