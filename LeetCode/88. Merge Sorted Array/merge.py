from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        combinedList = nums1[:m] + nums2[:n] 
        nums1[:] = sorted(combinedList)    
        return nums1
        
solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))