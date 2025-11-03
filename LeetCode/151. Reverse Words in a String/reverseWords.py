class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        newStr = s.split(" ")
        newStr = [word for word in newStr if word != ""] 
        
        return " ".join(newStr[::-1])


solution = Solution()
print(solution.reverseWords("the sky is blue"))
print(solution.reverseWords("  hello world  "))