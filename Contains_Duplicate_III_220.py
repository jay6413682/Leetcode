from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """ yim-6 追风少年的解，解题思路：
        https://leetcode-cn.com/problems/contains-duplicate-iii/solution/python3-er-cha-sou-suo-shu-by-moqimoqidea/
        SortedSet/SortedList 就是优化后的BST （red black tree）
        自己implement BST 的解：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/python3er-cha-sou-suo-shu-cun-zai-zhong-fu-yuan-su/
        方法二：滑动窗口 + 二叉搜索树的解：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/hua-dong-chuang-kou-er-fen-sou-suo-shu-zhao-shang-/
        red black tree: https://www.jianshu.com/p/e136ec79235c ; 任何不平衡都会在三次旋转之内解决。
        avl tree: https://www.jianshu.com/p/65c90aa1236d ; 
        b-tree; b+tree: https://blog.csdn.net/wanderlustLee/article/details/81297253
        complexity: 时间复杂度：TreeSet 基于红黑树，查找和插入都是 O(\log{k})O(logk) 复杂度。整体复杂度为 O(n\log{k})O           (nlogk)
        空间复杂度：O(k)O(k) : https://leetcode-cn.com/problems/contains-duplicate-iii/solution/gong-shui-san-xie-yi-ti-shuang-jie-hua-d-dlnv/ 
        """
        window = SortedSet()
        for i, num in enumerate(nums):
            idx = window.bisect_left(num - t)
            if idx < len(window) and window[idx] <= num + t:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])
        return False
        """
        # 结合 https://leetcode-cn.com/problems/contains-duplicate-iii/solution/python3er-cha-sou-suo-shu-cun-zai-zhong-fu-yuan-su/ 理解
        # 转化为，在window_bst（当前值以前，不包括当前值） 这个binary search tree 中查找是否存在一个元素 使得其值>= 当前值的-t ，<=当前值 + t 
        # 类似https://leetcode-cn.com/problems/contains-duplicate-iii/solution/gong-shui-san-xie-yi-ti-shuang-jie-hua-d-dlnv/ python解
        window_bst = SortedList()
        for i in range(len(nums)):
            if i > k:
                # 如果 window_bst size 大于 k (i > k), 删除第nums[i - k - 1]，即删除最先插入的元素
                window_bst.remove(nums[i - k - 1])
            n = len(window_bst)
            if n > 0: # 若该二叉搜索树中元素个数大于等于2，则查询
                # window_bst[idx] 为大于等于 nums[i] - t 的最小值
                idx = window_bst.bisect_left(nums[i] - t)
                # print(nums[i] - t, idx, n, nums[i] + t)
                # idx 不能超过 window size。
                # 另外根据 https://leetcode-cn.com/problems/contains-duplicate-iii/solution/hua-dong-chuang-kou-er-fen-sou-suo-shu-zhao-shang-/ ， window_bst[idx] <= nums[i] + t
                if idx < n and window_bst[idx] <= nums[i] + t:
                    return True
            # 插入。不能先插入，再查找，否则会难以解决 window_bst[idx] 不能是 插入节点这一条件
            window_bst.add(nums[i])
        return False
        """


class Solution3:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """ 关于分桶尤其是t + 1: https://leetcode-cn.com/problems/contains-duplicate-iii/solution/c-li-yong-tong-fen-zu-xiang-xi-jie-shi-b-ofj6/
        视频详解：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/gua-he-xin-shou-peng-you-de-shi-pin-ti-j-c4ua/
        in python // always gets closer to -infinite
        复杂度：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/cun-zai-zhong-fu-yuan-su-iii-by-leetcode-bbkt/
        时间复杂度：O(n)O(n)，其中 nn 是给定数组的长度。每个元素至多被插入哈希表和从哈希表中删除一次，每次操作的时间复杂度均为 O    (1)O(1)。

        空间复杂度：O(\min(n, k))O(min(n,k))，其中 nn 是给定数组的长度。哈希表中至多包含 \min(n, k + 1)min(n,k+1) 个元素。

        """
        buckets = {}
        bucket_size = t + 1
        for i, num in enumerate(nums):
            if i >= k + 1:
                buckets.pop(nums[i - k - 1] // bucket_size)
            bucket_id = num // bucket_size
            if bucket_id in buckets:
                return True
            buckets[bucket_id] = num
            if (bucket_id - 1) in buckets and abs(buckets[bucket_id - 1] - num) <= t:
                return True
            if (bucket_id + 1) in buckets and abs(buckets[bucket_id + 1] - num) <= t:
                return True
        return False


class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """ 暴力法：超出时间限制
        https://leetcode-cn.com/problems/contains-duplicate-iii/solution/hua-dong-chuang-kou-er-fen-sou-suo-shu-zhao-shang-/
        """
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                    return True
        return False
        '''
        n = len(nums)
        for start in range(n - 1):
            if start + k >= n:
                end = n - 1
            else:
                end = start + k
            sorted_sub_nums = sorted(nums[start:end + 1])
            # print(sorted_sub_nums)
            window_size = len(sorted_sub_nums)
            for i in range(window_size - 1):
                if sorted_sub_nums[i + 1] - sorted_sub_nums[i] <= t:
                    return True
        return False
        '''
