import math
class Solution:
    def mySqrt(self, x: int) -> int:
        """ binary search
        https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
        时间复杂度：O(\log x)O(logx)，每一次搜索的区间大小为原来的 \cfrac{1}{2} 21，时间复杂度为 O(\log_2 x) = O(\log x)O(log 2x)=O(logx)；
        空间复杂度：O(1)O(1)。  
        """
        small = 0
        large = x
        while small < large:
            mid = (small + large + 1) // 2
            if mid ** 2 > x:
                large = mid - 1
            else:
                small = mid
        return small


'''
# not preferred
class Solution:
    def mySqrt(self, x: int) -> int:
        """ binary search
        https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
        为什么 left = mid + 1，right = mid - 1？我看有的代码是 right = mid 或者 left = mid，没有这些加加减减，到底怎么回事，怎么判断？: https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
        时间复杂度：O(\log x)O(logx)，即为二分查找需要的次数。

        空间复杂度：O(1)O(1)。
        """
        left = 0
        right = x
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            res = mid ** 2
            if res == x:
                return mid
            elif res < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
'''


class Solution2:
    def mySqrt(self, x: int) -> int:
        """ binary search; recursive; my solution: time complexity: O(logn); space complexity: O(logn)
        """
        def helper(left, right):
            if left > right:
                # the reason to return right, is because left - right must == 1;
                # if left was = mid + 1; then right == last mid; which is the smaller val we'd like to return
                return right
            mid = (left + right) // 2
            res = mid * mid 
            if res == x:
                return mid
            elif res > x:
                right = mid - 1
            else:
                left = mid + 1
            return helper(left, right)
        return helper(0, x)


class Solution3:
    def mySqrt(self, x: int) -> int:
        """ math solution: https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
        时间复杂度：O(1)O(1)，由于内置的 exp 函数与 log 函数一般都很快，我们在这里将其复杂度视为 O(1)O(1)。

        空间复杂度：O(1)O(1)。
        """
        if not x:
            return x
        raw = int(math.exp(1/2 * math.log(x)))
        return raw + 1 if (raw + 1) ** 2 <= x else raw


class Solution4:
    def mySqrt(self, x: int) -> int:
        """ Newton's method, iterative, x is C: https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
        derivative 导数 https://www.shuxuele.com/calculus/derivatives-introduction.html
        凸函数：https://zhuanlan.zhihu.com/p/56876303
        时间复杂度：O(\log x)O(logx)，此方法是二次收敛的，相较于二分查找更快。
        复杂度证明： https://www.zhihu.com/question/63641120
        https://blog.staynoob.cn/post/2016/06/integer-arithmetic-karatsuba-multiplication/
        收敛：https://zhuanlan.zhihu.com/p/133234487
        二次收敛：https://zhidao.baidu.com/question/212136386.html 。。。不太懂
        空间复杂度：O(1)O(1)。
        """
        if x == 0:
            return 0
        res = xi = x
        while True:
            res = 0.5 * (xi + x / xi)
            if abs(res - xi) <= 10 ** (-6):
                return int(res)
            xi = res
