'''
Created on Jul 12, 2015

@author: ljiang

Determine whether an integer is a palindrome. Do this without extra space.
'''

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
        