from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        return max(hashMap, key=hashMap.get)

solution = Solution()
print(solution.majorityElement([3,2,3]))