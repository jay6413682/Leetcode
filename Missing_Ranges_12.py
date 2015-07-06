'''
Created on Jul 6, 2015

@author: ljiang


Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return ["2", "4->49", "51->74", "76->99"]

'''
class Missing_Ranges_12:
    def __init__(self,lst):
        self.lst=lst
    
    
    def Missing_Ranges(self):
        pass
        missing_range=[]
        self.lst.insert(0, -1)
        self.lst.append(100)
        for i in xrange(len(self.lst)-1):
            if self.lst[i+1]-self.lst[i]==2:
                missing_range.append(str(self.lst[i]+1))
            elif self.lst[i+1]-self.lst[i]>2:
                missing_range.append(str(self.lst[i]+1)+"->"+str(self.lst[i+1]-1))
        return missing_range
            
            
        