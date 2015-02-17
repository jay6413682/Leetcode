class MyCalendar:

    def __init__(self):
        """ brutal force/range query, https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-729-my-calendar-i/ """
        self.booked = []

    def _is_double_booking(self, s1, e1, s2, e2):
        # 画图可得
        """
        if max(s1, s2) < min(e1, e2):
            return True
        return False
        """
        if e2 <= s1 or e1 <= s2:
            return False
        return True

    def book(self, start: int, end: int) -> bool:
        for b in self.booked:
            if self._is_double_booking(b[0], b[1], start, end):
                return False
        self.booked.append([start, end])
        return True


from sortedcontainers import SortedDict
class MyCalendar2:
    def __init__(self):
        self.end_start = SortedDict()

    def book(self, start: int, end: int) -> bool:
        """ TreeMap/avl 平衡树/binary search
        solution: https://leetcode-cn.com/problems/my-calendar-i/solution/cpython3java-you-xu-zi-dian-by-hanxin_ha-4m8z/
        画图理解，另外：e.g.
        >>> sd = SortedDict(((20,15),(12,10),(13,12)))
        >>> sd.bisect_right(12)
        1
        >>> sd.values()[1]
        12
        >>> sd.bisect_right(17)
        2
        >>> sd.values()[2]
        15
        >>> sd.bisect_right(8)
        0
        >>> sd.values()[0]
        10

        https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.bisect_right
        有點像的一個 binary search 解：https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-729-my-calendar-i/
        另一個不太像的binary search 解：https://leetcode-cn.com/problems/my-calendar-i/solution/python-er-fen-cha-zhao-by-daxin-2021-r1rb/
        画图帮助理解
        """
        # log n
        ID = self.end_start.bisect_right(start)
        if 0 <= ID < len(self.end_start):
            # q.start < largest existing ends
            # ID is the index associated with first existing end that's larger than q.start
            if self.end_start.values()[ID] < end:
                # q.end > the start of first existing end that's larger than q.start
                return False
        self.end_start[end] = start
        return True

'''
解法3:线段树：https://leetcode-cn.com/problems/my-calendar-i/solution/xian-duan-shu-he-er-cha-sou-suo-shu-by-shi-huo-de-/
平衡树其实是线段树的解：https://leetcode-cn.com/problems/my-calendar-i/solution/wo-de-ri-cheng-an-pai-biao-i-by-leetcode/
'''