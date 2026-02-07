class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        longestSubstring = []

        for i in s:
            if i in longestSubstring:
                longestSubstring = longestSubstring[longestSubstring.index(i) + 1:]
            longestSubstring.append(i)
            output = max(output, len(longestSubstring))
        return output

solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))