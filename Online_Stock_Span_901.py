class StockSpanner:

    def __init__(self):
        # 单调栈mono stack: https://blog.csdn.net/Hanx09/article/details/108434955
        # 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）
        # 我的解，先把哨兵 sentinel 第0天 加入栈，这样第一天的span 就是 1 了 ，而不是0
        self.stack = [0]
        self.prices = [0]
        self.i = 0

    def next(self, price: int) -> int:
        self.prices.append(price)
        self.i += 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        if self.stack:
            span = self.i - self.stack[-1]
        else:
            span = self.i
        self.stack.append(self.i)
        return span

class StockSpanner:
    # 单调栈mono stack 。不初始化0的解
    def __init__(self):
        self.stack = []
        self.nums = []
    '''
    # timed out. 
    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.nums[self.stack[-1]] <= price:
            self.stack.pop()
            res += 1
        self.nums.append(price)
        self.stack = [i for i in range(len(self.nums))]
        return res
    '''
    # my latest try
    def next(self, price: int) -> int:
        current_i = len(self.nums)
        while self.stack and self.nums[self.stack[-1]] <= price:
            self.stack.pop()
        self.nums.append(price)
        if self.stack:
            res = current_i - self.stack[-1]
        else:
            res = current_i + 1
        self.stack.append(current_i)
        return res