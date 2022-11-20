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
