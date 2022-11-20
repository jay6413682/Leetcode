class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ backtracking回溯 https://leetcode.cn/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/
        """
        def dfs(start_i, res, path, le):
            res.append(path[:])
            # not necessary:
            #if start_i == le:
            #    return
            for i in range(start_i, le):
                path.append(nums[i])
                dfs(i + 1, res, path, le)
                path.pop()
        res = []
        dfs(0, res, [], len(nums))
        return res
