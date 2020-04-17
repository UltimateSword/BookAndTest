class Solution:

    def romanToInt(self, s: str) -> int:
        hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XC': 90,
            'XL': 40,
            "CM": 900,
            "CD": 400,
        }
        result = 0
        i = 0
        while i < len(s):
            one = s[i:i+2]
            if one in hash:
                result += hash[one]
                i += 2
            else:
                result += hash[s[i]]
                i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("LVIII"))