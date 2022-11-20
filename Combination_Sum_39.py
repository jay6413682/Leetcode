from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 我的回溯算法解法；使用sum 所以用时更长？
        https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
        """
        def dfs(candidates, target, start, path, res):
            if sum(path) == target:
                if path not in res:
                    res.append(path.copy())
                return
            elif sum(path) > target:
                return
            c = candidates[0]
            while start < len(candidates) and c <= target:
                c = candidates[start]
                path.append(c)
                dfs(candidates, target, start, path, res)
                path.pop()
                start += 1
        res = []
        candidates.sort()
        start = 0
        dfs(candidates, target, start, [], res)
        return res


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯/backtracking： https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
        复杂度：https://leetcode-cn.com/problems/combination-sum/solution/zu-he-zong-he-by-leetcode-solution/
        时间复杂度：O(S)O(S)，其中 SS 为所有可行解的长度之和。从分析给出的搜索树我们可以看出时间复杂度取决于搜索树所有叶子节点的深度之和，即所有可行解的长度之和。在这题中，我们很难给出一个比较紧的上界，我们知道 O(n \times 2^n)O(n×2 n) 是一个比较松的上界，即在这份代码中，nn 个位置每次考虑选或者不选，如果符合条件，就加入答案的时间代价。但是实际运行的时候，因为不可能所有的解都满足条件，递归的时候我们还会用 target - candidates[idx] >= 0 进行剪枝，所以实际运行情况是远远小于这个上界的。

        空间复杂度：O(\textit{target})O(target)。除答案数组外，空间复杂度取决于递归的栈深度，在最差情况下需要递归 O(\textit{target})O(target) 层。
        排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），需要记录哪些数字已经使用过，此时用 used 数组；组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同列表时），需要按照某种顺序搜索，此时使用 begin 变量。注意：具体问题应该具体分析， 理解算法的设计思想 是至关重要的，请不要死记硬背。

        """
        def dfs(candidates, length, target, start, path, res):
            if target == 0:
                res.append(path.copy())
                return
            i = start
            while i < length:
                c = candidates[i]
                # 剪枝
                # 根据上面画树形图的经验，如果 target 减去一个数得到负数，那么减去一个更大的树依然是负数
                if target - c < 0:
                    break
                    # continue
                path.append(c)
                dfs(candidates, length, target - c, i, path, res)
                path.pop()
                i += 1
        res = []
        # 剪枝需要升序，否则target - c < 0 就不能break 而用continue 因为后面的数有可能>0
        candidates.sort()
        dfs(candidates, len(candidates), target, 0, [], res)
        return res


class Solution:
    # my latest try. similar to https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
    done = False
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, total, path, res, start_i, le):
            # 当 total 等于 target 或 大于 target 说明 不需要再向右 或向下
            if total == target:
                res.append(path[:])
                self.done = True
                return
            if total > target:
                self.done = True
                return
            for i in range(start_i, le):
                # if done is true 既不向下 也不向右 因为candidates 有序，后面的只会更大
                if self.done:
                    break
                path.append(candidates[i])
                # 从上往下传时 start_i 不变, 但是在下面的 start i 都和顶端的 i 相同
                dfs(candidates, total + candidates[i], path, res, i, le)
                path.pop()
            # 出栈（向上）重置 done 的值
            self.done = False
        res = []
        candidates.sort()
        dfs(candidates, 0, [], res, 0, len(candidates))
        return res
