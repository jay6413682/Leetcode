class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """ 二分答案 binary search 与1283 题相同 https://leetcode.cn/problems/koko-eating-bananas/solution/er-fen-cha-zhao-ding-wei-su-du-by-liweiwei1419/
        https://leetcode.cn/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/ ：
        目标变量和另一个变量有相关关系（一般是线性关系），目标变量的性质不好推测，但是另一个变量的性质相对容易推测（满足某种意义上的单调性）。这样的问题的判别函数通常会写成一个函数的形式。
        目标变量：吃的速度k
        另一个变量：总时长
        这一类问题可以统称为「 最大值极小化 」问题，
        """
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            s = 0
            for p in piles:
                s += (p + mid - 1) // mid
            if s <= h:
                right = mid
            else:
                left = mid + 1
        return left