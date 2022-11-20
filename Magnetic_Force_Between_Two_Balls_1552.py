class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """ binary search 特殊二分答案 最大化最小值、最小化最大值
        上下界多一点不重要，下面的上下界和二分法：https://juejin.cn/post/6864407058662457358
        max_ball_counts 写法根据https://leetcode.cn/problems/magnetic-force-between-two-balls/solution/c-er-fen-sou-suo-ying-gai-neng-gei-ni-jiang-ming-b/ 更好理解
        看我的 numbers 总结 
        """
        position.sort()
        def max_ball_counts(position, max_min_force):
            # 最小间距 >= given max_min_force 最多可以几颗球
            balls = 1
            pre = position[0]
            le = len(position)
            for i in range(le - 1):
                if position[i] - pre < max_min_force and position[i + 1] - pre >= max_min_force:
                    pre = position[i + 1]
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
