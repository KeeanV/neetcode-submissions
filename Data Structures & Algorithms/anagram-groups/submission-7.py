class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for s in strs:
            sorty = tuple(sorted(s))
            if sorty in my_map:
                my_map[sorty].append(s)
            else:
                my_map[sorty] = [s]
        result = []
        for s in my_map.values():
            result.append(s)
        return result