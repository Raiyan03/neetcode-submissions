class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            mult=1
            for k in range(len(nums)):
                if i != k:
                    mult = mult * nums[k]
            res.append(mult)
        return res