from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法：https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
        关于剪枝：https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
        这个可能更好理解：https://leetcode.cn/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/ 
        时间复杂度：O(n×n!)，

        空间复杂度：O(n×n!)
        """
        # my latest solution. 不用排序
        le = len(nums)
        used_upper_levels = [False] * le
        def dfs(nums, used_upper_levels, depth, le, path, res):
            if depth == le:
                res.append(path[:])
                return
            used_current_levels = set()
            for i in range(le):
                if used_upper_levels[i]:
                    continue
                if nums[i] in used_current_levels:
                    continue
                used_current_levels.add(nums[i])
                used_upper_levels[i] = True
                path.append(nums[i])
                dfs(nums, used_upper_levels, depth + 1, le, path, res)
                path.pop()
                used_upper_levels[i] = False
        res = []
        dfs(nums, used_upper_levels, 0, le, [], res)
        return res
        # 需要排序：
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
