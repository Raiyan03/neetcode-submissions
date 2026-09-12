class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        if (len(nums) == 2):
            if nums[0] + nums[1] == target:
                return [0, 1]
        for i in range(len(nums)):
            hashTable[nums[i]] = i
        for c in range(len(nums)):
            if hashTable.get(target - nums[c], False) != False:
                if c == hashTable.get(target - nums[c], False):
                    continue
                return [c, hashTable.get(target - nums[c], False)]
