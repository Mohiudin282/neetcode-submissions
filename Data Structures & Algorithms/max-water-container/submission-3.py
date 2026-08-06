class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # largest = 0
        # for i in range(len(heights)):
        #     for r in range(i + 1, len(heights)):
        #         area = (r - i)*min(heights[i], heights[r])
        #         largest = max(largest, area)
        # return largest
        largest = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l)*min(heights[l],heights[r])
            largest = max(largest, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return largest
