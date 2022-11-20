from typing import List
from _collections import deque


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """ 回溯算法
        Cnk: https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/
        """
        # lastest solution：
        def dfs(start_i, depth, res, path):
            if depth == k:
                res.append(path[:])
                return
            if start_i == n + 1:
                return
            for i in range(start_i, n + 1):
                # 剪枝：
                # n - i: 剩下几个数可以选
                # k - (depth + 1)： 还需要几个数才能凑成k
                # 左边小于右边，当前level 剩下的数 和 子节点的数都不用看了 因为肯定不满足条件
                if n - i < k - (depth + 1):
                    break
                path.append(i)
                dfs(i + 1, depth + 1, res, path)
                path.pop()
        res = []
        dfs(1, 0, res, [])
        return res

        nums = [i for i in range(1, n + 1)]
        path = deque()
        res = []

        def dfs(start, nums, path, res):
            p_len = len(path)
            if p_len == k:
                res.append(list(path))
                return
            # no trimming
            # for i in range(start, n):
            # trimming:
            # k - p_len: 剩下需要加几个数字
            # n - (k - p_len): 上限前面一个数字（不是index），正好是上限的nums index值
            # n + 1 - (k - p_len))： range 上限值为第二个arg - 1，所以先加一
            for i in range(start, n + 1 - (k - p_len)):
                path.append(nums[i])
                dfs(i + 1, nums, path, res)
                path.pop()
        dfs(0, nums, path, res)
        return res
        '''
        # my first try
        def dfs(n, k, start, depth, path, res):
            if depth == k:
                res.append(path.copy())
                return
            i = start
            # try draw the tree to figure out upper limit:
            # n + (depth + 1) = upper_limit + k
            # e.g. 6 + 0 + 1 = 4 + 3
            while i <= n + depth + 1 - k:
                path.append(i)
                dfs(n, k, i + 1, depth + 1, path, res)
                path.pop()
                i += 1
        res = []
        dfs(n, k, 1, 0, [], res)
        return res
        '''
