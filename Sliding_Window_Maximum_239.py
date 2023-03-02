import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 暴力法 brutal force, sliding window
        超出时间限制
        这道题最暴力的方法就是 2 层循环，时间复杂度 O(n * K)O(n∗K)。
        空间复杂度：o(n)
        """
        res = []
        i = 0
        n = len(nums)
        while i < n - k + 1:
            max_val = max(nums[i:i + k])
            res.append(max_val)
            i += 1
        return res


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ priority queue, heapq, heap, 堆，滑动窗口sliding window
        类似解 https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/
        时间复杂度：O(n \log n)O(nlogn)，其中 nn 是数组 \textit{nums}nums 的长度。在最坏情况下，数组 \textit{nums}nums 中的元素单调递增，那么最终优先队列中包含了所有元素，没有元素被移除。由于将一个元素放入优先队列的时间复杂度为 O(\log n)O(logn)，因此总时间复杂度为 O(n \log n)O(nlogn)。

        空间复杂度：O(n)O(n)，即为优先队列需要使用的空间。这里所有的空间复杂度分析都不考虑返回的答案需要的 O(n)O(n) 空间，只计算额外的空间使用。（在最坏情况下，数组 \textit{nums}nums 中的元素单调递增，那么最终优先队列中包含了所有元素）
        解释的更清楚：https://leetcode-cn.com/problems/sliding-window-maximum/solution/you-xian-dui-lie-zui-da-dui-dan-diao-dui-dbn9/
        """
        # 注意 Python 默认的优先队列是小根堆
        priority_queue = [(-num, i) for (i, num) in enumerate(nums[:k])]
        heapq.heapify(priority_queue)
        res = [-priority_queue[0][0]]
        for i in range(k, len(nums)):
            num = nums[i]
            heappush(priority_queue, (-num, i))
            while priority_queue[0][1] <= i - k:
                heapq.heappop(priority_queue)
            res.append(-priority_queue[0][0])
        return res
        '''
        # or like below
        priority_queue = [(-num, i) for (i, num) in enumerate(nums[:k])]
        heapq.heapify(priority_queue)
        res = [-priority_queue[0][0]]
        for i in range(k, len(nums)):
            num = nums[i]
            # print(priority_queue)
            while priority_queue and priority_queue[0][1] <= i - k:
                heapq.heappop(priority_queue)
            print(priority_queue)
            heappush(priority_queue, (-num, i))
            res.append(-priority_queue[0][0])
        return res
        '''


class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 单调队列,monotonic queue, 双端队列, deque，double-ended queue, 滑动窗口sliding window
        monotonic/monotone queue vs monotonic/monotone stack: https://blog.csdn.net/Hanx09/article/details/108434955
        https://www.google.com/search?q=monotonic+queue+vs+monotonic+stack&oq=monotonic+stack+vs+monotonic+que&aqs=chrome.1.69i57j0i22i30.12688j1j7&sourceid=chrome&ie=UTF-8
        应用 区间最小（最大）值问题。
        解 https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/ 
        图解： https://leetcode-cn.com/problems/sliding-window-maximum/solution/you-xian-dui-lie-zui-da-dui-dan-diao-dui-dbn9/
        在上述滑动窗口形成及移动的过程中，我们注意到元素是从窗口的右侧进入的，然后由于窗口大小是固定的，因此多余的元素是从窗口左侧移除的。 一端进入，另一端移除，这不就是队列的性质吗？所以，该题目可以借助队列来求解。
        至此，该题目的求解思路就清晰了，具体如下：

        1. 遍历给定数组中的元素，如果队列不为空且当前考察元素大于等于队尾元素，则将队尾元素移除。直到，队列为空或当前考察元素小于新的队尾元素；
        2. 当队首元素的下标小于滑动窗口左侧边界left时，表示队首元素已经不再滑动窗口内，因此将其从队首移除。
        3. 由于数组下标从0开始，因此当窗口右边界right+1大于等于窗口大小k时，意味着窗口形成。此时，队首元素就是该窗口内的最大值。
:
        https://leetcode.cn/problems/sliding-window-maximum/solution/dong-hua-yan-shi-dan-diao-dui-lie-239hua-hc5u/
        时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。每一个下标恰好被放入队列一次，并且最多被弹出队列一次，因此时间复杂度为 O(n)O(n)。
        空间复杂度：O(k)O(k)。与方法一不同的是，在方法二中我们使用的数据结构是双向的，因此「不断从队首弹出元素」保证了队列中最多不会有超过 k+1k+1 个元素，因此队列使用的空间为 O(k)O(k)。

        """
        # index monotonic queue
        monotonic_queue = deque()
        res = []
        n = len(nums)
        '''
        # initialize the queue(头大尾小), it's required because the first k - 1 element shouldn't be in the res
        for i in range(k):
            # pop tails until no smaller val compared to curr
            while monotonic_queue and nums[i] > nums[monotonic_queue[-1]]:
                monotonic_queue.pop()
            monotonic_queue.append(i)
        res.append(nums[monotonic_queue[0]])
        # print(res, monotonic_queue)
        for i in range(k, n):
            # pop tails until no smaller val compared to curr
            while monotonic_queue and nums[i] > nums[monotonic_queue[-1]]:
                monotonic_queue.pop()
            monotonic_queue.append(i)
            # the head (largest val) is out of the queue, pop out the head
            if monotonic_queue[0] <= i - k:
                monotonic_queue.popleft()
            res.append(nums[monotonic_queue[0]])
        '''
        for i in range(n):
            # pop tails until no smaller val compared to curr
            while monotonic_queue and nums[i] > nums[monotonic_queue[-1]]:
                monotonic_queue.pop()
            monotonic_queue.append(i)
            # the head (largest val) is out of the queue, pop out the head
            if monotonic_queue[0] <= i - k:
                monotonic_queue.popleft()
            # only put the head in res when we moved the right pointer to the end of the first full window
            if i >= k - 1:
                res.append(nums[monotonic_queue[0]])
        return res



from collections import deque

class MonoDecQueue(object):
    """ 单调递减队列 implementation 1：https://leetcode.cn/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/ push and pop value
    为什么pop 不用 while loop ： slyfox1201: pop:在元素入队时，是按照下标i入队的，因此队列中剩余的元素，其下标一定是升序的。窗口大小不变，最先被排除出窗口的，一直是下标最小的元素，设为r。元素r在队列中要么是头元素，要么不存在。（栈是单减队列，输入的数组如果前面的数比后面的数小，就会被压出队列；如果前面的数>= 后面的数，后面的数入队列。所以如果window 向右移动，当要检查左边出window 的数是不是在队列中时，它只可能在队头，不可能在队列的其他地方，因为否则已经被压出队列了）
    为什么 self.queue[-1] < val， 而不是<=
    daping3：恰恰相反，能安全地pop_front是因为窗口中的最大值有重复时保留重复，哪里唯一了...
    Alexhanbing：比当前小的元素才继续往下压扁，大于等于的都会继续压，会存在重复元素，所以是单调队列，不是严格单调
    这样做的话，push时如果self.queue[-1] == val，self.queue[-1] 会保留在queue 当中，因为它现在还在window当中，只有当它不在window中时（pop的时候），再把它pop
    避免栈中前面的相同元素被过早弹出，下一次window要move out of 前面的相同元素时，把栈中后面的相同元素弹出
    """
    def __init__(self):
        self.queue = deque()

    def push(self, val):
        while self.queue and self.queue[-1] < val:
            self.queue.pop()
        self.queue.append(val)

    def max(self):
        return self.queue[0]
    
    def pop(self, val):
        if self.queue and self.queue[0] == val:
            self.queue.popleft()

class MonoDecQueue2(object):
    """ 单调递减队列 implementation 2：https://www.jianshu.com/p/e59d51e1eef5 和 https://leetcode.cn/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/ push and pop index
    这个更好理解，pop用了while loop
    为什么 self.queue[-1] < val， 而不是<=
    daping3：恰恰相反，能安全地pop_front是因为窗口中的最大值有重复时保留重复，哪里唯一了...
    Alexhanbing：比当前小的元素才继续往下压扁，大于等于的都会继续压，会存在重复元素，所以是单调队列，不是严格单调
    这样做的话，push时如果self.queue[-1] == val，self.queue[-1] 会保留在queue 当中，因为它现在还在window当中，只有当它不在window中时（pop的时候），再把它pop
    """
    def __init__(self, nums):
        self.nums = nums
        self.queue = deque()

    def push(self, i):
        while self.queue and self.nums[self.queue[-1]] < self.nums[i]:
            self.queue.pop()
        self.queue.append(i)

    def max(self):
        return self.nums[self.queue[0]]

    def pop(self, i):
        # 从队列中弹出所有输入数组中 i 和 它左侧的 数:self.queue[0] == i 的时候 也会被弹出
        # if or while 都可以，<= or == 都可以
        while self.queue and self.queue[0] <= i:
            self.queue.popleft()

class Solution4:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 最好理解，把window实时压入单调递减队列，然后取队列max值（queue[0]]） """
        res = []
        '''
        q = MonoDecQueue()
        for i, num in enumerate(nums):
            if i < k - 1:
                q.push(num)
            else:
                q.push(num)
                res.append(q.max())
                q.pop(nums[i - k + 1])
            #print(q.queue)
        '''
        q = MonoDecQueue2(nums)
        # print(q.queue)
        for i, num in enumerate(nums):
            if i < k - 1:
                q.push(i)
            else:
                q.push(i)
                res.append(q.max())
                q.pop(i - k + 1)
            #print(q.queue)
        return res


class Solution5:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # my solution, 单调队列： https://blog.csdn.net/Hanx09/article/details/108434955
        # 非严格单调递减
        mono_queue = deque()
        res = []
        for i, num in enumerate(nums):
            #'''
            # solution 1
            if i <= k - 1:
                # push
                while mono_queue and mono_queue[-1] < num:
                    mono_queue.pop()
                mono_queue.append(num)
                # add to window max if i == k - 1
                if i == k - 1:
                    res.append(mono_queue[0])
            else:
                # pop
                if mono_queue and mono_queue[0] == nums[i - k]:
                    mono_queue.popleft()
                # push
                while mono_queue and mono_queue[-1] < num:
                    mono_queue.pop()
                mono_queue.append(num)
                # add window max 
                res.append(mono_queue[0])
            #'''
            '''
            # solution 2
            if i < k - 1:
                # push when window not full yet
                while mono_queue and mono_queue[-1] < num:
                    mono_queue.pop()
                mono_queue.append(num)
            else:
                # push
                while mono_queue and mono_queue[-1] < num:
                    mono_queue.pop()
                mono_queue.append(num)
                # add window max
                res.append(mono_queue[0])
                # pop first before next push
                if mono_queue and mono_queue[0] == nums[i + 1 - k]:
                    mono_queue.popleft()
            '''
        return res
