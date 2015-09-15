'''
Created on Jul 6, 2015

@author: ljiang
Given a number represented as an array of digits, plus one to the number.

'''
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
    