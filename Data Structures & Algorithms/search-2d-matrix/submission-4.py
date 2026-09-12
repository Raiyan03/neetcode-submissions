class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        n = len(matrix[0])
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[mid // n][mid % n] > target:
                r = mid - 1
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                return True
        return False



    #     n = len(matrix[0]) - 1
    #     i = 0
    #     while i < len(matrix):
    #         if matrix[i][n] < target:
    #             i += 1
    #         elif matrix[i][n] > target:
    #             return self.binarySearch(matrix[i], target)
    #         else:
    #             return True
    #     return False
    
    # def binarySearch(self, arr, target):
    #     l, r = 0, len(arr) - 1
    #     while l <= r:
    #         mid = l + ((r - l) // 2)
    #         print(arr[mid])
    #         if arr[mid] > target:
    #             r = mid - 1
    #         elif arr[mid] < target:
    #             l = mid + 1
    #         else:
    #             return True
    #     return False