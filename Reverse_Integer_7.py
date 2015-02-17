'''
Created on Jul 6, 2015

@author: ljiang

Reverse digits of an integer. For example: x = 123, return 321. 

'''


class Solution:
    def reverse(self, x: int) -> int:
        """
        讲解：https://leetcode-cn.com/problems/reverse-integer/solution/tu-jie-7-zheng-shu-fan-zhuan-by-wang_ni_ma/
        综合https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/ 的解
        时间复杂度：O(\log |x|)O(log∣x∣)。翻转的次数即 xx 十进制的位数。
        空间复杂度：O(1)O(1)。
        """
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 - 1
        res = 0
        while x:
            # digit 是 正数
            if x < 0:
                digit = -x % 10
            else:
                digit = x % 10
            # print(digit, x)
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > MAX_INT % 10):
                return 0
            if res < MIN_INT // 10 + 1 or (res == MIN_INT // 10 + 1 and digit > -MIN_INT % 10):
                return 0
            if x < 0:
                res = res * 10 - digit
                x = (x + digit) // 10
            else:
                res = res * 10 + digit
                x //= 10
        return res


class SolutionTwo:
    """ Solving with string
    https://leetcode-cn.com/problems/reverse-integer/solution/pythondan-chu-he-tui-ru-shu-zi-yi-chu-qian-jin-xin/
    """
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        reversed_str_x = ''
        if str_x.startswith('-'):
            reversed_str_x += '-'
        n = len(str_x)
        i = n - 1
        non_zero_char_seen = False
        while i >= 0:
            if non_zero_char_seen is False and str_x[i] == '0':
                i -= 1
                continue
            elif str_x[i] == '-' or str_x[i] == '+':
                i -= 1
                continue
            non_zero_char_seen = True
            reversed_str_x += str_x[i]
            i -= 1
        reversed_x = int(reversed_str_x)
        if abs(reversed_x) > (2**31 - 1):
            return 0
        return reversed_x
        """
        # simpler solution:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0

        """


from sys import maxint
class Reverse_Integer_17:
    def __init__(self,intg):
        self.intg=intg
        
    def Reverse_Integer(self):
        reversed_int=0
        while(self.intg!=0):

            if self.intg>0:
                reversed_int=reversed_int*10+self.intg%10
            elif self.intg<0:
                reversed_int=reversed_int*10-(-1*self.intg)%10
            if reversed_int>maxint or reversed_int<-1*maxint-1:
                return 0
            if self.intg>0:
                self.intg=int(self.intg/10)
            elif self.intg<0:
                self.intg=-1*int(-1*self.intg/10)
        return reversed_int