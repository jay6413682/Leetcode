class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ 暴力法： https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/ """
        i = 0
        max_sum = nums[0]
        while i < len(nums):
            j = i
            while j < len(nums):
                max_sum = max(sum(nums[i:j + 1]), max_sum)
                j += 1
            i += 1
        return max_sum


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        贪心算法/Greedy algorithm : https://leetcode-cn.com/problems/maximum-subarray/solution/liang-chong-fang-fa-yi-kan-jiu-hui-yi-qiao-jiu-dui/
        复杂度：https://leetcode-cn.com/problems/maximum-subarray/solution/53-zui-da-zi-xu-he-bao-li-tan-xin-xiang-jie-by-car/
        讲解与例题：https://houbb.github.io/2020/01/23/data-struct-learn-07-base-greedy
        时间复杂度：O(n)
        空间复杂度：O(1)
        num_sum 其实是记录候选 max_sum ，然后和已有的max_sum 做比较
        如果前面的数的和是负数，那么对现在的数的作用就是负的，所以要算最大sub array 和就要抛弃前面的数的和
        """
        max_sum = nums[0]
        num_sum = 0
        for num in nums:
            num_sum += num
            max_sum = max(num_sum, max_sum)
            if num_sum < 0:
                num_sum = 0
        return max_sum


class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dynamic programming 未优化: https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
        关于动态规划问题详解：https://leetcode-cn.com/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
        """
        dp = [None] * len(nums)
        dp[0] = nums[0]
        for i, num in enumerate(nums[1:]):
            dp[i + 1] = max(num, dp[i] + num)
        return max(dp)


class Solution4:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dynamic programming 优化后: https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
        """
        curr = 0
        res = nums[0]
        for num in nums:
            curr = max(num, num + curr)
            res = max(curr, res)
        return res


class SegmentTreeNode(object):
    def __init__(self, start, end, lsum, rsum, isum, msum):
        self.start = start
        self.end = end
        self.lsum = lsum
        self.rsum = rsum
        self.isum = isum
        self.msum = msum


class SegmentTree(object):
    def _build_tree(self, nums, left, right):
        if left == right:
            return SegmentTreeNode(left, left, nums[left], nums[left], nums[left], nums[left])
        mid = (left + right) // 2
        left = self._build_tree(nums, left, mid)
        right = self._build_tree(nums, mid + 1, right)
        lsum = max(left.lsum, left.isum + right.lsum)
        rsum = max(right.rsum, right.isum + left.rsum)
        isum = left.isum + right.isum
        msum = max(left.msum, right.msum, left.rsum + right.lsum)
        # 下面这个return statement 相当于pushup() or push up
        return SegmentTreeNode(left, right, lsum, rsum, isum, msum)

    def __init__(self, nums):
        self.root = self._build_tree(nums, 0, len(nums) - 1)


class Solution5:
    """ segment tree:
    https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/ 
    https://leetcode-cn.com/problems/maximum-subarray/solution/cfen-zhi-suan-fa-qu-jian-er-fen-xian-duan-shu-jian/
    关于segment tree: https://www.youtube.com/watch?v=rYBtViWXYeI&ab_channel=HuaHua
    时间复杂度：假设我们把递归的过程看作是一颗二叉树的先序遍历，那么这颗二叉树的深度的渐进上界为 O(\log n)O(logn)，这里的总时间相当于遍历这颗二叉树的所有节点，故总时间的渐进上界是 O(\sum_{i=1}^{\log n} 2^{i-1})=O(n)O(∑ i=1logn2 −1)=O(n)，故渐进时间复杂度为 O(n)O(n)。
    空间复杂度：递归会使用 O(\log n)O(logn) 的栈空间，故渐进空间复杂度为 O(\log n)O(logn)

    """
    def maxSubArray(self, nums: List[int]) -> int:
        return SegmentTree(nums).root.msum

