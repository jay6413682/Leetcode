'''
Created on Jul 12, 2015

@author: ljiang

Determine whether an integer is a palindrome. Do this without extra space.
'''
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
        