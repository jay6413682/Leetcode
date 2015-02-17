'''
Created on Jul 6, 2015

@author: ljiang
Given a number represented as an array of digits, plus one to the number.

'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        recursive solution
        """
        n = len(digits)
        # last digit
        if digits[n - 1] != 9:
            digits[n - 1] += 1
        else:
            digits[n - 1] = 0
            if n > 1:
                # https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
                # slicing allows Replace and Resize part of the list
                digits[:n - 1] = self.plusOne(digits[:n - 1])
            else:
                digits.insert(0, 1)
        return digits


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        """ iterative/math
        https://leetcode-cn.com/problems/plus-one/solution/java-shu-xue-jie-ti-by-yhhzw/
        https://leetcode-cn.com/problems/plus-one/solution/hua-jie-suan-fa-66-jia-yi-by-guanpengchn/ 
        """
        i = len(digits) - 1
        carry = 0
        while i >= 0:
            # last digit
            if i == len(digits) - 1 or carry == 1:
                temp = digits[i] + 1
                if temp == 10:
                    carry = 1
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                return digits
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits


from copy import deepcopy
class Plus_One_18:
    def __init__(self):
        pass
    
    #tail recursive way, inefficient
    def Plus_One(self,lst,plusone):
        new_lst=[]
        if len(lst)==1 and lst[0]==9:
            return [1,0]
        for i in xrange(len(lst)):
            if i==len(lst)-1:
                new_lst.append(lst[i])
                new_lst[i]=lst[i]+1
                if new_lst[i]==10:
                    new_lst[i]=0
                    plusone=1
                if plusone==1:
                    new_lst[:len(new_lst)-1]=self.Plus_One(new_lst[:len(new_lst)-1],0)
                break
            new_lst.append(lst[i])
        return new_lst
    
    #iteration way
    def Plus_One_2(self,lst):
        new_lst=deepcopy(lst)
        for i in xrange(len(lst)-1,-1,-1):
            if i==len(lst)-1:
                new_lst[i]+=1
            if new_lst[i]==10:
                if i==0:
                    new_lst.insert(0,1)
                    new_lst[1]=0
                else:
                    new_lst[i-1],new_lst[i]=new_lst[i-1]+1,0

        return new_lst    
    
    def Plus_One_3(self,lst):
        new_num=0
        new_lst=[]
        for i in xrange(len(lst)):
            new_num=new_num*10+lst[i]
            if i==len(lst)-1:
                new_num+=1
        while new_num!=0:
            new_lst.insert(0, new_num%10)
            new_num=new_num/10
        return new_lst


    def Plus_One_4(self,lst):
        new_lst=deepcopy(lst)
        if len(new_lst)==1 and new_lst[0]==9:
            return [1,0]
        
        for i in xrange(len(lst)-1,-1,-1):
            if i==len(lst)-1:
                new_lst[i]+=1
            if new_lst[i]==10:
                new_lst[i]=0
                new_lst[:i]=self.Plus_One_4(lst[:i])

        return new_lst    
    
    def Plus_One_5(self,lst):
        for i in xrange(len(lst)-1,-1,-1):
            if lst[i]<9:
                lst[i]=lst[i]+1
                return lst
            else:
                lst[i]=0
        lst.append(0)
        lst[0]=1
        return lst
    