class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i, num in enumerate(nums):
            lst.append([num, i])

        lst.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            curr = lst[i][0] + lst[j][0]
            if curr == target:
                return [min(lst[i][1], lst[j][1]),
                        max(lst[i][1], lst[j][1])]
            elif curr > target:
                j -= 1
            else:
                i += 1
        return []