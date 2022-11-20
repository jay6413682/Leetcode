class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """ 离散化/暴力/超时
        https://leetcode-cn.com/problems/the-skyline-problem/solution/tian-ji-xian-wen-ti-cong-bao-li-dao-you-hua-by-jie/
        时间复杂度：O(n^2)O(n 2)，空间复杂度：O(n)O(n)。
        """
        # 离散化x 坐标
        # # 根据JinFish/带带大师兄的問題：请问一下怎么处理这种情况：[4, 9, 15], [10, 12, 10] 。第一个区间的右端点+1恰好等于第二个区间的左端点， jie的回答
        xs = set()
        for building in buildings:
            xs.add(building[0] * 2)
            xs.add(building[1] * 2)
        xs = list(xs)
        temp_xs = sorted(xs)
        for x in temp_xs:
            if x + 1 not in temp_xs:
                xs.append(x + 1)
        xs.sort()
        # 上缘x y 坐标
        xys = defaultdict(int)
        for building in buildings:
            for x in range(2 * building[0], 2 * building[1] + 1):
                xys[x] = max(xys[x], building[2])
        # print(xys)
        # skyline
        res = []
        # print(xs, xys)
        for x in xs:
            y = xys[x]
            if not res:
                res.append([x // 2, y])
            else:
                last_y = res[-1][1]
                if last_y < y:
                    # 上升
                    res.append([x // 2, y])
                elif last_y > y:
                    # 下降
                    res.append([x // 2, y])
        return res


class SegmentTreeNode:
    def __init__(self, start, end, max_val, lazy_notation, left=None, right=None):
        self.start = start
        self.end = end
        self.max_val = max_val
        # lazy notation，懒惰标记：
        # https://www.acwing.com/blog/content/1684/
        # https://zhuanlan.zhihu.com/p/350443545
        self.lazy_notation = lazy_notation
        self.left = left
        self.right = right


class SegmentTree:

    def push_down(self, root):
        # push down，懒惰标记下传一层
        # https://www.acwing.com/blog/content/1684/
        if root.lazy_notation:
            root.left.max_val = max(root.lazy_notation, root.left.max_val)
            root.right.max_val = max(root.lazy_notation, root.right.max_val)
            root.left.lazy_notation = max(root.lazy_notation, root.left.lazy_notation)
            root.right.lazy_notation = max(root.lazy_notation, root.right.lazy_notation)
            root.lazy_notation = 0

    def update_segment(self, root, start, end, val):
        # 区间更新 segment update
        # https://www.acwing.com/blog/content/1684/
        if root.start == start and root.end == end:
            root.max_val = max(val, root.max_val)
            root.lazy_notation = max(val, root.lazy_notation)
        else:
            self.push_down(root)
            mid = (root.start + root.end) // 2
            if mid >= end:
                self.update_segment(root.left, start, end, val)
            elif mid < start:
                self.update_segment(root.right, start, end, val)
            else:
                self.update_segment(root.left, start, mid, val)
                self.update_segment(root.right, mid + 1, end, val)
            root.max_val = max(root.max_val, val)

    def init_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, start, 0, 0)
        mid = (start + end) // 2
        left = self.init_tree(start, mid)
        right = self.init_tree(mid + 1, end)
        return SegmentTreeNode(start, end, 0, 0, left=left, right=right)

    def __init__(self, buildings):
        bds = set()
        # 离散化Discretization，在相差大于1的数间加一个数, sort and unique the given buildings
        # https://www.cnblogs.com/qlky/articles/5716796.html
        # # 根据JinFish/带带大师兄的問題：请问一下怎么处理这种情况：[4, 9, 15], [10, 12, 10] 。第一个区间的右端点+1恰好等于第二个区间的左端点， jie的回答:
        # 实在抱歉这么久了才回复你，最近有点忙，没看到你的评论。不过你提的问题很好，确实我所有的解法都不能通过这个用例，不过直观上来说，造成这个问题的根源在于+1这个操作使得两个区间刚好连起来了，那么解决方法就是，我们能否+0.5使得两个区间不会连起来？显然不太方便，那不妨所有输入的点都*2吧：
        for building in buildings:
            bds.add(building[0] * 2)
            bds.add(building[1] * 2)
        self.bds = sorted(list(bds))
        for bd in bds:
            if bd + 1 not in bds:
                self.bds.append(bd + 1)
        self.bds = sorted(list(self.bds))
        # 初始化segment tree ，value = 0
        self.root = self.init_tree(0, len(self.bds) - 1)
        # 区间更新 segment update
        for building in buildings:
            # 根据JinFish/带带大师兄的問題：请问一下怎么处理这种情况：[4, 9, 15], [10, 12, 10] 。第一个区间的右端点+1恰好等于第二个区间的左端点， jie的回答
            self.update_segment(self.root, self.bds.index(building[0] * 2), self.bds.index(building[1] * 2), building[2])

    def query(self, root, index):
        # 單點查詢，single point search
        # https://leetcode-cn.com/problems/the-skyline-problem/solution/tian-ji-xian-wen-ti-cong-bao-li-dao-you-hua-by-jie/
        if index == root.start == root.end:
            return root.max_val
        # 查询时push down
        # https://www.acwing.com/blog/content/1684/
        self.push_down(root)
        mid = (root.start + root.end) // 2
        if index <= mid:
            return self.query(root.left, index)
        else:
            return self.query(root.right, index)


class Solution1:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """ 线段树/segement tree https://leetcode-cn.com/problems/the-skyline-problem/solution/tian-ji-xian-wen-ti-cong-bao-li-dao-you-hua-by-jie/
        master theory ： 时间复杂度：O(n\log{n})O(nlogn)，空间复杂度：O(n)O(n) - 最壞4n - 1: https://blog.csdn.net/DREAM_yao/article/details/108801613; 最好：2n ： https://www.jianshu.com/p/91f2c503e62f
        """
        st = SegmentTree(buildings)
        res = []
        # print(st.bds)
        for i, bd in enumerate(st.bds):
            # query 每个离散点的高度
            h = st.query(st.root, i)
            # print(h)
            if not res:
                res.append([bd // 2, h])
            else:
                if h < last_h:
                    # 例如 如果输入为[[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]]
                    # x * 2 后 18 高度为 15， 19 高度为0，18对应的9的天际线应该标记为0
                    res.append([(bd - 1) // 2, h])
                elif h > last_h:
                    res.append([bd // 2, h])
            last_h = h
        return res


from sortedcontainers import SortedList


class Solution2:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """ 扫描线，priority queue， Benhao comment ： https://leetcode-cn.com/problems/the-skyline-problem/solution/gong-shui-san-xie-sao-miao-xian-suan-fa-0z6xc/  sortedlist好像不是大根堆而是有序统计树（红黑树）。所以搜索value再remove的时间复杂度是logn. 在python 里总体的时间复杂度是O(nlog(n))
        heapq 没有 remove 所以用红黑树 做的 SortedList
        详解：https://leetcode-cn.com/problems/the-skyline-problem/solution/gong-shui-san-xie-sao-miao-xian-suan-fa-0z6xc/
        要根据题目中第一个例子照着解题过一遍便于理解
        """
        res = []
        points = [] 
        for left, right, height in buildings:
            points.append((left, -height))
            points.append((right, height))
        points.sort()
        prev = 0
        sorted_list = SortedList([prev])
        for point in points:
            if point[1] < 0:
                sorted_list.add(-point[1])
            else:
                sorted_list.remove(point[1])
            # 如果point左端點，若point高 <= prev天际线, curr天际线 则 = prev天际线, 什么都不做；若point高 > prev 天际线(上坡), so curr天际线 > prev天际线，把curr天际线 加入res
            # 如果point右端点，若point高 < prev天际线, curr天际线 则 = prev天际线，什么都不做；若point高 = prev天际线，如果没有其他同高point, so curr天际线 < prev天际线, 把curr天际线 加入 res
            curr = sorted_list[-1]
            # curr: 现在的最大值（天际线） 不等于 以前的 天际线
            if curr != prev:
                res.append([point[0], curr])
                prev = curr
        return res
        '''
        # https://leetcode-cn.com/problems/the-skyline-problem/solution/you-xian-dui-lie-java-by-liweiwei1419-jdb5/
        # 要根据题目中第一个例子照着解题过一遍便于理解
        res = []
        points = [] 
        for left, right, height in buildings:
            points.append((left, -height))
            points.append((right, height))
        points.sort()
        prev = 0
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        delay = defaultdict(int)
        priority_queue = []
        # heapq: max heap, push negative, so pop the smallest num
        heapq.heappush(priority_queue, -prev)
        for point in points:
            if point[1] < 0:
                heapq.heappush(priority_queue, point[1])
            else:
                delay[point[1]] += 1
            # 如果堆顶元素在延迟删除集合中，才真正删除，这一步可能执行多次，所以放在 while 中
            # while (true) 都是可以的，因为 maxHeap 一定不会为空
            # 根据规则二 堆顶（最大）元素不可能是关键点，需要将它从优先队列中删除
            while True:
                curr = -priority_queue[0]
                if curr in delay:
                    delay[curr] -= 1
                    if delay[curr] == 0:
                        delay.pop(curr)
                    heapq.heappop(priority_queue)
                else:
                    break
            curr = -priority_queue[0]
            # 前后天际线有高度差，才有关键点出现
            if curr != prev:
                res.append([point[0], curr])
                prev = curr
                # print(res)
        return res
        '''

