class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = s.replace(" ", "").lower()
        l = 0
        r = len(str) - 1
        while l < r:
            while l < r and not str[l].isalnum():
                l+=1
            while r > l and not str[r].isalnum():
                r-=1
            if str[l] != str[r]:
                return False
            l+=1
            r-=1
        return True