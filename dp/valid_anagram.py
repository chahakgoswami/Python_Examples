class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.sort()
        t.sort()
        return s==t