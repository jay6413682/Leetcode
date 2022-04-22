from typing import List
from _collections import deque


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """ 回溯算法
        Cnk: https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/
        """
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
