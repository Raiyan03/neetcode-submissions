class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        def binarySearch(l, r):
            while l <= r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    return mid
            return -1
        print(pivot)
        find = binarySearch(pivot, len(nums) - 1)

        if find != -1:
            return find
        else:
            return binarySearch(0, pivot - 1)
