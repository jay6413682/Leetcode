

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ 暴力法 超出时间限制
        https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/ti-mu-fen-xi-ji-yi-hua-sou-suo-bing-cha-ji-ji-lu-d/
        总体时间复杂度为(O(nlogn))(O(nlogn))。
        """
        '''
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        counter = 1
        longest_len = 1
        # print(nums)
        for n in nums:
            if n + 1 in nums:
                counter += 1
            else:
                counter = 1
            # print(counter, longest_len)
            longest_len = max(counter, longest_len)
        return longest_len
        '''
        if not nums:
            return 0
        sorted_unique_nums = sorted(list(set(nums)))
        n = len(sorted_unique_nums)
        length = 1
        counter = 1
        for i in range(n - 1):
            if sorted_unique_nums[i + 1] == sorted_unique_nums[i] + 1:
                counter += 1
                if counter > length:
                    length = counter
            else:
                counter = 1
        return length



class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ 哈希表/hash
        https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
        增加了判断跳过的逻辑之后，时间复杂度是多少呢？外层循环需要 O(n)O(n) 的时间复杂度，只有当一个数是连续序列的第一个数的情况下才会进入内层循环，然后在内层循环中匹配连续序列中的数，因此数组中的每个数只会进入内层循环一次。根据上述分析可知，总时间复杂度为 O(n)O(n)，符合题目要求。
        时间复杂度：O(n)O(n)，其中 nn 为数组的长度。具体分析已在上面正文中给出。

        空间复杂度：O(n)O(n)。哈希表存储数组中所有的数需要 O(n)O(n) 的空间。

        """
        if not nums:
            return 0
        nums = set(nums)
        len_longest_consecutive = 1
        for num in nums:
            if num - 1 in nums:
                continue
            next_num = num + 1
            while next_num in nums:
                next_num += 1
            len_consecutive = next_num - num
            len_longest_consecutive = len_consecutive if len_consecutive > len_longest_consecutive else len_longest_consecutive
        return len_longest_consecutive


class UnionFind(object):
    """ union find or called Disjoint-set """
    def __init__(self, nums):
        self.fa = {num: num for num in nums}
        self.count = {num: 1 for num in nums}
    def find(self, num):
        if num == self.fa[num]:
            return num
        # 路径压缩/Path compression optimization
        self.fa[num] = self.find(self.fa[num])
        return self.fa[num]
    def union(self, a, b):
        if b not in self.fa:
            return 1
        x, y = self.find(a), self.find(b)
        if x == y: return self.count[x]
        # 按秩合并/Union by size or depth（ rank ）, in this example, it is by size: https://cp-algorithms.com/data_structures/disjoint_set_union.html#toc-tgt-4
        if self.count[x] <= self.count[y]:
            self.fa[x] = y
            self.count[y] += self.count[x]
            rtv = self.count[y]
        else:
            self.fa[y] = x
            self.count[x] += self.count[y]
            rtv = self.count[x]
        return rtv


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ 并查集：https://zhuanlan.zhihu.com/p/93647900 ； https://oi-wiki.org/ds/dsu/
        close to https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/tu-jie-yu-dao-jiu-shen-jiu-bing-cha-ji-by-chun-men/
        time complexity: with optimization, Union find nearly constant time queries. so in total it is O(n); Also, it's worth mentioning that DSU with union by size / rank, but without path compression works in O(nlogn) time per query.: https://cp-algorithms.com/data_structures/disjoint_set_union.html#toc-tgt-4
        https://zhuanlan.zhihu.com/p/93647900：
        路径压缩和按秩合并如果一起使用，时间复杂度接近 [公式] ，但是很可能会破坏rank的准确性。
        纪卓志 George纪卓志
        秩是树的高度，路径压缩后会影响秩的秩，这个时候再用秩做启发式合并会得到错误的信息。一般来说我都不会用秩去合并，而是改用按大小合并+路径压缩，因为大小是树的属性且与树高度变化无关。只需要把根的自环表示改成无效根表示，根的父节点改成树大小的负值就可以。有的时候需要统计等价类大小可以直接使用
        https://oi-wiki.org/ds/dsu/
        在算法竞赛的实际代码中，即便不使用启发式合并，代码也往往能够在规定时间内完成任务。在 Tarjan 的论文[1]中，证明了不使用启发式合并、只使用路径压缩的最坏时间复杂度是 。在姚期智的论文[2]中，证明了不使用启发式合并、只使用路径压缩，在平均情况下，时间复杂度依然是 。

        如果只使用启发式合并，而不使用路径压缩，时间复杂度为 。由于路径压缩单次合并可能造成大量修改，有时路径压缩并不适合使用。例如，在可持久化并查集、线段树分治 + 并查集中，一般使用只启发式合并的并查集。

        space complexity: O(n)
        """
        if not nums:
            return 0
        uf = UnionFind(nums)
        res = 1
        for num in nums:
            res = max(res, uf.union(num, num + 1))
        return res




class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        hash map/dynamic programming, https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/dong-tai-gui-hua-python-ti-jie-by-jalan/
        whiteding 和 音宫的comment
        O(n) 复杂度

        """
        num_consecutive_count_mapping = {}
        num_set = set(nums)
        res = 0
        # 思想：我们把来的每一个数，都当作端点来对待: 以num为端点的consecutive count
        for num in num_set:
            if num not in num_consecutive_count_mapping:
                left = num_consecutive_count_mapping.get(num - 1, 0)
                right = num_consecutive_count_mapping.get(num + 1, 0)
                count = left + right + 1
                if count > res:
                    res = count
                num_consecutive_count_mapping[num] = num_consecutive_count_mapping[num - left] = num_consecutive_count_mapping[num + right] = count
        return res


class Solution3_2:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ dp 超出memory限制 ，我的解，根据记忆化搜索我的解法写出 (记忆化搜索到dynamic programming：https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247485319&idx=1&sn=95a3dc9c97ca57185de792ca70924afe&chksm=fd9cac98caeb258ebea466f59378670a90af1cb3015ae70922e1d04ac711a5b8d8d853ac5e7d&token=677741617&lang=zh_CN&scene=21#wechat_redirect)"""
        if not nums:
            return 0
        max_val = max(nums)
        min_val = min(nums)
        length = max_val - min_val + 1
        # 以num为终点的最长路的长度
        dp = [0] * length
        nums_set = set(nums)
        longest = 0
        for num in range(min_val, max_val + 1):
            if length == 0:
                break
            idx = num - min_val
            if num in nums_set:
                if num == min_val:
                    dp[idx] = 1
                else:
                    dp[idx] = dp[idx - 1] + 1
                longest = max(longest, dp[idx])
        return longest



class Solution4:
    """ 记忆化搜索 / memorization / dp : https://stackoverflow.com/questions/6184869/what-is-the-difference-between-memoization-and-dynamic-programming
    解题 https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/ti-mu-fen-xi-ji-yi-hua-sou-suo-bing-cha-ji-ji-lu-d/
    https://oi-wiki.org/dp/memo/ 模版
    int g[MAXN];
    int f(状态参数) {
        if (g[规模] != 无效数值) return g[规模];
        if (终止条件) return 最小子问题解;
        g[规模] = f(缩小规模);
        return g[规模];
    }
    int main() {
        // ...
        memset(g, 无效数值, sizeof(g));
        // ...
    }
    官方都是dfs递归 来解记忆化搜索
    记忆化搜索的思想来实现的，我们可以注意到，其实是自顶向下来看的 https://stackoverflow.com/questions/6164629/what-is-the-difference-between-bottom-up-and-top-down 
    TOP of the tree
    fib(4)
     fib(3)...................... + fib(2)
      fib(2)......... + fib(1)       fib(1)........... + fib(0)
       fib(1) + fib(0)   fib(1)       fib(1)              fib(0)
        fib(1)   fib(0)
    BOTTOM of the tree
    然而动态规划的思想是从底向上的：
    def dp_fib(n):
       partial_answers = [1, 1]
       while len(partial_answers) <= n:
         partial_answers.append(partial_answers[-1] + partial_answers[-2])
       return partial_answers[n]
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        # // 记忆化搜索 dfs返回的结果是以v为起点的最长路的长度
        def dfs(mp, num):
            # if (终止条件) return 最小子问题解;
            if num not in mp:
                mp[num] = 0
                return mp[num]
            # if (g[规模] != 无效数值) return g[规模];
            if mp[num] != 0:
                return mp[num]
            # g[规模] = f(缩小规模);
            mp[num] = dfs(mp, num + 1) + 1
            # return g[规模];
            return mp[num]
        #  // mp[v] 表示以v为起点的最长路的长度
        # memset(g, 无效数值, sizeof(g));
        mp = {num: 0 for num in nums}
        for num in nums:
            mp[num] = dfs(mp, num)
        # print(mp)
        return max(mp.values())


class Solution4_2:
    mem = {}
    def longestConsecutive(self, nums: List[int]) -> int:
        """ 记忆化搜索 我的解法二 """
        if not nums:
            return 0
        self.mem = {num: 0 for num in nums}
        # 记忆化搜索 dfs返回的结果是以v为终点的最长路的长度
        def dfs(num):
            # if (终止条件) return 最小子问题解;
            if num not in self.mem:
                return 0
            # if (g[规模] != 无效数值) return g[规模];
            if self.mem[num] != 0:
                return self.mem[num]
            # g[规模] = f(缩小规模);
            self.mem[num] = dfs(num - 1) + 1
            # return g[规模];
            return self.mem[num]
        longest = 1
        for num in nums:
            longest = max(longest, dfs(num))
        return longest
