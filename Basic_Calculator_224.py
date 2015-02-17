class Solution:
    def calculate(self, s: str) -> int:
        """ Similar to 150. double stack: https://leetcode-cn.com/problems/basic-calculator/solution/shuang-zhan-jie-jue-tong-yong-biao-da-sh-olym/
        """
        def _calc(num_stack, sign_stack):
            sign = sign_stack.pop()
            num_right = num_stack.pop()
            num_left = num_stack.pop()
            if sign == '+':
                num = num_left + num_right
            else:
                num = num_left - num_right
            num_stack.append(num)

        num_stack = deque()
        sign_stack = deque()
        i = 0
        n = len(s)
        while i < n:
            char = s[i]
            if char == ' ':
                i += 1
            elif char == '(':
                sign_stack.append(char)
                i += 1
            elif char.isdigit():
                j = i + 1
                num = int(s[i])
                while j < n and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                num_stack.append(num)
                i = j
            elif char in ['+', '-']:
                # if - is the first item or it has (, + , -, before it; (if space is removed from string before hand), it means it's unary operator, add 0 to number stack
                if char == '-' and i == 0:
                    num_stack.append(0)
                    sign_stack.append(char)
                    # print(num_stack, sign_stack)
                    i += 1
                    continue
                j = i - 1
                while j >= 0:
                    # print(sign_stack, num_stack)
                    if s[j] == ' ':
                        j -= 1
                        continue
                    elif s[j] in ['(']:
                        num_stack.append(0)
                        break
                    else:
                        break
                # 把前面stacks 里前一个的加减运算做了
                if sign_stack and sign_stack[-1] in ['+', '-']:
                    _calc(num_stack, sign_stack)
                sign_stack.append(char)
                # print(sign_stack, num_stack)
                i += 1
            elif char == ')':
                # 把前面的加减做了，另外把左括号pop
                if sign_stack:
                    if sign_stack[-1] in ['+', '-']:
                        _calc(num_stack, sign_stack)
                    # there could be case like (1) , so there is only left bracket in sign_stack
                    sign_stack.pop()
                i += 1
            else:
                raise Exception
        # either there are two numbers in num_stack and a sign in sign_stack or there is only one number in num_stack
        if sign_stack:
            _calc(num_stack, sign_stack)
        return num_stack[-1]
        """
        # 根据https://leetcode-cn.com/problems/basic-calculator/solution/shuang-zhan-jie-jue-tong-yong-biao-da-sh-olym/ 重写
        def _calc(nums, ops):
            if not ops or ops[-1] == '(':
                return nums.pop()
            op = ops.pop()
            num_right = nums.pop()
            num_left = nums.pop()
            if op == '+':
                return int(num_left) + int(num_right)
            elif op == '-':
                return int(num_left) - int(num_right)
            else:
                raise Exception(op)
            
        n = len(s)
        nums = deque([0])
        ops = deque()
        i = 0
        tmp_num = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '(':
                ops.append(s[i])
                i += 1
            elif s[i].isdigit():
                while i < n and s[i].isdigit():
                    tmp_num = int(s[i]) + 10 * tmp_num
                    i += 1
                nums.append(tmp_num)
                tmp_num = 0
            elif s[i] in '+-':
                if i > 0 and s[i - 1] == '(':
                    nums.append(0)
                nums.append(_calc(nums, ops))
                ops.append(s[i])
                i += 1
            else:
                # ) case
                nums.append(_calc(nums, ops))
                ops.pop()
                i += 1
            # print(nums, ops)
        if ops:
            nums.append(_calc(nums, ops))
        return sum(nums)
        """


class Solution2:
    def calculate(self, s: str) -> int:
        # 单stack 解法 清风Python：https://leetcode-cn.com/problems/basic-calculator/solution/ru-he-xiang-dao-yong-zhan-si-lu-lai-zi-y-gpca/
        stack = deque()
        n = len(s)
        temp_num_str = ''
        for i in range(n - 1, -1, -1):
            if s[i].isdigit():
                temp_num_str += s[i]
                continue
            if not s[i].isdigit():
                if temp_num_str:
                    stack.append(int(temp_num_str[::-1]))
                    temp_num_str = ''
            if s[i] in ' +':
                continue
            if s[i] == ')':
                stack.append(s[i])
            elif s[i] == '-':
                stack.append(-stack.pop())
            elif s[i] == '(':
                num = 0
                while stack[-1] != ')':
                    num += stack.pop()
                stack.pop()
                stack.append(num)
            else:
                raise Exception
        if temp_num_str:
            stack.append(int(temp_num_str[::-1]))
        return sum(stack)


from collections import deque

class Solution3:
    def calculate(self,s:str)->int: 
        """ recursive, 不好理解，看不懂就算了 https://leetcode-cn.com/problems/basic-calculator/solution/ru-he-xiang-dao-yong-zhan-si-lu-lai-zi-y-gpca/ 
        https://leetcode-cn.com/problems/basic-calculator/solution/fen-jie-fu-za-wen-ti-yi-ge-ge-jie-jue-by-2rvh/
        """
        def dfs(queue):
            i = 0
            num = 0
            res = deque()
            sign = '+'
            while queue:
                char = queue.popleft()
                # print(char, num)

                if char == '(':
                    num = dfs(queue)
                if char.isdigit():
                    num = num * 10 + int(char)
                # 符号或者s 长度为0 最后一个数
                if char in ['+', '-', '(', ')'] or len(queue) == 0:
                    # e.g. 1 + 1 + 1，遇到第二个加号时，把第二个1 push 进res，遇到最后一个数的时候，把1加进res
                    if sign == '+':
                        res.append(num)
                    else:
                        res.append(-num)
                    # print(res)
                    num = 0
                    sign = char
                if char == ')':
                    break
            # print(res)
            return sum(res)
        queue = deque(s)
        return dfs(queue)
