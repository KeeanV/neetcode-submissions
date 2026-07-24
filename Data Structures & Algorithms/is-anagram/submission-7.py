class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count frequencies of each letter
        # sort and compare by character
        return sorted(s) == sorted(t)