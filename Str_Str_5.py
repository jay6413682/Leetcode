'''
Created on Mar 19, 2015

@author: ljiang
'''

import itertools
class Str_Str_5:
    def __init__(self,needle,haystack):
        self.needle=needle
        self.haystack=haystack
    
    #brute force method 1, O(n^2)    
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
            
    #brute force 2; O(n^2)
    def strStr2(self):
        for i in itertools.count():
            for j in itertools.count():
                if j==len(self.needle):
                    return i
                if i+j==len(self.haystack):
                    return False
                if self.needle[j]!=self.haystack[i+j]:
                    break
    
    #brute force 4: O(n^2); the logic is almost the same as brute force 2
    def strStr5(self):
        for i in xrange(0,len(self.haystack)+1):
            for j in xrange(0,len(self.needle)+1):
                if j == len(self.needle):
                    return i
                if i+j==len(self.haystack):
                    return False

                if self.haystack[i+j]!=self.needle[j]:
                    break
               
        return False
                             
    #brute force 3; slice makes copies so the space complexity is high
    def strStr3(self):
        for i in xrange(0,len(self.haystack)-len(self.needle)+1):
            if self.haystack[i:i+len(self.needle)]==self.needle:
                return i
        return False
    
    #Rabin-Karp algorithm
    def strStr4(self):
        if len(self.needle)>10 or len(self.haystack)>10:
            return False
        if len(self.needle)==0:
            return 0
        if len(self.haystack)==0 and len(self.needle)==0:
            return 0     
        
        if len(self.haystack)<len(self.needle):
            return False
        def rollingHash(strg,length):
            hs=0
            for i in xrange(0,length):
                hs+=(255**i)*ord(strg[length-i-1])
            return hs
        
        def update(strg,hs,indx,length):
            if indx+length == len(strg):
                return
            y=ord(strg[indx])
            z=(255**(length-1))*y
            x=hs-z
            hs=x*255+ord(strg[indx+length])
            #hs=(hs-ord(strg[indx])*(255**(length-1)))*255+ord(strg[indx+length])
            return hs
                        
        needle_hash=rollingHash(self.needle, len(self.needle))
        haystack_hash=rollingHash(self.haystack, len(self.needle))
        length=len(self.needle)
        for j in xrange(0,len(self.haystack)-len(self.needle)+1):            
            if haystack_hash==needle_hash:
                return j
            haystack_hash=update(self.haystack,haystack_hash,j,length)        
        return False
            
        
                    