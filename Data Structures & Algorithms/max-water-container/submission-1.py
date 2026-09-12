class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        
        while l < r:
            subArea = 0
            if heights[l] > heights[r]:
                subArea = heights[r] * (r - l)
                r -= 1
            else:
                subArea = heights[l] * (r - l)
                l += 1
            area = max(subArea, area)
        return area