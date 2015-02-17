from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯法，大剪枝 + 小剪枝 优化
        https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
        """
        def dfs(candidates, target, length, start, path, res):
            if target == 0 and path not in res:
                res.append(path.copy())
                return
            i = start
            while i < length:
                c = candidates[i]
                # 大剪枝：减去 candidates[i] 小于 0，减去后面的 candidates[i + 1]、candidates[i + 2] 肯定也小于 0，因此用 break
                if target - c < 0:
                    break
                # 小剪枝：同一层相同数值的结点，从第 2 个开始，候选数更少，结果一定发生重复，因此跳过，用 continue
                if i > start and candidates[i] == candidates[i - 1]:
                    i += 1
                    continue
                path.append(c)
                i += 1
                dfs(candidates, target - c, length, i, path, res)
                path.pop()
        res = []
        candidates.sort()
        dfs(candidates, target, len(candidates), 0, [], res)
        return res


class Solution2:
    """ 我的解法，回溯法，没有小剪枝，需要优化 """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, length, start, path, res):
            # path not in res没有小剪枝所以需要查重
            if target == 0 and path not in res:
                res.append(path.copy())
                return
            while start < length:
                c = candidates[start]
                if target - c < 0:
                    break
                path.append(c)
                start += 1
                dfs(candidates, target - c, length, start, path, res)
                path.pop()
        res = []
        candidates.sort()
        dfs(candidates, target, len(candidates), 0, [], res)
        return res
