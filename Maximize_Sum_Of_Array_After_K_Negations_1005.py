class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """ greedy 贪心
        https://programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html#%E6%80%9D%E8%B7%AF
        本题思路其实比较好想了，如何可以让数组和最大呢？

        贪心的思路，局部最优：让绝对值大的负数变为正数，当前数值达到最大，整体最优：整个数组和达到最大。

        局部最优可以推出全局最优。

        那么如果将负数都转变为正数了，K依然大于0，此时的问题是一个有序正整数序列，如何转变K次正负，让 数组和 达到最大。

        那么又是一个贪心：局部最优：只找数值最小的正整数进行反转，当前数值和可以达到最大（例如正整数数组{5, 3, 1}，反转1 得到-1 比 反转5得到的-5 大多了），全局最优：整个 数组和 达到最大。

        虽然这道题目大家做的时候，可能都不会去想什么贪心算法，一鼓作气，就AC了。

        我这里其实是为了给大家展现出来 经常被大家忽略的贪心思路，这么一道简单题，就用了两次贪心！

        那么本题的解题步骤为：

        第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
        第二步：从前向后遍历，遇到负数将其变为正数，同时K--
        第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
        第四步：求和
        """
        nums.sort()
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                k -= 1
                nums[i] = -nums[i]
        nums.sort()
        if k % 2 == 1:
            nums[0] = -nums[0]
        return sum(nums)