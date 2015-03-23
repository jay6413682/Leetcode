'''
Created on Mar 19, 2015

@author: ljiang
'''
class Str_Str_5:
    def __init__(self,needle,haystack):
        self.needle=needle
        self.haystack=haystack
        
    def strStr(self):
        if len(self.needle)>10 or len(self.haystack)>10:
            return False
        if len(self.needle)==0:
            return 0
        if len(self.haystack)==0 and len(self.needle)==0:
            return 0     
        i=0
        j=0
        haystack_height=[]
        while i<len(self.haystack):
            while j<len(self.needle):
                if self.needle[j]!=self.haystack[i]:
                    break
                else:
                    j+=1
                    haystack_height.append(i)
                    break
            i+=1
        if len(haystack_height)!=len(self.needle):
            return False
        else:
            for i in xrange(0,len(haystack_height)-1):
                if haystack_height[i]-haystack_height[i+1]!=-1:
                    return False
            else:
                return haystack_height[0]
            
                             

                    