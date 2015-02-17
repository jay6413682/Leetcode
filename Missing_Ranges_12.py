'''
Created on Jul 6, 2015

@author: ljiang


Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return ["2", "4->49", "51->74", "76->99"]

'''


def _get_range(left: int, right: int) -> list:
    return '{}->{}'.format(left, right) if left < right else str(left)


def missing_range(nums: list, start: int, end: int) -> list:
    """ https://www.lintcode.com/problem/missing-ranges/description """
    s = start - 1
    e = end + 1
    new_nums = [s] + nums + [e]
    rng = []
    for i, cur_val in enumerate(new_nums):
        if i == 0:
            continue
        if cur_val - new_nums[i - 1] >= 2:
            rng.append(_get_range(new_nums[i - 1] + 1, cur_val - 1))
    return rng


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
            
            
        