class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # convert nums to a set for O(1) lookup and to remove duplicates
        longest_seq = []  # tracks the longest consecutive sequence found so far

        for num in num_set:  # loop through each unique number in the set
            if (num - 1) not in num_set:  # only start counting if this is the START of a sequence
                # we know it's a start because the number before it doesn't exist in the set
                current_num = num  # begin the sequence at this number
                current_seq = [current_num]  # initialize the sequence with the starting number

                # build the sequence upward by checking if the next number exists
                
                while (current_num + 1) in num_set:  # keep going as long as the next number is in the set
                    current_num += 1  # move to the next consecutive number
                    current_seq.append(current_num)  # add it to the current sequence

                # check if this sequence is the longest we have seen so far
                if len(current_seq) > len(longest_seq):
                    longest_seq = current_seq  # update the record holder

        return len(longest_seq)  # return the length of the longest consecutive sequence found
