
class Solution:
    def decodeString(self, s: str) -> str:
        """ my recursive solution, not very efficient """
        if '[' not in s and ']' not in s:
            return s
        bracket_stack_counter = 0
        start = end = 0
        decoded = ''
        repeater = 1
        start_found = False
        repeater_start = 0
        for i, ch in enumerate(s):
            if ch.isdigit() and ((i > 0 and not s[i - 1].isdigit()) or (i == 0)):
                repeater_start = i
            elif ch == '[':
                if not start_found:
                    repeater = int(s[repeater_start:i])
                    start = i + 1
                    start_found = True
                bracket_stack_counter += 1
            elif ch == ']':
                end = i - 1
                bracket_stack_counter -= 1
                if bracket_stack_counter == 0:
                    decoded += repeater * self.decodeString(s[start:end + 1])
                    start_found = False
            elif ch.isalpha() and not start_found:
                decoded += ch
        return decoded



class Solution4:
    def decodeString(self, s: str) -> str:
        """ stack 栈
        https://leetcode-cn.com/problems/decode-string/solution/zhan-de-ji-yi-nei-ceng-de-jie-ma-liao-bie-wang-lia/ 方法2
        """
        # 我的解
        stack = deque()
        for char in s:
            if char.isdigit() or char == '[' or char.isalpha():
                stack.append(char)
            else:
                temp = ''
                # 组成string
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                # print(temp)
                stack.pop()
                multi = 0
                counter = 1
                # 组成前面的倍数
                while stack and stack[-1].isdigit():
                    multi = multi + counter * int(stack.pop())
                    counter *= 10
                # print(multi)
                # 倍数 X string ，再放回栈
                stack.append(multi * temp)
                # print(stack)
        return ''.join(stack)


class Solution2:
    def decodeString(self, s: str) -> str:
        """ 辅助栈解法：视频：https://leetcode-cn.com/problems/decode-string/solution/zi-fu-chuan-jie-ma-by-leetcode-solution/
        解法： https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
        """
        stack = []
        res = ''
        multi = 0
        for ch in s:
            if ch.isdigit():
                multi = multi * 10 + int(ch)
            elif ch.isalpha():
                res += ch
            elif ch == '[':
                stack.append((multi, res))
                multi = 0
                res = ''
            else:
                curr_multi, curr_res = stack.pop()
                res = curr_res + curr_multi * res
        return res


class Solution3:
    def decodeString(self, s: str) -> str:
        """ https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
        另外，注意lewes 在评论中的解法

        时间复杂度 O(N)，递归会更新索引，因此实际上还是一次遍历 s；
        空间复杂度 O(N)，极端情况下递归深度将会达到线性级别。
        """
        def dfs(s, i):
            res, multi = '', 0
            while i < len(s):
                if s[i].isdigit():
                    multi = 10 * multi + int(s[i])
                elif s[i].isalpha():
                    res += s[i]
                elif s[i] == '[':
                    i, temp = dfs(s, i + 1)
                    res += temp * multi
                    multi = 0
                else:
                    return i, res
                i += 1
            return res
        return dfs(s, 0)
