class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtracking 回溯 ： https://leetcode.cn/problems/subsets-ii/solution/90-zi-ji-iiche-di-li-jie-zi-ji-wen-ti-ru-djmf/
        def dfs(sorted_nums, start_i, res, path, le):
            res.append(path[:])
            for i in range(start_i, le):
                # 我们要对同一树层使用过的元素进行跳过
                if i > start_i and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(sorted_nums, i + 1, res, path, le)
                path.pop()

        nums.sort()
        res = []
        dfs(nums, 0, res, [], len(nums))
        return res
