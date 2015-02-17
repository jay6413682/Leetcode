from heapq import heappush, heappop, heappushpop, heapify
from typing import List
class KthLargest:
    """ my first solution, 超出时间限制 """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        i = 0
        n = len(self.nums)
        if n == 0:
            self.nums.append(val)
        else:
            while i < n:
                if val <= self.nums[i]:
                    self.nums.insert(i, val)                    
                    break
                elif i == n - 1:
                    self.nums.append(val)
                    break
                i += 1
        return self.nums[-1 * self.k]


class KthLargest2:
    """ priority queue; use min heap; heapq: https://docs.python.org/3/library/heapq.html 
    close to https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/solution/python-dong-hua-shou-xie-shi-xian-dui-by-ypz2/

    初始化时间复杂度为：O(n \log k)O(nlogk) ，其中 nn 为初始化时 \textit{nums}nums 的长度；

    单次插入时间复杂度为：O(\log k)O(logk)。

    空间复杂度：O(k)O(k)。需要使用优先队列存储前 kk 大的元素。

    https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/solution/shu-ju-liu-zhong-de-di-k-da-yuan-su-by-l-woz8/
    """

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.h_nums = nums
        self.k = k
        while len(self.h_nums) > k:
            heappop(self.h_nums)

    def add(self, val: int) -> int:
        if len(self.h_nums) < self.k:
            heappush(self.h_nums, val)
        # if len(self.h_nums) == self.k - 1:
        #    heappush(self.h_nums, val)
        elif val > self.h_nums[0]:
            heappushpop(self.h_nums, val)
        return self.h_nums[0]
    '''
    # my other solution
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.h_nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.h_nums, val)
        while len(self.h_nums) > self.k:
            heappop(self.h_nums)
        return self.h_nums[0]
    '''

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None, count=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = count

class KthLargest:
    """ similar to BST solution, not a recursive but iterative add() implementation: https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/solution/python3er-cha-sou-suo-shu-shu-ju-liu-zhong-de-di-k/
    还可以继续优化
    时间复杂度：O(H)，H为二叉搜索树的深度；
    空间复杂度：O(H)，H为递归栈的深度，也是二叉搜索树的深度；
    若二叉搜索树元素个数为N，则平均可达到O(logN)的复杂度； - master theory
    故若维持的二叉搜索树元素个数较小，能较好地降低算法复杂度。

    """
    def _insert_to_bts(self, root, num):
        if not root:
            return TreeNode(num, count=1)
        else:
            if num < root.val:
                root.left = self._insert_to_bts(root.left, num)
            else:
                root.right = self._insert_to_bts(root.right, num)
            root.count += 1
        return root

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # create bst
        self.bst_root = None
        self.kth_large = None
        for num in nums:
            self.bst_root = self._insert_to_bts(self.bst_root, num)

    def add(self, val: int) -> int:
        if self.kth_large and val <= self.kth_large:
            return self.kth_large
        self.bst_root = self._insert_to_bts(self.bst_root, val)
        node = self.bst_root
        k = self.k
        while node:
            if node.right and k < node.right.count + 1:
                node = node.right
            elif node.right and k == node.right.count + 1 or (not node.right and k == 1):
                self.kth_large = node.val
                return node.val
            elif node.right and k > node.right.count + 1 or (not node.right and k > 1):
                if node.right:
                    k = k - (node.right.count + 1)
                else:
                    k = k - 1
                node = node.left
            else:
                # not node.right and self.k < 1:
                raise Exception('Since there must be a kth largest, we should never reach here')
