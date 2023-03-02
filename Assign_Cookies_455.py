class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """ greedy 贪心 https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html#%E6%80%9D%E8%B7%AF
        注意是先遍历饼干还是先遍历胃口以及从小到大还是从大到小排列
        """
        g.sort()
        s.sort()
        j = 0
        count = 0
        ns = len(g)
        for i in range(len(s)):
            if j < ns and s[i] >= g[j]:
                count += 1
                j += 1
        return count

        """ greedy 贪心 my solution if not sort the array """
        count = 0
        removed = []
        for need in g:
            to_remove = None
            # print(len(s))
            for j in range(len(s)):
                if s[j] >= need:
                    if to_remove is None or s[j] < s[to_remove]:
                        to_remove = j
            if to_remove is not None:
                s.pop(to_remove)
                count += 1
        return count
