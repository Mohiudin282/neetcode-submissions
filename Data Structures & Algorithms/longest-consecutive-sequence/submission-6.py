class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        longest = 0
        for i in range(len(nums)):
            current = 0
            if nums[i] - 1 not in arr:
                current+=1
                while nums[i] + current in arr:
                    current+=1
                longest = max(longest, current)
        return longest