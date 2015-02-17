'''
Created on Jun 11, 2015

@author: ljiang
Validate if a given string is numeric.
'''

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        """ regex/regular expression/正则表达式：类似https://leetcode-cn.com/problems/valid-number/solution/java-zheng-ze-biao-da-shi-fang-fa-san-xi-vc9q/
        先画出dfa图，然后NFA/DFA -> regex: https://www.youtube.com/watch?v=UKYvP8aS7fM&ab_channel=EasyTheory
        GNFA and state elimination: https://condor.depaul.edu/glancast/444class/docs/lectures/lecOct02.html  
        """
        return re.fullmatch(r'(\+|-)?(\.\d+|\d+(\.\d*)?)([Ee](\+|-)?\d+)?', s) is not None


'''
def is_number(s: str) -> bool:
    """ regex solution """
    if re.match('^\s*[+-]?\d*\.?\d+(e[+-]?\d+)?\s*$', s) or re.match(
            '^\s*[+-]?\d+\.?\d*(e[+-]?\d+)?\s*$', s):
        return True
    return False
'''


class SolutionFour:
    def isNumber(self, s: str) -> bool:
        """
        dfa可以直接写 图：https://leetcode-cn.com/problems/valid-number/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-4/ 。 注意https://leetcode.com/problems/valid-number/discuss/23725/C%2B%2B-My-thought-with-DFA 图是错的
        正则表达式->dfa:  
        computer to do it:
        regex -> nfa : https://www.youtube.com/watch?v=RYNN-tb9WxI&ab_channel=BarryBrown (注意讲解有错For A*,  ε returns from state 3 to state 2. 比如：https://www.youtube.com/watch?v=v4vo1uKSMII&ab_channel=MiftaSintaha 2:46的公式，另外enfa VS nfa)
        nfa -> dfa: https://www.youtube.com/watch?v=taClnxU-nao&ab_channel=BarryBrown 
        regex -> dfa: https://www.youtube.com/watch?v=dlH2pIndNrU&ab_channel=BarryBrown (注意讲解有错it should be 4 to 3 using epsilon not 5 to 3)

        一些其他内容：
        regex -> fsa: https://www.youtube.com/watch?v=GwsU2LPs85U&ab_channel=BarryBrown
        https://www.youtube.com/watch?v=shN_kHBFOUE&ab_channel=BarryBrown 
        nfa vs dfa: https://www.geeksforgeeks.org/difference-between-dfa-and-nfa/ : nfa 一个state可以转化出多个states，dfa：一个state只能转化出一个state
        https://zhuanlan.zhihu.com/p/30009083 
        各种概念：https://blog.csdn.net/c601097836/article/details/47040703

        解题方法类似：https://leetcode-cn.com/problems/valid-number/solution/you-xiao-shu-zi-by-leetcode-solution-298l/
        如果不用enum：https://leetcode-cn.com/problems/valid-number/solution/python-dfa-zhuang-tai-ji-zhuan-huan-by-q-0rog/
        如果用二维数组：https://leetcode-cn.com/problems/valid-number/solution/biao-qu-dong-fa-by-user8973/

        时间复杂度：O(n)O(n)，其中 nn 为字符串的长度。我们需要遍历字符串的每个字符，其中状态转移所需的时间复杂度为 O(1)O(1)。

        空间复杂度：O(1)O(1)。只需要创建固定大小的状态转移表。

        """
        from enum import Enum
        class States(Enum):
            START = 0
            AFTER_SIGN = 1
            AFTER_DIGITS = 2
            AFTER_DOT_BEFORE_E = 3
            AFTER_DIGIT_BEFORE_E = 4
            AFTER_E = 5
            AFTER_E_SIGN = 6
            AFTER_E_DIGIT = 7
            AFTER_DOT = 8
        class Actions(Enum):
            SIGN = '+|-'
            DIGIT = '\d'
            DOT = '\.'
            E = 'E|e'
        accepted_states = [States.AFTER_DIGITS, States.AFTER_DOT_BEFORE_E, States.AFTER_DIGIT_BEFORE_E, States.AFTER_E_DIGIT]
        state_transfer = {
            States.START: {
                Actions.SIGN: States.AFTER_SIGN,
                Actions.DIGIT: States.AFTER_DIGITS,
                Actions.DOT: States.AFTER_DOT
            },
            States.AFTER_SIGN: {
                Actions.DIGIT: States.AFTER_DIGITS,
                Actions.DOT: States.AFTER_DOT
            },
            States.AFTER_DIGITS: {
                Actions.DIGIT: States.AFTER_DIGITS,
                Actions.DOT: States.AFTER_DOT_BEFORE_E,
                Actions.E: States.AFTER_E
            },
            States.AFTER_DOT_BEFORE_E: {
                Actions.DIGIT: States.AFTER_DOT_BEFORE_E,
                Actions.E: States.AFTER_E
            },
            States.AFTER_DIGIT_BEFORE_E: {
                Actions.DIGIT: States.AFTER_DIGIT_BEFORE_E,
                Actions.E: States.AFTER_E
            },
            States.AFTER_E: {
                Actions.SIGN: States.AFTER_E_SIGN,
                Actions.DIGIT: States.AFTER_E_DIGIT
            },
            States.AFTER_E_SIGN: {
                Actions.DIGIT: States.AFTER_E_DIGIT
            },
            States.AFTER_E_DIGIT: {
                Actions.DIGIT: States.AFTER_E_DIGIT
            },
            States.AFTER_DOT: {
                Actions.DIGIT: States.AFTER_DIGIT_BEFORE_E
            }
        }
        def _char_to_action(char):
            if char in ['+', '-']:
                return Actions.SIGN
            if char.isdigit():
                return Actions.DIGIT
            if char == '.':
                return Actions.DOT
            if char in ['E', 'e']:
                return Actions.E
        state = States.START
        for ch in s:
            action = _char_to_action(ch)
            if action not in state_transfer[state]:
                return False
            state = state_transfer[state][action]
        return state in accepted_states


class SolutionThree:
    def isNumber(self, s: str) -> bool:
        """ simulation/模拟：https://leetcode-cn.com/problems/valid-number/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-4/ """
        i = 0
        is_numeric = False
        n = len(s)
        # deal with prefixing whitespaces
        while i < n and s[i] == ' ':
            i += 1
        # deal with signs
        if i < n and s[i] in '+-': i += 1
        # deal with integer part
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True
        # deal with decimal point
        if i < n and s[i] == '.': i += 1
        # deal with fractional part
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True
        # deal with e
        if i < n and s[i] in ['e', 'E']:
            if not is_numeric:
                return False
            i += 1
            is_numeric = False
            # deal with signs
            if i < n and s[i] in '+-': i += 1
            # deal with integer part
            while i < n and s[i].isdigit():
                i += 1
                is_numeric = True
            '''
            # Is 99e2.5 a number? if it is, then keep below
            # otherwise delete.
            # deal with decimal point
            if i < n and s[i] == '.': i += 1
            # deal with fractional part
            while i < n and s[i].isdigit():
                i += 1
                is_numeric = True
            '''

        # deal with affixing whitespaces
        while i < n and s[i] == ' ':
            i += 1
        # print(is_numeric, i)
        return is_numeric and i == len(s)


class SolutionOne(object):
    """ This solution is relatively efficient and can be found
    https://leetcode.com/submissions/detail/410966513/
    https://leetcode-cn.com/problems/valid-number/solution/java-luo-ji-chao-qing-xi-jie-fa-by-charlesgao/
    """
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        dot_flag = e_flag = digit_flag = False
        for i, char in enumerate(s):
            if char in '+-':
                # + - can only be the first char or after e
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif char == '.':
                # there cannot be . or e before .
                if dot_flag or e_flag:
                    return False
                dot_flag = True
            elif char == 'e':
                # there cannot be e or any none digit before e
                if e_flag or not digit_flag:
                    return False
                e_flag = True
                digit_flag = False
            elif char.isdigit():
                digit_flag = True
            else:
                return False
        return digit_flag


def is_number(s: str) -> bool:
    try:
        float(s)
    except ValueError:
        return False
    return True


class SolutionTwo(object):
    """
    solutions:
    https://leetcode.com/submissions/detail/409369817/
    The solution below seems very cumbersome , need look into easier ways
    """
    def isNumber(self, s: str) -> bool:
        i = 0
        num_start = None
        num_end = None
        sign = None
        count_of_e = 0
        e_start = None
        trailing_space_start = None
        count_of_dot = 0
        while i < len(s):
            if num_start is None:
                if s[i] != ' ':
                    num_start = i
                    if (s[i] != '.' and s[i] != '+' and s[i] != '-' and not s[i].isdigit()) or\
                            ((s[i] == '.' or s[i] == '+' or s[i] == '-')  and i == len(s) - 1):
                        return False
                    elif s[i] == '+':
                        sign = 1
                    elif s[i] == '-':
                        sign = -1
                    elif s[i].isdigit():
                        sign = 1
                    elif s[i] == '.':
                        count_of_dot += 1
                elif i == len(s) - 1:
                     return False
            elif num_start is not None:
                if not s[i].isdigit() and s[i] != 'e' and s[i] != ' ' and s[i] != '.' and s[i] != '-' and s[i] != '+':
                    return False
                if num_end is None:
                    if s[i] != ' ' and i != len(s) - 1 and s[i + 1] == ' ':
                        num_end = i
                    elif s[i] != ' ' and i == len(s) - 1:
                        num_end = i
                    elif s[i] == ' ':
                        num_end = i - 1
                if s[i] == 'e':
                    count_of_e += 1
                    if e_start is None:
                        e_start = i
                    if count_of_e > 1 or i == num_end or ((not s[i - 1].isdigit() and s[i - 1] != '.') or (s[i - 1] == '.' and i - 1 == num_start)):
                        return False
                if s[i] == '.':
                    count_of_dot += 1
                    if (e_start is not None and i > e_start) or count_of_dot > 1 or (not s[i - 1].isdigit() and i == len(s) - 1) or (not s[i - 1].isdigit() and not s[i + 1].isdigit()):
                        return False
                if s[i] == ' ' and trailing_space_start is None:
                    trailing_space_start = i
                    if s[i - 1] == '.' and num_start == num_end:
                        return False
                if s[i] != ' ' and trailing_space_start is not None and i > trailing_space_start:
                    return False
                if (s[i] == '+' or s[i] == '-') and ((e_start is None) or (e_start is not None and i < e_start) or (e_start is not None and i != e_start + 1) or (e_start is not None and (i == len(s) - 1 or not s[i + 1].isdigit()))):
                    return False
            i += 1
        return True


class valid_number_9:
    def __init__(self):
        pass
    def valid_num(self,num):
        num=num.strip(" ")
        dot_count=0
        #sign=0
        if num=="":
            return False
        elif num=='.':
            return False
        elif num[0]=='+' or num[0]=='-':
            num=num.lstrip(num[0])
        for i in num:
            if i=='.':
                dot_count+=1
                if dot_count>1:
                    return False
            if not (i.isdigit() or i=='.'):
                return False            
        return True
                