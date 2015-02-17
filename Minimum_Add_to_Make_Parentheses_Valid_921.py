class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """ my solution; 两个栈空间复杂度高一点 """
        left_stack = []
        right_stack = []
        for ch in S:
            if ch == '(':
                left_stack.append(ch)
            else:
                if left_stack:
                    left_stack.pop()
                else:
                    right_stack.append(ch)
        return len(left_stack) + len(right_stack)


class Solution2:
    def minAddToMakeValid(self, S: str) -> int:
        """ 栈实现 https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/solution/li-yong-zhan-shi-xian-by-multiply-p6j0/ """
        stack = []
        for ch in S:
            if ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return len(stack)


class Solution3:
    def minAddToMakeValid(self, S: str) -> int:
        """
        https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/solution/yi-wen-miao-sha-san-dao-gua-hao-xiang-guan-de-ti-2/
        1541 题如果理解不了，看 https://leetcode-cn.com/problems/minimum-insertions-to-balance-a-parentheses-string/solution/liang-chong-jie-fa-by-jason-2-73/
        """
        left_needs = 0
        right_needs = 0
        for ch in S:
            if ch == '(':
                right_needs += 1
            else:
                right_needs -= 1
                if right_needs == -1:
                    left_needs += 1
                    right_needs = 0
        return right_needs + left_needs
