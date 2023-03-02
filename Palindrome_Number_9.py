'''
Created on Jul 12, 2015

@author: ljiang

Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ math https://leetcode.cn/problems/palindrome-number/solution/dong-hua-hui-wen-shu-de-san-chong-jie-fa-fa-jie-ch/ """
        if x < 0:
            return False
        remaining_digits_to_compare = 1
        tmp = x
        while tmp:
            tmp //= 10
            remaining_digits_to_compare *= 10
        remaining_digits_to_compare //= 10
        # print(div)
        while remaining_digits_to_compare > 0:
            # 得到最左
            left = x // remaining_digits_to_compare
            # 得到最右
            right = x % 10
            if left != right:
                return False
            # 去掉最左
            x %= remaining_digits_to_compare
            # 去掉最右
            x //= 10
            remaining_digits_to_compare //= 100
        return True
        '''
        上面这种方法可以解决 从 一个数 最低位 -> 最高位，最高位 -> 最低位 print 每一位
        remaining_digits_to_compare = 1
        tmp = x
        while tmp:
            tmp //= 10
            remaining_digits_to_compare *= 10
        remaining_digits_to_compare //= 10
        # print(div)
        while remaining_digits_to_compare > 0:
            # 得到最左
            left = x // remaining_digits_to_compare
            # 得到最右
            right = x % 10
            print('left: ', left, 'right: ', right)
            # 去掉最左
            x %= remaining_digits_to_compare
            # 去掉最右
            x //= 10
            remaining_digits_to_compare //= 100
        '''
        

        # 下面是我第一次try，不efficient
        if x < 0:
            return False
        digits = -1
        tmp = x
        while tmp:
            tmp //= 10
            digits += 1
        # print(digits)
        while x >= 10:
            high_digit = 10 ** digits
            # 得到最左
            left = x // high_digit
            # 去掉最左
            x %= high_digit
            # print('x: ', x)
            # x 的 位数
            tmp = x
            x_digits = 0
            while tmp:
                x_digits += 1
                tmp //= 10
            # print('x_digits: ', x_digits)
            # 得到最右
            right = x % 10
            # 去掉最右
            x //= 10
            if left != right:
                return False
            # 左侧0 的位数
            zero_digits = digits - x_digits
            # print('zero_digits: ', zero_digits)
            # match high digit 位数 与 x 位数
            digits -= 2
            while zero_digits:
                # 得到最右
                right = x % 10
                # print('right: ', right)
                if right != 0:
                    return False
                # 去掉最右
                x //= 10
                digits -= 2
                zero_digits -= 1
        return True


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        """ string solution """
        """
        x_str = str(x)
        reversed_x_str = str(x)[::-1]
        return x_str == reversed_x_str
        """
        x_str = str(x)
        left = 0
        right = len(x_str) - 1
        while left < right:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        return True


class SolutionTwo:
    """ compare right half of number
    
    check https://leetcode-cn.com/problems/palindrome-number/solution/dong-hua-hui-wen-shu-de-san-chong-jie-fa-fa-jie-ch/
    """
    def isPalindrome(self, x: int) -> bool:
        # 末尾为 0 就可以直接返回 false
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        # reverse right half of num to compare
        half_reversed_x = 0
        while x > half_reversed_x:
            half_reversed_x = half_reversed_x * 10 + x % 10
            x //= 10
        return x == half_reversed_x or x == half_reversed_x // 10


class SolutionOne:
    def isPalindrome(self, x: int) -> bool:
        """ Mathmatical solution
        https://leetcode-cn.com/problems/palindrome-number/solution/dong-hua-hui-wen-shu-de-san-chong-jie-fa-fa-jie-ch/
        """
        if x < 0:
            return False
        div = 1
        while x // div >= 10:
            div *= 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x - left * div - right) // 10
            div //= 100
        return True




class Palindrome_Number_19(object):
    def __init__(self,num):
        self.num=num
    def palindrome_number(self):
        original_num=self.num
        if self.num<0:
            return False
        reversed_integer=0
        while self.num!=0:
            reversed_integer=self.num%10+reversed_integer*10
            self.num=self.num/10
        if original_num==reversed_integer:
            return True
        else:
            return False
    def palindrome_number_2(self):
        if self.num<0:
            return False
        div=1
        while self.num/div>=10:
            div*=10
        while self.num!=0:
            first_digit=self.num/div
            last_digit=self.num%10
            if first_digit!=last_digit:
                return False
            self.num=(self.num%div)/10
            div/=100
        return True
  