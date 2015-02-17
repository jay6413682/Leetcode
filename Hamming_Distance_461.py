class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        https://leetcode-cn.com/problems/hamming-distance/solution/yi-ming-ju-chi-by-leetcode/
        复杂度分析

        时间复杂度：\mathcal{O}(1)O(1)，在 Python 和 Java 中 Integer 的大小是固定的，处理时间也是固定的。 32 位整数需要 32 次迭代。

        空间复杂度：\mathcal{O}(1)O(1)，使用恒定大小的空间。
        """
        xy_xor = x ^ y
        counter = 0
        while xy_xor:
            if xy_xor & 1 == 1:
                counter += 1
            xy_xor >>= 1
        return counter


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Brian W. Kernighan algorithm: https://leetcode-cn.com/problems/hamming-distance/solution/yi-ming-ju-chi-by-leetcode-solution-u1w7/
        时间复杂度：\mathcal{O}(1)O(1)。

        与移位方法相似，由于整数的位数恒定，因此具有恒定的时间复杂度。

        但是该方法需要的迭代操作更少。

        空间复杂度：\mathcal{O}(1)O(1)，与输入无关，使用恒定大小的空间。


        """
        x_xor_y = x ^ y
        distance = 0
        while x_xor_y:
            x_xor_y &= (x_xor_y - 1)
            distance += 1
        return distance
