class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        my_set = set(nums)
        for i in my_set:
            if i-1 not in my_set:
                curr = i
                streak = 1
                while curr+1 in my_set:
                    curr +=1
                    streak+=1
                longest = max(longest, streak)
        return longest
                