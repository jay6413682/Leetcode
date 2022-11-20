class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ binary search: https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
        Find K Closest Elements 问题转化为 寻找最优区间的左边界
        总的来说是定一个R=总数组长度-K个最接近的元素 然后判断时候 根据 MID 和MID+K 之间的差值形成一个里面有K+1个元素的区间.然后对比左到右哪个元素更接近目标值.距离目标值远(即绝对值大)的就缩那一边的边界.
        关于为什么l = mid +1 ，r = mid： 区间是k + 1 个数，要去掉一个数，如果 x 离 m 近，去掉区间最右，m仍然可能是答案，所以r = m；如果x 离m + k 近，去掉区间最左（m），所以l = m + 1
        时间复杂度：O(\log N + K)O(logN+K)，这里 NN 是数组的长度，使用二分法的时间复杂度是对数级别的。感谢 @a-wen-u 朋友的指正。
        空间复杂度：O(1)O(1)，只使用了常数个额外的辅助空间。

        """
        left = 0
        n = len(arr)
        right = n - k
        while left < right:
            mid = (left + right) // 2
            # cannot be abs(x - arr[mid]) <= abs(arr[mid + k] - x)
            # 比如 [1,1,2,2,2,2,2,3,3]
            # 3
            # 3
            # 造成arr[mid] 离 x 比较近的 错觉
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left + k]


class Solution3:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ 双指针，删除法 https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
        复杂度分析：

        时间复杂度：O(N)O(N)，这里 NN 是数组的长度。
        空间复杂度：O(1)O(1)，只使用了常数个额外的辅助空间。
        """
        '''
        left_pointer = 0
        n = len(arr)
        right_pointer = -1
        total_to_pop = n - k
        pop_counter = 0
        while pop_counter != total_to_pop:
            # print('left: {}, right: {}'.format(left_pointer, right_pointer))
            if abs(arr[left_pointer] - x) <= abs(arr[right_pointer] - x):
                arr.pop(-1)
            else:
                arr.pop(0)
            pop_counter += 1
        return arr
        '''
        # don't use pop, because it will change the arr passed in
        left_pointer = 0
        n = len(arr)
        right_pointer = n - 1
        total_to_pop = n - k
        pop_counter = 0
        while pop_counter != total_to_pop:
            # print('left: {}, right: {}'.format(left_pointer, right_pointer))
            if abs(arr[left_pointer] - x) <= abs(arr[right_pointer] - x):
                right_pointer -= 1
            else:
                left_pointer += 1
            pop_counter += 1
        return arr[left_pointer: right_pointer + 1]


class Solution4:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ 双指针 加 binary search
        ForFut comment, samantha's reply: https://leetcode-cn.com/problems/find-k-closest-elements/solution/zhao-dao-kge-zui-jie-jin-de-yuan-su-by-leetcode/
        """
        # binary search for x
        n = len(arr)
        if x < arr[0]:
            return arr[:k]
        if x > arr[n-1]:
            return arr[n - k:n]
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if x > arr[mid]:
                left = mid + 1
            else:
                right = mid
        i = left
        if i > 0 and x - arr[i - 1] <= arr[i] - x:
            i -= 1
        counter = k
        # print(i)
        # double pointers, look left and right from i
        l = i - 1
        r = i + 1
        while r - l - 1 < k:
            if l < 0:
                r += 1
                continue
            if r >= n:
                l -= 1
                continue
            if x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1
            # print(l, r)
        return arr[l + 1:r]


class Solution:
    """ my own solution, binary search 超出时间限制 """
    def binary_search(self, arr, x):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            m = arr[mid]
            if m == x:
                return mid
            elif m < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        counter = 0
        while k > 0:
            x += counter * ((-1) ** counter)
            if x < arr[0] or x > arr[-1]:
                counter += 1
                continue
            # print('x: {}'.format(x))
            found = self.binary_search(arr, x)
            # print(found)
            if found != -1:
                val = arr[found]
                if not res:
                    res.append(val)
                else:
                    for i, v in enumerate(res):
                        if val < v:
                            res.insert(i, val)
                            break
                    else:
                        res.append(val)
                k -= 1
            counter += 1
        return res


class Solution2:
    """ my own solution, low efficientcy, 超出时间限制 """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = []
        for val in arr:
            diff = abs(val - x)                
            if not diffs:
                diffs.append((diff, val))
            else:
                for i, r in enumerate(diffs):
                    if diff < r[0]:
                        diffs.insert(i, (diff, val))
                        break
                else:
                    diffs.append((diff, val))
        # print('diffs: {}'.format(diffs))
        k_diffs = diffs[:k]
        res = []
        for (d, v) in k_diffs:
            if not res:
                res.append(v)
            else:
                for i, r in enumerate(res):
                    if v < r:
                        res.insert(i, v)
                        break
                else:
                    res.append(v)
        return res

