class Solution:
    def romanToInt(self, s: str) -> int:

        # M > D > C > L > X > V > I (for reference)
        # Largest to smallest: add them up
        # Smallest to largest: subtract smaller 

        # hashmap (dictionary)
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0      # to store final converted integer value, initialized at 0

        # looping through each character s[i] in input roman string: 
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result = result - roman[s[i]]
            else:
                result = result + roman[s[i]]   # if not small, simply add the no. to result and move forward.
        
        return result

        # Condition1: i + 1 < len(s), this ensures that there is next character to compare with string s. This ensures that we don't try to access an index out of string which will cause error.

        # Condition2: roman[s[i]] < roman[s[i + 1]], this check if the value of the current roman numeral s[i] is less than the value of next roman numeral s[i + 1]. If it is true, it means current numeral is part of subtractive pair( IV, IX, XL ).

        # Time: O(n)
        # Space: O(1)