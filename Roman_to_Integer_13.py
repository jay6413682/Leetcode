
class Solution:
    def romanToInt(self, s: str) -> int:
        """ https://leetcode-cn.com/problems/roman-to-integer/solution/yong-shi-9993nei-cun-9873jian-dan-jie-fa-by-donesp/ """
        symbol_value_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        n = len(s)
        val_sum = 0
        if i == 1:
            return symbol_value_map[s]
        while i < n - 1:
            symbol, next_symbol = s[i], s[i + 1]
            val = symbol_value_map[symbol]
            next_val = symbol_value_map[next_symbol]
            if val < next_val:
                val_sum -= val
            else:
                val_sum += val
            i += 1
        val_sum += symbol_value_map[s[i]]
        return val_sum


class Solution2:
    def romanToInt(self, s: str) -> int:
        """ https://leetcode-cn.com/problems/roman-to-integer/solution/hua-jie-suan-fa-13-luo-ma-shu-zi-zhuan-zheng-shu-b/ there is some error in the mapping, but fixed below """
        roman_int_map = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        i = 0
        n = len(s)
        res = 0
        while i < n:
            if i != n - 1 and s[i:i + 2] in roman_int_map:
                res += roman_int_map[s[i:i + 2]]
                i += 2
            else:
                res += roman_int_map[s[i]]
                i += 1
        return res
