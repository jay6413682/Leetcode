'''
Created on Jul 23, 2015

@author: ljiang
'''
class LongestIncreasingSubsequence:
    def __init__(self,lst):
        self.lst=lst
    def find_len_lis(self):
        len_inc_seq={}
        len_inc_seq[0]=1
        max=1
        for i in xrange(0,len(self.lst)):
            len_inc_seq[i]=1
            for j in xrange(i-1,-1,-1):
                if self.lst[i]>self.lst[j] and len_inc_seq[j]+1>len_inc_seq[i]:
                    len_inc_seq[i]=len_inc_seq[j]+1
                    if len_inc_seq[i]>max:
                        max=len_inc_seq[i]
        return max