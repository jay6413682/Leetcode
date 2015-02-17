""" MUST READ! Here is a better explanation of the question: https://blog.csdn.net/fuxuemingzhu/article/details/101040431

The read function will only be called once for each test case.

There is no where to verify this solution though, not lintcode or leetcode.

I drawed a graph for different conditions to solve this issue
"""


class Solution:

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        eof = False
        num_chars_read = 0
        while eof is False and num_chars_read < n:
            buf4 = [''] * 4
            num_chars_read4 = Reader.read4(buf4)
            if num_chars_read4 < 4:
                eof = True
            num_chars_read4 = num_chars_read4 if num_chars_read4 < n - num_chars_read else n - num_chars_read
            buf[num_chars_read:] = buf4[:num_chars_read4]
            num_chars_read += num_chars_read4
        return num_chars_read


Solution().read([], 6)
Solution().read([], 20)
Solution().read([], 14)
Solution().read([], 10)
Solution().read([], 4)
Solution().read([], 0)
Solution().read([], 20)
Solution().read([], 20)
