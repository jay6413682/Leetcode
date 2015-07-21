'''
Created on Jul 16, 2015

@author: ljiang

Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Integer_to_Roman_36:
    def __init__(self,num):
        self.num=num
        self.dic={1000:"M", 900:"CM", 500:"D", 400:"CD",100:"C",  90:"XC",  50:"L",  40:"XL",10:"X",   9:"IX",   5:"V",   4:"IV",1:"I" }
    
    def itor(self):
        pass
        roman=""
        for k in sorted(self.dic.keys(),reverse=True):
            msb=self.num/k
            if msb>0:
                for j in xrange(msb):
                    roman+=self.dic[k]
                    self.num-=k
        return roman
            