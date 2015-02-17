from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """ https://leetcode-cn.com/problems/baseball-game/solution/682bang-qiu-bi-sai-python3-biao-zhun-zha-en2w/
        也可维护stack 和 sum： void 回复 free-fish comment： https://leetcode-cn.com/problems/baseball-game/solution/bang-qiu-bi-sai-by-leetcode/
        """
        stack = []
        for op in ops:
            # below is how you check whether negative number or positive number
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            elif op == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif op == 'D':
                stack.append(int(stack[-1]) * 2)
            elif op == 'C':
                stack.pop()
        return sum(stack)
