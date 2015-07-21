'''
Created on Jul 14, 2015

@author: ljiang
Given an array of integers, every element appears twice except for one. Find that single one.

'''
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
            
        