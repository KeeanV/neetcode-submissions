class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       longest = 0
       my_set = set(nums)
       for i in my_set:
        if i -1 not in my_set: 
            current = i
            streak = 1
            while current+1 in my_set:
                streak+=1
                current +=1
            longest = max(longest, streak)
       return longest