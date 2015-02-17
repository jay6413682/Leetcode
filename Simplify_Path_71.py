class Solution:
    def simplifyPath(self, path: str) -> str:
        """ 我的解法 效率不高 """
        stack = []
        if path[-1] != '/':
            path += '/'
        for i, ch in enumerate(path):
            if ch == '/':
                if stack and stack[-1]== '/':
                    continue
                elif stack and len(stack) > 1 and stack[-1] == '.':
                    if stack[-2] == '/':
                        # curr level
                        stack.pop()
                    elif len(stack) > 2 and stack[-2] == '.' and stack[-3] == '/':
                        # uppder level
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        while stack and stack[-1] != '/':
                            stack.pop()
                        if not stack:
                            stack.append('/')
                    else:
                        stack.append('/')
                else:
                    stack.append('/')
            else:
                stack.append(ch)
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        return ''.join(stack)


class Solution2:
    def simplifyPath(self, path: str) -> str:
        """ 栈：https://leetcode-cn.com/problems/simplify-path/solution/zhan-by-powcai/ """
        stack = []
        path_items = path.split('/')
        for item in path_items:
            if item == '..':
                if stack:
                    stack.pop()
            elif item != '.' and item:
                stack.append(item)
        return '/' + '/'.join(stack)

