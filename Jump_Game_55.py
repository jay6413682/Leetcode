class Solution:
    def jump(self, nums: List[int]) -> int:
        """ greedy 贪心 https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html#%E6%96%B9%E6%B3%95%E4%BA%8C
        这里需要统计两个覆盖范围，当前这一步的最大覆盖和下一步最大覆盖。
        如果移动下标达到了当前这一步的最大覆盖最远距离了，还没有到终点的话，那么就必须再走一步来增加覆盖范围，直到覆盖范围覆盖了终点。
        """
        stop = 0 # stop：当前覆盖最远距离下标
        n = len(nums)
        if n == 1:
            return 0
        min_jumps = 0
        i = 0
        new_stop = 0
        while True:
            # new_stop: 下一步覆盖最远距离下标
            new_stop = max(new_stop, i + nums[i]) # 更新下一步覆盖最远距离下标
            if i == stop: # 遇到当前覆盖最远距离下标
                stop = new_stop # 更新当前覆盖最远距离下标
                min_jumps += 1 # 需要走下一步
            i += 1
            if stop >= n - 1: # 下一步的覆盖范围已经可以达到终点，结束循环
                return min_jumps
