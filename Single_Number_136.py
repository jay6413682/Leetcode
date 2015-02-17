'''
Created on Jul 14, 2015

@author: ljiang
Given an array of integers, every element appears twice except for one. Find that single one.

'''
class Solution2:
    """ 空间复杂度 o(n)太高
    https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
    """
    def singleNumber(self, nums: List[int]) -> int:
        non_dup_nums = []
        for num in nums:
            if num not in non_dup_nums:
                non_dup_nums.append(num)
            else:
                non_dup_nums.remove(num)
        return non_dup_nums[0]
        """
        non_dup_nums = set()
        for n in nums:
            if n not in non_dup_nums:
                non_dup_nums.add(n)
            else:
                non_dup_nums.remove(n)
        return non_dup_nums.pop()
        """
        

class Solution:
    """ 位运算 bit manipulation : https://www.cnblogs.com/Neeo/articles/10536202.html
    为什么反码解决了加减法运算问题 & 关于原码(true form)补码(two's complement)反码(inverse code)： https://www.cnblogs.com/zhxmdefj/p/10902322.html
    规律总结： https://leetcode-cn.com/leetbook/read/leetcode-cookbook/5c9u92/
    异或运算满足交换律和结合律: https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
    """
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for num in nums:
            temp ^= num
        return temp


class Single_Number_33:
    def __init__(self,lst):
        self.lst=lst
        
    def find_single_number(self):
        pass
        dic={}
        for i in self.lst:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for x in dic:
            if dic[x]==1:
                return x
    
    def find_single_number_2(self):
        pass
        single_lst=[]
        for i in self.lst:
            if i in single_lst:
                single_lst.remove(i)
                
            else:
                single_lst.append(i)
        return single_lst[0]
    
    def find_single_number_3(self):
        single_num=0
        for i in self.lst:
            single_num^=i
        return single_num
            
        