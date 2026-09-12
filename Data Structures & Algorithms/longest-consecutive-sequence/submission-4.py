class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in nums:
            count = 1
            if i - 1 in numset:
                continue
            else:
                num = i + 1
                while num in numset:
                    count += 1
                    num += 1
            longest = max(count, longest)
        return longest