'''
Created on Jul 21, 2015

@author: ljiang
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples. [1,3,5,6],5->2 [1,3,5,6], 2->1 [1,3,5,6], 7->4 [1,3,5,6], 0->0

'''

class Search_Insert_Position_48:
    def __init__(self,lst,target):
        self.lst=lst
        self.target=target
    def search_and_insert(self):
        pass
        left=0
        right=len(self.lst)-1
        mid=(left+right)/2
        
        while left<right:
            if self.lst[mid] == self.target:
                return mid
            elif self.target<self.lst[mid]:
                right=mid
            elif self.target>self.lst[mid]:
                left=mid+1
            mid=(left+right)/2
                
        if self.lst[mid]>self.target:
            return mid
        else:
            return mid+1
            
                
            