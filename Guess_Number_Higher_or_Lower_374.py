# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """ binary search: https://leetcode-cn.com/problems/guess-number-higher-or-lower/solution/cai-shu-zi-da-xiao-by-leetcode-solution-qdzu/
        时间复杂度： O\big(\log_2 n\big)O(log2n) 。为二分查找的时间复杂度。
        空间复杂度： O(1)O(1) 。没有使用额外的空间。
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            guess_rt = guess(mid)
            if guess_rt == 0:
                return mid
            elif guess_rt == -1:
                right = mid - 1
            else:
                left = mid + 1
