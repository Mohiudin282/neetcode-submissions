class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        gram = {}
        for c in s:
            ana[c] = 1 + ana.get(c, 0)
        for c in t:
            gram[c] = 1 + gram.get(c, 0)
        if ana == gram:
            return True
        return False