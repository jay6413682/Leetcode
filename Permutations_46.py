from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        非回溯递归解法：comments里满船星辉解法；无情铁手？有做优化

        https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
        """
        """
        if len(nums) == 1:
            return [nums]
        i = 0
        n = len(nums)
        permutations = []
        while i < n:
            dup_nums = nums.copy()
            curr = dup_nums.pop(i)
            child_permutations = self.permute(dup_nums)
            for permutation in child_permutations:
                permutations.append([curr] + permutation)
            i += 1
        return permutations
        """
        return self.build_permutation(nums, set())

    def build_permutation(self, nums, used_index):
        if len(used_index) == len(nums):
            return [[]]

        permutations = []
        for i, num in enumerate(nums):
            if i in used_index:
                continue
            used_index.add(i)
            child_permutations = self.build_permutation(nums, used_index)
            for permutation in child_permutations:
                permutations.append([num] + permutation)
            used_index.remove(i)
        return permutations


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法/深度优先搜索/DFS详解：https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/ 看视频讲解
        我们每天使用的搜索引擎帮助我们在庞大的互联网上搜索信息。搜索引擎的「搜索」和「回溯搜索」算法里「搜索」的意思是一样的。

        搜索问题的解，可以通过 遍历 实现。所以很多教程把「回溯算法」称为爆搜（暴力解法）。因此回溯算法用于 搜索一个问题的所有的解 ，通过深度优先遍历的思想实现。
        更多关于回溯法：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
        
        时间复杂度：O(n×n!)，

        空间复杂度：O(n×n!)

        """
        if not nums:
            return nums
        def dfs(nums, depth, path, used, res):
            if depth == len(nums):
                res.append([p for p in path])
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                print("  递归之前 => {}".format(path))
                dfs(nums, depth + 1, path, used, res)
                path.pop()
                used[i] = False
                print("递归之后 => {}".format(path))

        res = []
        path = []
        depth = 0
        used = [False for _ in range(len(nums))]
        dfs(nums, depth, path, used, res)
        return res
