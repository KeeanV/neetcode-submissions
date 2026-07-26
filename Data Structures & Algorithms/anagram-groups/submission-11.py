class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for s in strs:
            sorty = tuple(sorted(s))
            my_map[sorty].append(s)
        return list(my_map.values())