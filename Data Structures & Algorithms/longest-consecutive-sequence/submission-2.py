class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = []
        if len(nums) <= 1:
            return len(nums)
        for num in numset:
            if num + 1 in numset:
                lenght = 1
                while num + lenght in numset:
                    lenght += 1
                longest.append(lenght)
            else:
                longest.append(1)
        return max(longest)
