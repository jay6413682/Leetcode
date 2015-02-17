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


def is_palindrome(strn):
    left = 0
    right = len(strn) - 1
    while left <= right:
        if not strn[left].isalpha():
            left += 1
            continue
        elif not strn[right].isalpha():
            right -= 1
            continue
        elif strn[left].lower() != strn[right].lower():
            return False
        left += 1
        right -= 1
    return True
