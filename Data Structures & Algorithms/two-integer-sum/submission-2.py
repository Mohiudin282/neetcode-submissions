class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for ind, val in enumerate(nums, 0):
            if val in dict:
                return [dict[val], ind]
            else:
                dict[target - val] = ind
            