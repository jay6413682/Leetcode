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


