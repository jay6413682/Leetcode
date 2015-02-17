# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        binary search: https://leetcode-cn.com/problems/first-bad-version/solution/di-yi-ge-cuo-wu-de-ban-ben-by-leetcode-s-pf8h/
        时间复杂度：O(\log n)O(logn)。搜索空间每次减少一半，因此时间复杂度为 O(\log n)O(logn)。
        空间复杂度：O(1)O(1)。
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            is_bad_ver = isBadVersion(mid)
            if is_bad_ver is True:
                right = mid
            else:
                left = mid + 1
        return left
