from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for j, num in enumerate(nums):
            if num not in hashMap:
                hashMap[num] = j
            else:
                if abs(j - hashMap[num]) <= k:
                    return True
                hashMap[num] = j
        return False

solution = Solution()
# print(solution.containsNearbyDuplicate([1,2,3,1], 3))
# print(solution.containsNearbyDuplicate([1,0,1,1], 1))
# print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))