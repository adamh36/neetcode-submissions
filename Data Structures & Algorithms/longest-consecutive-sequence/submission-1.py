class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(1) lookup and removes duplicates
        longest = 0  # tracks the longest count found so far

        for num in num_set:
            if (num - 1) not in num_set:  # only start at the beginning of a sequence
                current_num = num
                length = 1  # this sequence has at least 1 number

                while (current_num + 1) in num_set:  # keep going while next number exists
                    current_num += 1
                    length += 1  # increment count instead of appending to a list

                longest = max(longest, length)  # update if this sequence is longer

        return longest
