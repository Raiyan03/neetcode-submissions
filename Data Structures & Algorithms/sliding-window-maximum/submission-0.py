class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxL = []
        
        l = 0
        for r in range(k, len(nums) + 1):
            maxL.append(max(nums[l:r]))
            l += 1
        return maxL