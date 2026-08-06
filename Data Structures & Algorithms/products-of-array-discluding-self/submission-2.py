class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            k = 1
            l = 0
            while l < len(nums):
                if l == i:
                    l+=1
                    continue
                k*=nums[l]
                l+=1
            res.append(k)
        return res