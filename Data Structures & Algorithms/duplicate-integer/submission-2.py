class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempList = []
        for i in nums:
            if i in tempList:
                return True
            tempList.append(i)
        return False