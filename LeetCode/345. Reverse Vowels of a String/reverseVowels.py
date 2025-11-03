class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)

        i, j = 0 , len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels: 
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)



# Test Cases
solution = Solution()
print(solution.reverseVowels("IceCreAm"))
print(solution.reverseVowels("leetcode"))