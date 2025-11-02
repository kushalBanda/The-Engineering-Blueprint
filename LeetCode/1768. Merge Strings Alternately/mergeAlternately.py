class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        minLen = min(len(word1), len(word2))
        for i in range(minLen):
            merged+= word1[i]
            merged+= word2[i]

        merged.append(word1[minLen:])
        merged.append(word2[minLen:])

        return "".join(merged)


# Test Cases
solution = Solution()
print(solution.mergeAlternately("ab", "pqrs"))
