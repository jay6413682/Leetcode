class Solution:
    """ brutal force
    https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode-solution-ds6y/

    时间复杂度：O(n \times m)O(n×m)，其中 nn 是字符串 \textit{haystack}haystack 的长度，mm 是字符串 \textit{needle}needle 的长度。最坏情况下我们需要将字符串 \textit{needle}needle 与字符串 \textit{haystack}haystack 的所有长度为 mm 的子串均匹配一次。

    空间复杂度：O(1)O(1)。我们只需要常数的空间保存若干变量。
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            found = haystack[i:i + len(needle)]
            if found == needle:
                return i
        return -1


class Solution2:
    def _get_next(self, needle):
        # 可用https://leetcode-cn.com/problems/implement-strstr/solution/shua-chuan-lc-shuang-bai-po-su-jie-fa-km-tb86/ 和 https://leetcode-cn.com/problems/implement-strstr/solution/zhe-ke-neng-shi-quan-wang-zui-xi-de-kmp-8zl57/ 事例帮助理解
        j = 0
        i = 1
        n = len(needle)
        next = [0] * n
        while i < n:
            if needle[i] == needle[j]:
                next[i] = j + 1
                j += 1
                i += 1
            else:
                if j >= 1:
                    j = next[j - 1]
                else:
                    next[i] = 0
                    i += 1
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        """ 我自己的kmp 解法；有点像下面这个链接Benhao的评论解

        KMP讲解: https://leetcode-cn.com/problems/implement-strstr/solution/shua-chuan-lc-shuang-bai-po-su-jie-fa-km-tb86/
        时间复杂度：n 为原串的长度，m 为匹配串的长度。复杂度为 O(m + n)O(m+n)。
        空间复杂度：构建了 next 数组。复杂度为 O(m)O(m)。
        宫水三叶回答chicchic：
        哈哈哈哈 j 就是匹配串的指针呀

        如果匹配不上 就跳转到 next 点继续匹配 j = next[j] 就是这个含义 ~

        其实我觉得你可以把「KMP 相比朴素如何加快查找」、「为什么需要 next」、「next 如何求得（注意是如何求得，而不是为什么可以这样求）」

        然后背过模板 即可

        或者偷懒一点 干脆只背模板
        我大致搞懂 KMP 的逻辑 是在我背过模板的两三年之后

        理解证明 则是在我背过模板的四五年之后
        如果你有状态机前置知识 可以尝试去看看 ~

        其实是一个线性状态机 +前缀
        状态机，finite state machine:https://zhuanlan.zhihu.com/p/47434856 
        https://www.cnblogs.com/21207-iHome/p/6085334.html
        例子：https://leetcode-cn.com/problems/implement-strstr/solution/zhe-ke-neng-shi-quan-wang-zui-xi-de-kmp-8zl57/
        """
        if not needle:
            return 0
        next = self._get_next(needle)
        i = j = 0
        n = len(haystack)
        m = len(needle)
        res = -1
        while i < n:
            if haystack[i] == needle[j]:
                # j 到 needle 尾，说明match
                if j == m - 1:
                    res = i - m + 1
                    break
                i += 1
                j += 1
            else:
                if j >= 1:
                    j = next[j - 1]
                else:
                    i += 1
        return res
