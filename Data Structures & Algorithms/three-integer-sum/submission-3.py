class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, value in enumerate(nums):
            if value > 0:
                break
            if index > 0 and value == nums[index - 1 ]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                checkSum = value + nums[l] + nums[r]
                if checkSum > 0:
                    r -= 1
                elif checkSum < 0:
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res