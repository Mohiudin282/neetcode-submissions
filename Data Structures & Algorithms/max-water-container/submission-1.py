class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            for r in range(i + 1, len(heights)):
                area = (r - i)*min(heights[i], heights[r])
                largest = max(largest, area)
        return largest