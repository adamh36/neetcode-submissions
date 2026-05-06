class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            value = target - nums[i]
            if value in hashmap:
                return [hashmap[value], i ]
            else:
                hashmap[nums[i]] = i
