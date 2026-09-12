class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = {}

        for cur in nums:
            hashSet[cur] = hashSet.get(cur, 0) + 1
            if hashSet[cur] > 1:
                return cur