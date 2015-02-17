'''
Created on Jul 16, 2015

@author: ljiang

Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        """ 贪心算法: https://zhuanlan.zhihu.com/p/53334049
        解：https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcod-75rs/
        复杂度分析

        时间复杂度：O(1)O(1)。由于有一组有限的罗马数字，循环可以迭代多少次有一个硬上限。因此，我们说时间复杂度是常数的，即 O(1)O(1)。
        空间复杂度：O(1)O(1)，使用的内存量不会随输入整数的大小而改变，因此是常数的。

        """
        """
        # only >python3.5 dict 有序
        int_to_roman_map = {
            1000: 'M',
            900: "CM",
            500: 'D',
            400: "CD",
            100: 'C',
            90: "XC",
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        """
        int_to_roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman = ''
        for i, r in int_to_roman_map:
            if num == 0:
                break
            multiplier = num // i
            num %= i
            roman += r * multiplier
        '''
        # another less efficient way
        for i, r in int_to_roman_map:
            while num >= i:
                num -= i
                roman += r
        return roman
        '''
        return roman


class Solution2:
    def intToRoman(self, num: int) -> str:
        """
        https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcode/
        复杂度分析

        时间复杂度：O(1)O(1)。无论输入的大小，都会执行相同数量的操作。因此，时间复杂度是常数的。
        空间复杂度：O(1)O(1)，虽然我们使用数组，但不管输入的大小，它们都是相同的大小。因此，它们是常数级空间。
        这种方法的缺点是，如果要扩展罗马数字，它是不灵活的（这是一个有趣的后续问题）。例如，如果我们说符号 H 现在表示 5000，而 P 现在表示 10000，允许我们表示多达 39999 的数字，会怎么样？方法 1 修改起来要快得多，因为您只需要将这两个值添加到代码中，而不需要进行任何计算。但是对于方法 2，您需要计算并硬编码 10 个新的表示。如果我们再加上一些符号就能达到 39999999 呢？方法2变得越来越难管理，我们添加的符号越多。

        """
        thousands = ['', 'M', 'MM', 'MMM']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens =['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        th = num // 1000
        # h = (num - th * 1000) // 100
        h = (num % 1000) // 100
        # te = (num - th * 1000 - h * 100) // 10
        te = (num % 1000 % 100) // 10
        # o = (num - th * 1000 - h * 100 - te * 10) // 1
        o = (num % 1000 % 100 % 10) // 1
        return thousands[th] + hundreds[h] + tens[te] + ones[o]


class Integer_to_Roman_36:
    def __init__(self,num):
        self.num=num
        self.dic={1000:"M", 900:"CM", 500:"D", 400:"CD",100:"C",  90:"XC",  50:"L",  40:"XL",10:"X",   9:"IX",   5:"V",   4:"IV",1:"I" }
    
    def itor(self):
        pass
        roman=""
        for k in sorted(self.dic.keys(),reverse=True):
            msb=self.num/k
            if msb>0:
                for j in xrange(msb):
                    roman+=self.dic[k]
                    self.num-=k
        return roman
            