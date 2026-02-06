from typing import List 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums: 
            seen[num] = seen.get(num, 0) + 1
        for num, count in seen.items():
            if count == 1:
                return num

solution = Solution()
print(solution.singleNumber([4,1,2,1,2]))