from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)

solution = Solution()
print(solution.majorityElement([3,2,3]))    