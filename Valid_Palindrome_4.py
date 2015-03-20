'''
Created on Mar 19, 2015

@author: ljiang

Question:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.
Example Questions Candidate Might Ask:
Q: What about an empty string? Is it a valid palindrome?
A: For the purpose of this problem, we define empty string as valid palindrome.

'''
class ValidPalindrome:
    def __init__(self,st):
        self.st=st
        
    def isPalindrome(self):
        i=0
        j=len(self.st)-i-1
        if len(self.st)==0:
            return True
        else:
            while i<j:
                if not(self.st[i].isalpha()):
                    i+=1
                    continue
                if not(self.st[j].isalpha()):
                    j-=1
                    continue
                if self.st[i].lower()==self.st[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
            return True
                