from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            print(num, count)
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

solution = Solution()
print(solution.majorityElement([3,2,3]))    