class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """ greedy 贪心：https://programmercarl.com/0860.%E6%9F%A0%E6%AA%AC%E6%B0%B4%E6%89%BE%E9%9B%B6.html#%E6%80%9D%E8%B7%AF
        有如下三种情况：

        情况一：账单是5，直接收下。
        情况二：账单是10，消耗一个5，增加一个10
        情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5
        此时大家就发现 情况一，情况二，都是固定策略，都不用我们来做分析了，而唯一不确定的其实在情况三。

        而情况三逻辑也不复杂甚至感觉纯模拟就可以了，其实情况三这里是有贪心的。

        账单是20的情况，为什么要优先消耗一个10和一个5呢？

        因为美元10只能给账单20找零，而美元5可以给账单10和账单20找零，美元5更万能！

        所以局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零。

        局部最优可以推出全局最优，并找不出反例，那么就试试贪心算法！


        """
        fives = tens = twenties = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives:
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                    twenties += 1
                elif fives >= 3:
                    fives -= 3
                    twenties +=1
                else:
                    return False
        return True
