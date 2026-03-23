from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output = 0
        
        for i in range(0, len(points) - 1):
            diff_x = points[i + 1][0] - points[i][0]
            diff_y = points[i + 1][1] - points[i][1]
            output += max(abs(diff_x), abs(diff_y))

        return output
        


solution = Solution()
print(solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))