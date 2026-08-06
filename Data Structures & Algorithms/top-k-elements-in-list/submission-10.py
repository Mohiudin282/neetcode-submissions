class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()
        res = []
        i = 0
        while i < k:
            res.append(arr.pop()[1])
            i+=1
        return res