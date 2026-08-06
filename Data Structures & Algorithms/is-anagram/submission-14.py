class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = {}
        freq2 = {}
        for char in s:
            freq1[char] = 1 + freq1.get(char, 0)
        for char in t:
            freq2[char] = 1 + freq2.get(char, 0)
        return freq1 == freq2