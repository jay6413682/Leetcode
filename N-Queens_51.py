class Solution:
    """ backtracking/回溯 超时 ， 剪枝不够 """
    res = ''
    found_counter = 0
    def getPermutation(self, n: int, k: int) -> str:
        used = [False] * (n + 1)
        def dfs(used, path, depth):
            if depth == n:
                self.found_counter += 1
                if self.found_counter == k:
                    self.res = ''.join(path)
                return
            for i in range(1, n + 1):
                if self.res:
                    return
                if used[i]:
                    continue
                path.append(str(i))
                used[i] = True
                dfs(used, path, depth + 1)
                used[i] = False
                path.pop()
        dfs(used, [], 0)
        return self.res


class Solution:
    res = ''
    remaining_counter = 0
    def getPermutation(self, n: int, k: int) -> str:
        """ backtracking 回溯 我的解 https://leetcode.cn/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/ 
        """
        used = [False] * (n + 1)
        factorials = [1]
        for i in range(1, n + 1):
            factorials.append(factorials[i - 1] * i)
        self.remaining_counter = k
        #print(factorials)
        def dfs(used, path, depth):
            curr_fact_counter = factorials[n - depth]
            #print(curr_fact_counter, self.remaining_counter)
            if curr_fact_counter < self.remaining_counter:
                self.remaining_counter -= curr_fact_counter
                return
            else:
                if self.remaining_counter == 1 and depth == n:
                    self.res = ''.join(path)
                    return
                #print(used, path, depth)
                for i in range(1, n + 1):
                    if self.res:
                        return
                    if used[i]:
                        continue
                    path.append(str(i))
                    used[i] = True
                    dfs(used, path, depth + 1)
                    used[i] = False
                    path.pop()
        dfs(used, [], 0)
        return self.res


class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        """ backtracking 回溯 官方最优 https://leetcode.cn/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/ 
        """
        used = [False] * (n + 1)
        factorials = [1]
        for i in range(1, n + 1):
            factorials.append(factorials[i - 1] * i)
        def dfs(used, path, depth, k):
            if depth == n:
                return
            # 当前level 的 单个子node 共 有多少种排列法
            curr_fact_counter = factorials[n - 1 - depth]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if curr_fact_counter < k:
                    k -= curr_fact_counter
                    continue
                path.append(str(i))
                used[i] = True
                dfs(used, path, depth + 1, k)
                return
        path = []
        dfs(used, path, 0, k)
        return ''.join(path)
