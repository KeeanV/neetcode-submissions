class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count frequencies of each letter
        # sort and compare by character
        if len(s) != len(t):
            return False
        my_map = defaultdict(int)
        for c in s:
            my_map[c] += 1
        for c in t:
            my_map[c] -= 1
            if my_map[c] < 0:
                return False
        return True