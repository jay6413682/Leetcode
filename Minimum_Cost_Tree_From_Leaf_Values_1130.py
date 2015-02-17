class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """ dp/类似1039题 https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns#Minimum-(Maximum)-Path-to-Reach-a-Target
        解法：https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/solution/xiang-xi-jie-shi-dong-tai-gui-hua-dan-diao-zhan-ji/
        https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/solution/java-dp-by-ke-xue-jia-12/
        python解https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/solution/dong-tai-gui-hua-dan-diao-zhan-python3-by-smoon1-2/
        """
        n = len(arr)
        max_values = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                max_values[i][j] = max(arr[i:j + 1])
        dp = [[float('inf')] * n for _ in range(n)]
        # print(dp, max_values)
        for i in range(n):
            dp[i][i] = 0
        for j in range(n):
            for i in range(j - 1, -1, -1):
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max_values[i][k] * max_values[k + 1][j])
        # print(dp)
        return dp[0][n - 1]


class Solution2:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """ 单调栈，monotonic stack
        不好理解，尽量：https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/solution/xiang-xi-jie-shi-dong-tai-gui-hua-dan-diao-zhan-ji/
        https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/one-pass-on-time-and-space
        虽然有这个解释，但是有些时候并不符合Huffman Tree https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/solution/wei-shi-yao-dan-diao-di-jian-zhan-de-suan-fa-ke-xi/ 

        Time O(N) for one pass
        Space O(N) for stack in the worst cases
        """
        stack = deque([float('inf')])
        res = 0
        for v in arr:
            while v > stack[-1]:
                popped = stack.pop()
                res += popped * min(v, stack[-1])
            stack.append(v)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
