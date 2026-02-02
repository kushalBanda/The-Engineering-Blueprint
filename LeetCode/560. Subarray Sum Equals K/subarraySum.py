from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}

        for i, num in enumerate(nums):
            print(f"\nIndex {i}")
            print(f"Before: prefix_sum = {prefix_sum}")

            prefix_sum += num
            print(f"After adding {num}: prefix_sum = {prefix_sum}")

            needed = prefix_sum - k
            print(f"Looking for prefix_sum - k = {needed}")

            if needed in prefix_count:
                count += prefix_count[needed]
                print(f"Found {prefix_count[needed]} match(es), count = {count}")

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
            print(f"prefix_count = {prefix_count}")

        return count


solution = Solution()
print("\nFinal Count:", solution.subarraySum([1,1,1], 2))
