
from sortedcontainers import SortedDict

class MyCalendarThree2:

    def __init__(self):
        # delta event counter at a specific time
        self.delta_event_counter = SortedDict()

    def book(self, start: int, end: int) -> int:
        """ range query
        https://zxi.mytechroad.com/blog/geometry/732-my-calendar-iii/ 解法一
        类似 731解法
        注意此题不能剪枝，因为最大值也许在end 后面某区间出现，不同于731
        Time Complexity: O(n^2)

        Space Complexity: O(n)

        """
        if start not in self.delta_event_counter:
            self.delta_event_counter[start] = 1
        else:
            self.delta_event_counter[start] += 1
        if end not in self.delta_event_counter:
            self.delta_event_counter[end] = -1
        else:
            self.delta_event_counter[end] -= 1
        max_counter = 0
        counter = 0
        for time, count in self.delta_event_counter.items():
            counter += count
            max_counter = max(max_counter, counter)

        return max_counter

'''
https://zxi.mytechroad.com/blog/geometry/732-my-calendar-iii/ 解法二
比较抽象，不好理解
俄罗斯方块  可画图帮助理解 实际是三角形 不是方块 高度维护的是起始点的值  ++next： 表示iterator 的key 到下一个，并不是加一
思路类似segment tree，但是数据结构不一样
'''


class SegmentNode(object):
    def __init__(self, l, r, count=0, m=-1, left=None, right=None):
        self.l = l
        self.r = r
        self.m = m
        self.count = count
        self.left = left
        self.right = right

class MyCalendarThree:

    def __init__(self):
        self.root = SegmentNode(0, 10^9)
        self.max_count = 0

    def add(self, root, start, end):
        """ segment tree; 线段树
        https://www.youtube.com/watch?v=yK9a-rT3FBQ&ab_channel=HuaHua
        http://zxi.mytechroad.com/blog/geometry/732-my-calendar-iii/ 
        time complexity Time complexity: 
        O(n^2)
        Space complexity: O(n)
        具體要看https://www.youtube.com/watch?v=yK9a-rT3FBQ&ab_channel=HuaHua 解法1 2詳解
        """
        # no m created, no childs
        if root.m == -1:
            if root.l == start and root.r == end:
                # found
                root.count += 1
                self.max_count = max(self.max_count, root.count)
            elif root.l == start:
                # left match, create child nodes
                root.m = end
                root.left = SegmentNode(start, end, root.count + 1)
                root.right = SegmentNode(end, root.r, root.count)
                self.max_count = max(self.max_count, root.left.count)
            elif root.r == end:
                # right match, create child nodes
                root.m = start
                root.left = SegmentNode(root.l, start, root.count)
                root.right = SegmentNode(start, end, root.count + 1)
                self.max_count = max(self.max_count, root.right.count)
            else:
                # in the middle
                root.m = start
                root.left = SegmentNode(root.l, start, root.count)
                root.right = SegmentNode(start, root.r, root.count)
                # add to the right child
                self.add(root.right, start, end)
        else:
            # m exists, start to search
            if root.m <= start:
                # search right child
                self.add(root.right, start, end)
            elif root.m >= end:
                # search left child
                self.add(root.left, start, end)
            else:
                # in the middle
                self.add(root.left, start, root.m)
                self.add(root.right, root.m, end)

    def book(self, start: int, end: int) -> int:
        self.add(self.root, start, end)
        return self.max_count


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)