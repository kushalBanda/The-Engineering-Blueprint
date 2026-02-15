from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []
        for i in nums: 
            if new_nums.count(i) < 2:
                new_nums.append(i)
        nums[:] = new_nums
        return len(nums)