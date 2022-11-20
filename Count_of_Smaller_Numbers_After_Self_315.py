# （了解）树状数组解：
# 关于树状数组，视频：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/shu-zhuang-shu-zu-by-liweiwei1419/
# 具体解法：问题分析部分，树状数组解决方法部分，尤其是幻灯片，关键是 - A[i]：统计“当前遇到数字的出现次数”的数组，所以问题转化为求前缀和（：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/shu-zhuang-shu-zu-de-xiang-xi-fen-xi-by-yangbingji/
# 复杂度https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/：时间复杂度：我们梳理一下这个算法的流程，这里离散化使用哈希表去重，然后再对去重的数组进行排序，时间代价为 O(n \log n)O(nlogn)；初始化树状数组的时间代价是 O(n)O(n)；通过值获取离散化 \rm idid 的操作单次时间代价为 O(\log n)O(logn)；对于每个序列中的每个元素，都会做一次查询 \rm idid、单点修改和前缀和查询，总的时间代价为 O(n \log n)O(nlogn)。故渐进时间复杂度为 O(n \log n)O(nlogn)。
# 空间复杂度：这里用到的离散化数组、树状数组、哈希表的空间代价都是 O(n)O(n)，故渐进空间复杂度为 O(n)O(n)。

class BinaryIndexedTree(object):
    """ 树状数组 binary indexed tree ，Fenwick Tree  https://leetcode.cn/problems/count-of-smaller-numbers-after-self/solution/shu-zhuang-shu-zu-by-liweiwei1419/ 

    性质：
    C 数组 index 的二进制表示的最低位的 1 和 后面的 0 转化成十进制，就是 index 对应 C 节点管理的A 节点个数 （更重要）
    C 数组 index 的二进制表示的最低位 1 后面的 0 的个数决定了，当前结点在第几层

    """
    def __init__(self, size):
        self.size = size
        # C数组：
        self.data = [0 for _ in range(size + 1)]

    def update(self, i, delta):
        # 单点更新 my recursive solution
        if i > self.size:
            return
        self.data[i] += delta
        # 子节点到父节点路径唯一
        # 子节点 index + its lowbit = 父节点 index
        parent_i = i + (i & (-i))
        self.update(parent_i, delta)
    
    def prefix_sum(self, i):
        # 查询前缀和 ， my recursive solution
        if i <= 0 :
            return 0
        lowbit = i & (-i)
        # index 进行二进制分解，可以转化成 多个100... （lowbit） 形式的 二进制数 之和，而index 正好是 管理的A 节点个数
        # 另外 已知 index 的二进制表示的最低位的 1 和 后面的 0 转化成十进制，就是 index 对应 C 节点管理的A 节点个数 
        # 所以每一次 index - lowbit ，prefix sum 就 + C[index]
        next_i = i - lowbit
        return self.prefix_sum(next_i) + self.data[i]



class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        复杂度分析 ： https://leetcode.cn/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/

    假设题目给出的序列长度为 n

    时间复杂度：我们梳理一下这个算法的流程，这里离散化使用哈希表去重，然后再对去重的数组进行排序，时间代价为 O(nlogn)；初始化树状数组的时间代价是 O(n)；通过值获取离散化 id 的操作单次时间代价为 O(logn)；对于每个序列中的每个元素，都会做一次查询 id、单点修改和前缀和查询，总的时间代价为 O(nlogn)。故渐进时间复杂度为 O(nlogn)。
    空间复杂度：这里用到的离散化数组、树状数组、哈希表的空间代价都是 O(n)，故渐进空间复杂度为 O(n)。
        """
        # A(i): 大小排名为i的元素的出现个数 (排名1为最小的树)
        # C(i): 对应的binary indexed tree
        size = len(nums)
        s = list(set(nums))
        s_size = len(s)
        tree = BinaryIndexedTree(size)
        # 用 heap 和 hashmap 来 离散化
        heapify(s)
        rank = 1
        rank_map = {}
        while s:
            smallest = heappop(s)
            rank_map[smallest] = rank
            rank += 1
        res = [None] * size
        for i in range(size - 1, -1, -1):
            rank = rank_map[nums[i]]
            #print(rank, i, nums[i])
            res[i] = tree.prefix_sum(rank - 1)
            tree.update(rank, 1)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """ inversion pair 逆序对 merge sort 归并排序 my latest solution 
        根据逆序对解法一 数出每一个数前面有多少个数比它大：左大右小且右侧没有iterate完，count += (mid - i + 1) -> 左大右小且右侧没有iterate完，前面比它大的每一个数count + 1
        """
        n = len(nums)
        count = [0] * n
        # 也可以 创建 index_nums = [(i, nums[i]) for i in range(n)]: 一种可行的办法是：把「下标」和「数值」绑在一起进行归并排序，在一些编程语言中提供了 Tuple 和 Pair 这样的类可以实现，也可以自己创建一个类。https://leetcode.cn/problems/count-of-smaller-numbers-after-self/solution/gui-bing-pai-xu-suo-yin-shu-zu-python-dai-ma-java-/ 
        # 或者不用 排序 nums 而是 只排序 indexes

        index_nums = [i for i in range(n)]
        def merge_sort(nums, left, right, index_nums):
            # special case
            nonlocal count
            if left == right:
                return
            mid = (left + right) // 2
            # divide
            merge_sort(nums, left, mid, index_nums)
            merge_sort(nums, mid + 1, right, index_nums)

            if nums[mid] <= nums[mid + 1]:
                return
            
            i = left
            j = mid + 1
            tmp = nums.copy()
            index_nums_copy = index_nums.copy()
            k = i
            while i <= mid and j <= right:
                if nums[i] > nums[j]:
                    # 左大
                    tmp[k] = nums[j]
                    for m in range(i, mid + 1):
                        count[index_nums[m]] += 1
                    #count += (mid - i + 1)
                    index_nums_copy[k] = index_nums[j]
                    j += 1
                    #print('>',count, k,j, left, mid, right, (j - (mid + 1)))
                else:
                    # 左小
                    tmp[k] = nums[i]
                    index_nums_copy[k] = index_nums[i]
                    i += 1
                k += 1
            current_i = i
            while i <= mid:
                tmp[k] = nums[i]
                index_nums_copy[k] = index_nums[i]
                k += 1
                i += 1
            while j <= right:
                tmp[k] = nums[j]
                index_nums_copy[k] = index_nums[j]
                k += 1
                j += 1
            for i in range(left, right + 1):
                nums[i] = tmp[i]
                index_nums[i] = index_nums_copy[i]
            #print(nums)
        if not nums:
            return count
        merge_sort(nums, 0, n - 1, index_nums)
        #print(nums)
        return count



class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """ merge sort；类似https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/ （数组中的逆序对）
        对应下面视频题解中的 计算数组的”逆序对“个数示意图 1
        视频：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/gui-bing-pai-xu-suo-yin-shu-zu-python-dai-ma-java-/
        对应计算数组的“逆序对”个数示意图 2 (修改：说明：5出列时，后有序数组中已出列的元素都小于5)
        我的解答类似：hadyang https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/gui-bing-pai-xu-suo-yin-shu-zu-python-dai-ma-java-/ 只是计算count[index[i]] 不同
        索引堆：https://juejin.cn/post/6844903618609414157
        时间复杂度：O(N \log N)O(NlogN)，数组的元素个数是 NN，递归执行分治法，时间复杂度是对数级别的，因此时间复杂度是 O(N \log N)O(NlogN)。
        空间复杂度：O(N)O(N)，需要 33 个数组，一个索引数组，一个临时数组用于索引数组的归并，还有一个结果数组，它们的长度都是 NN，故空间复杂度是 O(N)O(N)。
        """
        n = len(nums)
        # 索引数组：改变索引数组，不改变nums。操作的是索引，比较的是索引对应的原始数组的值
        self.indexes = [i for i in range(n)]
        # 临时索引数组
        self.new_indexes = [i for i in range(n)]
        self.res = [0 for _ in nums]
        def merge_and_count(nums, left, right):
            if left == right:
                return
            mid = (left + right) // 2
            # divide
            merge_and_count(nums, left, mid)
            merge_and_count(nums, mid + 1, right)
            # 若左侧升序数组都小于右侧，则不需找右侧比左侧小的情况
            if nums[self.indexes[mid]] <= nums[self.indexes[mid + 1]]:
                return
            # 索引数组也好，原数组也好，其比较的左右范围是一样的
            i = left
            j = mid + 1
            x = left
            # merge and count
            while i <= mid and j <= right:
                # 原数组nums位置不变，通过索引数组来确定比较哪个数
                if nums[self.indexes[i]] <= nums[self.indexes[j]]:
                    self.new_indexes[x] = self.indexes[i]
                    # res 数组与原数组nums 位置一致，所以通过索引数组来确定加哪个位置
                    # j - mid - 1：看https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/gui-bing-pai-xu-suo-yin-shu-zu-python-dai-ma-java-/视频
                    self.res[self.indexes[i]] += j - mid - 1
                    x += 1
                    i += 1
                else:
                    self.new_indexes[x] = self.indexes[j]
                    x += 1
                    j += 1
            # 若右侧有剩余，直接copy index 到new_indexes
            if i > mid:
                while j <= right:
                    self.new_indexes[x] = self.indexes[j]
                    x += 1
                    j += 1
             # 若左侧有剩余，copy index 到new_indexes，另外，由于右侧数都小于左侧，所以加right - mid
            if j > right:
                while i <= mid:
                    self.new_indexes[x] = self.indexes[i]
                    self.res[self.indexes[i]] += right - mid
                    i += 1
                    x += 1
            # 把temp indexes copy 到 indexes
            self.indexes[:] = self.new_indexes
        merge_and_count(nums, 0, n - 1)
        return self.res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """ my solution, not efficient, time complexity o(n^2), space complexity o(n) """
        res = []
        i = 0
        m = len(nums)
        while i < m:
            j = i + 1
            counter = 0
            while j < m:
                if nums[j] < nums[i]:
                    counter += 1
                j += 1
            res.append(counter)
            i += 1
        return res
        # my second try. not efficient, 超时 堆 heap
        heap = []
        n = len(nums)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            counter = 0
            temp = []
            while heap and heap[0] < nums[i]:
                popped = heappop(heap)
                counter += 1
                temp.append(popped)
            heappush(heap, nums[i])
            res[i] = counter
            while temp:
                heappush(heap, temp.pop())
        return res


class SegmentTreeNode:
    def __init__(self, count, smallest, largest, left=None, right=None):
        self.count = count
        self.largest = largest
        self.smallest = smallest
        self.left = left
        self.right = right


class SegmentTree:
    def _build_tree(self, start, end):
        # initialize tree with 0 value
        if start == end:
            return SegmentTreeNode(0, start, end)
        mid = (start + end) // 2
        left_tree = self._build_tree(start, mid)
        right_tree = self._build_tree(mid + 1, end)
        return SegmentTreeNode(0, start, end, left_tree, right_tree)

    def insert(self, root, val):
        if root.smallest == root.largest == val:
            root.count += 1
            return
        mid = (root.smallest + root.largest) // 2
        if val <= mid:
            self.insert(root.left, val)
        else:
            self.insert(root.right, val)
        root.count = root.left.count + root.right.count

    def count_range(self, root, start, end):
        if start > end:
            return 0
        if root.smallest == start and root.largest == end:
            return root.count
        mid = (root.smallest + root.largest) // 2
        if end <= mid:
            return self.count_range(root.left, start, end)
        elif start > mid:
            return self.count_range(root.right, start, end)
        else:
            return self.count_range(root.left, start, mid) + self.count_range(root.right, mid + 1, end)

    def __init__(self, nums):
        # 此树用最大数和最小数作为tree 的range ，不是用nums的index
        self.root = self._build_tree(min(nums), max(nums))


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """ 线段树, segment tree  https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/c-xian-duan-shu-jie-fa-by-dufre/
        复杂度：master theorem: 总时间复杂度 n*log(end - start) + (end - start) ~= n*log(end - start)
        build_tree: time:  最后一层工作量 O(n^logba)-> O(n) space: stack, log(n)
        insert: time: 每层工作量一样 O(n^d*logn) ->O(logn). space: stack log(n)
        count_range: time: 每层工作量一样 O(n^d*logn) ->O(logn). space: stack log(n)
        """
        n = len(nums)
        res = [0] * n
        st = SegmentTree(nums)
        # print(st.root.largest, st.root.smallest, st.root.count)
        root = st.root
        smallest = st.root.smallest
        for i in range(n - 1, -1, -1):
            # 插入segment tree 中已有数字 （num[i] .. num[n - 1]）中符合 小于 num[i] 的count
            res[i] = st.count_range(root, smallest, nums[i] - 1)
            st.insert(st.root, nums[i])
            # print(st.root.count)
        return res
