class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort all strings
        # keep hashmap of keys and values
        my_map = {}
        for s in strs:
            sorty = ''.join(sorted(s)) # needs to be immutable so either tuple() or string
            if sorty not in my_map:
                my_map[sorty] = []
            my_map[sorty].append(s)
        result = []
        for key, val in my_map.items():
            result.append(val)
        return result