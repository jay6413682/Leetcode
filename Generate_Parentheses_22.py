class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """ backtrack 回溯 https://leetcode.cn/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/ """
        # dfs：
        def dfs(pre_str, res, left_counter, right_counter, depth):
            if depth == n * 2:
                res.append(pre_str)
                return
            if left_counter < n:
                dfs(pre_str + '(', res, left_counter + 1, right_counter, depth + 1)
            if right_counter < left_counter:
                dfs(pre_str + ')', res, left_counter, right_counter + 1, depth + 1)
        res = []
        dfs('', res, 0, 0, 0)
        return res
        # bfs：pre_str, left_counter, right_counter可以构建一个类，node.pre_str, node.left_counter, node.right_counter
        queue = deque([['(', 1, 0]])
        pre_str = ''
        res = []
        while queue:
            # print(queue)
            pre_str, left_counter, right_counter = queue.popleft()
            if left_counter == n and right_counter == n:
                res.append(pre_str)
            if left_counter < n:
                queue.append([pre_str + '(', left_counter + 1, right_counter])
            if right_counter < left_counter:
                queue.append([pre_str + ')', left_counter, right_counter + 1])
        return res
