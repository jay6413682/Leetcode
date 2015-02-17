from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法：https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
        关于剪枝：https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
        时间复杂度：O(n×n!)，

        空间复杂度：O(n×n!)
        """
        def dfs(nums, depth, path, used, res):
            if depth == len(nums):
                res.append(path.copy())
                return
            for i, num in enumerate(nums):
                if used[i] or (i > 0 and not used[i - 1] and nums[i] == nums[i - 1]):
                    continue
                used[i] = True
                path.append(num)
                dfs(nums, depth + 1, path, used, res)
                path.pop()
                used[i] = False
        nums.sort()
        res = []
        dfs(nums, 0, [], [False for _ in range(len(nums))], res)
        return res
