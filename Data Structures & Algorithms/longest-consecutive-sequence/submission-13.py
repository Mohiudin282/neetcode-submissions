class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        remdup = set(nums)
        longest = 0
        for num in remdup:
            if num -1 not in remdup:
                current = 1
                while num + current in remdup:
                    current+=1
                longest = max(current, longest)
        return longest