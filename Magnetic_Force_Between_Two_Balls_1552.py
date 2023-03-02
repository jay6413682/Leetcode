class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """ binary search 特殊二分答案 最大化最小值、最小化最大值
        上下界多一点不重要，下面的上下界和二分法：https://juejin.cn/post/6864407058662457358
        max_ball_counts ： 相邻小球的间距最小值大于等于 x，其实就等价于相邻小球的间距均大于等于 x。https://leetcode.cn/problems/magnetic-force-between-two-balls/solution/liang-qiu-zhi-jian-de-ci-li-by-leetcode-solution/
        看我的 numbers 总结 
        """
        position.sort()
        def max_ball_counts(position, max_min_force):
            # 最小间距 >= given max_min_force 最多可以几颗球， 这个不好理解
            # https://leetcode.cn/problems/magnetic-force-between-two-balls/solution/c-er-fen-sou-suo-ying-gai-neng-gei-ni-jiang-ming-b/
            balls = 1
            pre = position[0]
            le = len(position)
            for i in range(1, le):
                if position[i] - pre < max_min_force and position[i + 1] - pre >= max_min_force:
                    pre = position[i + 1]
                    balls += 1
            return balls
        
        def max_ball_counts(position, max_min_force):
            # 最小间距 >= given max_min_force 最多可以几颗球. 这个更好理解
            #  相邻小球的间距最小值大于等于 x，其实就等价于相邻小球的间距均大于等于 x
            # 0 index 一定会选中：如果下一个球 和 0 间距 >= max_min_force, 那么选中 0 index 和 下一个球
            # 如果下一个球和 0 间距 < max_min_force, 继续找 知道找到 下一个间距 >= max_min_force。但是无论如何 0 index 也选中了
            # 假设 不选 0 index，那么可选范围就缩小了，有risk 可能选少了球 （除非可以往前 选球？也许结果也一样？）
            balls = 1
            pre = position[0]
            le = len(position)
            for i in range(1, le):
                if position[i] - pre >= max_min_force:
                    pre = position[i]
                    balls += 1
            return balls

        left = 1
        right = position[-1] - position[0] # max(position) - min(position)
        while left < right:
            mid = (left + right + 1) // 2
            balls = max_ball_counts(position, mid)
            # 如果球不够，要增加球，就要减少间距
            if balls < m:
                right = mid - 1
            else:
                left = mid
        '''
        # or:
        while left < right:
            mid = (left + right) // 2
            balls = ball_counts(position, mid)
            if balls > m:
                left = mid + 1
            else:
                right = mid
        '''
        return left
