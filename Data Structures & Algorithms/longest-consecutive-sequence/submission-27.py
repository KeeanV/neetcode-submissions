class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for i in my_set:
            curr_length = 1
            if i-1 not in my_set:
                curr = i
                while curr+1 in my_set:
                    curr +=1
                    curr_length +=1
                longest = max(longest, curr_length)
        return longest