'''
Created on Jun 11, 2015

@author: ljiang
Validate if a given string is numeric.
'''
class valid_number_9:
    def __init__(self):
        pass
    def valid_num(self,num):
        num=num.strip(" ")
        dot_count=0
        #sign=0
        if num=="":
            return False
        elif num=='.':
            return False
        elif num[0]=='+' or num[0]=='-':
            num=num.lstrip(num[0])
        for i in num:
            if i=='.':
                dot_count+=1
                if dot_count>1:
                    return False
            if not (i.isdigit() or i=='.'):
                return False            
        return True
                