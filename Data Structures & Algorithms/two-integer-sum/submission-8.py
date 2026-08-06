class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i, num in enumerate(nums):
            lst.append([num, i])
        lst.sort()
        l = 0
        r = len(lst) - 1
        while l < r:
            total = lst[l][0] + lst[r][0]
            if total == target:
                return [min(lst[l][1], lst[r][1]),
                        max(lst[l][1], lst[r][1])]
            elif total > target:
                r-=1
            else:
                l+=1