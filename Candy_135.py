class Solution:
    def candy(self, ratings: List[int]) -> int:
        ''' greedy 贪心 https://leetcode.cn/problems/candy/solution/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/
        # 若左规则解最小糖果数量为2，右边解最小糖果数量为4，那么要同时满足左右规则，要取x，y中最大的，才能满足两边的规则。要不然取3的话满足不了右规则，取5的又多余了。取4正好能满足两个规则，又是最少的。
        # 你先假设只有右边这一种情况下的最优值，然后你再加上左边这个条件。那么你左边的条件一定要比更新完右边的数组里的值大或者不变吧，你不可能把值缩小，如果你缩小了说明右边的符合条件被你破坏掉了。所以你在找左边的情况时，如果你更新的值比右边在这个点要小，那么就不能更新它。
        '''
        n = len(ratings)
        res = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                res[i] = res[i - 1] + 1
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                res[j] = max(res[j + 1] + 1, res[j])
        return sum(res)

        # my own solution:
        n = len(ratings)
        if n == 1:
            return 1
        res = [None] * n
        # 先找到所有局部最低点，取 1
        for i in range(0, n):
            if i == 0:
                if ratings[i] <= ratings[i + 1]:
                    res[i] = 1
            elif i == n - 1:
                if ratings[i] <= ratings[i - 1]:
                    res[i] = 1
            elif ratings[i] <= ratings[i + 1] and ratings[i] <= ratings[i - 1]:
                res[i] = 1
        #print(res)
        for i in range(0, n):
            if res[i] == 1:
                # 从 局部最低点 向左扫
                j = i - 1
                while j >= 0 and res[j] is None:
                    if ratings[j] > ratings[j + 1]:
                        res[j] = res[j + 1] + 1
                    else:
                        break
                    j -= 1
                # 如果 最后这个 j 点 （有可能是 另一个局部最低点 向右扫 后已经取值）ratings[j] > ratings[j + 1] 但是res 值 <= res[j + 1], 重新给 这个点 赋更大的值 这样 才能  j 左侧 右侧 都 满足条件, 比如 [1,6,10,8,7,3,2] 当j == 2
                if j >= 0 and ratings[j] > ratings[j + 1] and res[j] <= res[j + 1]:
                    res[j] = res[j + 1] + 1
                #print(res)
                # 从 局部最低点 向右扫
                k = i + 1
                while k < n and res[k] is None:
                    if ratings[k] > ratings[k - 1]:
                        res[k] = res[k - 1] + 1
                    else:
                        break
                    k += 1
        #print(res)
        return sum(res)
