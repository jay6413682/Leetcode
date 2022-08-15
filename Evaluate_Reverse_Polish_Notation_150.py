from math import ceil, floor
from typing import List
from _collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """ 递归，我自己的解法，效率很低 """
        if len(tokens) == 1:
            return int(tokens[0])
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in ('+', '-', '*', '/'):
                token_1 = tokens.pop(i - 2)
                token_2 = tokens.pop(i - 2)
                if token == '+':
                    result = int(token_1) + int(token_2)
                elif token == '-':
                    result = int(token_1) - int(token_2)
                elif token == '*':
                    result = int(token_1) * int(token_2)
                elif token == '/':
                    result = int(int(token_1) / int(token_2))
                tokens[i - 2] = str(result)
                return self.evalRPN(tokens)
            i += 1


class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        """ stack solution:
        https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/solution/150-ni-bo-lan-biao-da-shi-qiu-zhi-zhan-de-jing-dia/ 动画
        """
        stack = deque()
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                right_val = stack.pop()
                left_val = stack.pop()
                if token == '+':
                    result = left_val + right_val
                elif token == '-':
                    result = left_val - right_val
                elif token == '*':
                    result = left_val * right_val
                elif token == '/':
                    result = int(left_val / right_val)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
        '''
        # my another try
        stack = deque()
        for t in tokens:
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            else:
                num_right = stack.pop()
                num_left = stack.pop()
                if t == '+':
                    stack.append(num_left + num_right)
                elif t == '/':
                    d = num_left / num_right
                    if d < 0:
                        d = ceil(d)
                    else:
                        d = int(d)
                    stack.append(d)
                elif t == '*':
                    stack.append(num_left * num_right)
                else:
                    stack.append(num_left - num_right)
            # print(stack)
        return stack.pop()
    
