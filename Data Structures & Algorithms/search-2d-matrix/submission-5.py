class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top = 0
        bot = ROW - 1

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] <  target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l, r = 0, COL - 1
        row = (top + bot) // 2
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False





        # l = 0
        # r = (len(matrix) * len(matrix[0])) - 1
        # n = len(matrix[0])
        # while l <= r:
        #     mid = l + ((r - l) // 2)
        #     if matrix[mid // n][mid % n] > target:
        #         r = mid - 1
        #     elif matrix[mid // n][mid % n] < target:
        #         l = mid + 1
        #     else:
        #         return True
        # return False



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