class SegmentTreeNode(object):
    def __init__(self, sum_val, start, end, left=None, right=None):
        self.sum_val = sum_val
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class NumArray:
    """ 线段树；Segment Tree https://www.youtube.com/watch?v=rYBtViWXYeI&ab_channel=HuaHua
    复杂度：master theorem
    build_tree: time:  最后一层工作量 O(n^logba)-> O(n) space: stack, log(n)
    update: time: 每层工作量一样 O(n^d*logn) ->O(logn). space: stack log(n)
    sumRange: time: 每层工作量一样 O(n^d*logn) ->O(logn). space: stack log(n)
    """

    def build_tree(self, start, end, nums):
        if start == end:
            return SegmentTreeNode(nums[start], start, end)
        mid = (start + end) // 2
        left = self.build_tree(start, mid, nums)
        right = self.build_tree(mid + 1, end, nums)
        return SegmentTreeNode(left.sum_val + right.sum_val, start, end, left, right)

    def __init__(self, nums: List[int]):
        # build the segment tree
        self.root = self.build_tree(0, len(nums) - 1, nums)
        # print(self.root.sum_val, self.root.start, self.root.end)

    def update(self, index: int, val: int) -> None:
        def _update(root, i, val):
            if root.start == root.end == index:
                root.sum_val = val
                return
            mid = (root.start + root.end) // 2
            if i <= mid:
                _update(root.left, i, val)
            else:
                _update(root.right, i, val)
            root.sum_val = root.left.sum_val + root.right.sum_val

        _update(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def _sum_range(root, left, right):
            if left == root.start and right == root.end:
                return root.sum_val
            mid = (root.start + root.end) // 2
            if right <= mid:
                total = _sum_range(root.left, left, right)
            elif left > mid:
                total = _sum_range(root.right, left, right)
            else:
                total = _sum_range(root.left, left, mid) + _sum_range(root.right, mid + 1, right)
            return total
        return _sum_range(self.root, left, right)
        '''
        # or similarly
        def dfs(root, left, right):
            if root and root.start == left and root.end == right:
                return root.sum_val
            left_start = root.left.start
            left_end = root.left.end
            right_start = root.right.start
            right_end = root.right.end
            if left >= left_start and right <= left_end:
                return dfs(root.left, left, right)
            elif right <= right_end and left >= right_start:
                return dfs(root.right, left, right)
            else:
                # print(left, right, left_end, right_start)
                return dfs(root.left, left, left_end) + dfs(root.right, right_start, right)
        return dfs(self.root, left, right)
        '''


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
