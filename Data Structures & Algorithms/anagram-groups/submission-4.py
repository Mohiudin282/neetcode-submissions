class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            record[sortedS].append(s)
        return list(record.values())