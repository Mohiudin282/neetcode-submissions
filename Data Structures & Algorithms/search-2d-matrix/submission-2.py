class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, arr in enumerate(matrix):
            l = 0
            r = len(arr) - 1

            while l <= r:
                mid = (r + l) // 2
                if arr[mid] == target:
                    return True
                if arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False