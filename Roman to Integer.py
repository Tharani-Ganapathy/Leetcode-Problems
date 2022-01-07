class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        length = len(s)


        for i in range(length):
            if i != length-1:
                if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                    result += roman_dict[s[i]]
                else:
                    result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        return result
