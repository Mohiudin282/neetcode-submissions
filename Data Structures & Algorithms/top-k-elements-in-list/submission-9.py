class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i, 0)
        arr = []
        for num, freq in dict.items():
            arr.append([freq, num])

        arr.sort()
        res = []
        i = 0
        while i < k:
            res.append(arr.pop()[1])
            i+=1
        return res