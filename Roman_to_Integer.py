class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i + 1 < len(s) and s[i + 1] == "V":
                    total += roman_to_int['V'] - roman_to_int['I']
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == "X":
                    total += roman_to_int['X'] - roman_to_int['I']
                    i += 2
                else:
                    total += roman_to_int['I']
                    i += 1
            elif s[i] == "V":
                total += roman_to_int['V']
                i += 1
            elif s[i] == "X":
                if i + 1 < len(s) and s[i + 1] == "L":
                    total += roman_to_int['L'] - roman_to_int['X']
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == "C":
                    total += roman_to_int['C'] - roman_to_int['X']
                    i += 2
                else:
                    total += roman_to_int['X']
                    i += 1
            elif s[i] == "L":
                total += roman_to_int['L']
                i += 1
            elif s[i] == "C":
                if i + 1 < len(s) and s[i + 1] == "D":
                    total += roman_to_int['D'] - roman_to_int['C']
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == "M":
                    total += roman_to_int['M'] - roman_to_int['C']
                    i += 2
                else:
                    total += roman_to_int['C']
                    i += 1
            elif s[i] == "D":
                total += roman_to_int['D']
                i += 1
            elif s[i] == "M":
                total += roman_to_int['M']
                i += 1
        return total

test0 = "III"
test1 = "LVIII"
test2 = "MCMXCIV"
print(Solution().romanToInt(test0))
print(Solution().romanToInt(test1))
print(Solution().romanToInt(test2))
