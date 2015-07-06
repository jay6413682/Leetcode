'''
Created on Jul 6, 2015

@author: ljiang

Reverse digits of an integer. For example: x = 123, return 321. 

'''
from sys import maxint
class Reverse_Integer_17:
    def __init__(self,intg):
        self.intg=intg
        
    def Reverse_Integer(self):
        reversed_int=0
        while(self.intg!=0):

            if self.intg>0:
                reversed_int=reversed_int*10+self.intg%10
            elif self.intg<0:
                reversed_int=reversed_int*10-(-1*self.intg)%10
            if reversed_int>maxint or reversed_int<-1*maxint-1:
                return 0
            if self.intg>0:
                self.intg=int(self.intg/10)
            elif self.intg<0:
                self.intg=-1*int(-1*self.intg/10)
        return reversed_int