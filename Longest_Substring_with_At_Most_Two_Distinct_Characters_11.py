'''
Created on Jun 16, 2015

@author: ljiang

Given a string S, find the length of the longest substring T that contains at most two distinct characters.

'''


def longest_substring_with_at_most_n_distinct_characters(s: str, n: int) -> int:
    """ This is equivalent to 904. Fruit Into Baskets
    https://leetcode.com/problems/fruit-into-baskets/
    """
    char_count_mapping = {}
    substr_start = 0
    max_len = 0
    for i, chrt in enumerate(s):
        if chrt not in char_count_mapping:
            char_count_mapping[chrt] = 1
        else:
            char_count_mapping[chrt] += 1
        if len(char_count_mapping) > n:
            max_len = max_len if max_len > i - substr_start else i - substr_start
            while substr_start < i:
                char_count_mapping[s[substr_start]] -= 1
                if char_count_mapping[s[substr_start]] == 0:
                    del char_count_mapping[s[substr_start]]
                    substr_start += 1
                    break
                substr_start += 1
        else:
            max_len = max_len if i - substr_start + 1 < max_len else i - substr_start + 1
    return max_len




class Longest_Substring_with_At_Most_Two_Distinct_Characters_11:
    def __init__(self):
        pass
    
    def Longest_Substring_with_At_Most_Two_Distinct_Characters(self,strg):
        i=0        
        max_len=0
        while i<len(strg):
            j=0
            while j<len(strg):
                substr=strg[i:j+1]
                if len(set(substr))<=2 and len(substr)>max_len:
                    max_len=len(substr)
                j+=1
            i+=1
            
        return max_len
    
    def Longest_Substring_with_At_Most_Two_Distinct_Characters_2(self,strg):
        i=0
        j=0
        max_len=1
        while i<=j and j<len(strg):
            substr=strg[i:j+1]
            if len(set(substr))<=2:
                if len(substr)>max_len:
                    max_len=len(substr)
                j+=1
                
            else:
                i+=1
                
        return max_len
    
    def Longest_Substring_with_At_Most_Two_Distinct_Characters_3(self,s):
        i = 0
        j = -1
        maxLen = 0
        for k in xrange(1,len(s)):
            if (s[k] == s[k - 1]):
                continue
            if (j >= 0 and s[j] != s[k]):
                if k-i>maxLen:
                    maxLen=k-i
                i = j + 1 
            j = k - 1
        if maxLen==0:
            maxLen=len(s)
            
        return maxLen
    