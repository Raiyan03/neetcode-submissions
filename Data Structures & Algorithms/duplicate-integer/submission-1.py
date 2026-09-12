class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempList = []
        for num in nums:
            if num in tempList:
                return True
            tempList.append(num)
        return False