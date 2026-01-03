class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        lst = list(s)
        len_lst = len(lst)
        total = 0
        i = 0

        while i < len_lst:
            if i < len_lst - 1:
                if lst[i] == 'I' and lst[i + 1] == 'V':
                    total += 4
                    i += 2
                    continue
                elif lst[i] == 'I' and lst[i + 1] == 'X':
                    total += 9
                    i += 2
                    continue
                elif lst[i] == 'X' and lst[i + 1] == 'L':
                    total += 40
                    i += 2
                    continue
                elif lst[i] == 'X' and lst[i + 1] == 'C':
                    total += 90
                    i += 2
                    continue
                elif lst[i] == 'C' and lst[i + 1] == 'D':
                    total += 400
                    i += 2
                    continue
                elif lst[i] == 'C' and lst[i + 1] == 'M':
                    total += 900
                    i += 2
                    continue

            total += roman_to_int[lst[i]]
            i += 1

        return total

solution = Solution()
print(solution.romanToInt("MCMXCIV"))