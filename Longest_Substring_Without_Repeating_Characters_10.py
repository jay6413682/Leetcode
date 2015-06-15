'''
Created on Jun 11, 2015

@author: ljiang

Given a string, find the length of the longest substring without repeating characters. 
'''
class Longest_Substring_Without_Repeating_Characters_10:
    def __init__(self):
        pass
    
    def Longest_Substring_Without_Repeating_Characters(self,strg):
        max_sub_string=""
        i=0
        max_len=0
        while i <len(strg):
            if strg[i] in max_sub_string:
                strg=strg.replace(max_sub_string[:max_sub_string.index(strg[i])+1],'',1)
                i=0#max_sub_string.index(strg[i])+1
                max_sub_string=strg[i]
            else:
                max_sub_string+=strg[i]
                if len(max_sub_string)>max_len:
                    max_len=len(max_sub_string)                
            i+=1

            
        return max_len
    
    
    def Longest_Substring_Without_Repeating_Characters_2(self,strg):
        i=0
        j=0
        max_sub_string=""
        max_len=0
        while i<len(strg):
            if strg[i] in max_sub_string:
                j+=max_sub_string.index(strg[i])+1
                i=j
                max_sub_string=strg[j]
            else:
                max_sub_string=strg[j:i+1]
                if len(max_sub_string)>max_len:
                    max_len=len(max_sub_string) 
            i+=1
                
        
        return max_len
        