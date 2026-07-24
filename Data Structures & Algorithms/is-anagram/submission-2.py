class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        var = sorted(s)
        var2 = sorted(t)
        if var ==var2:
            return True
        return False