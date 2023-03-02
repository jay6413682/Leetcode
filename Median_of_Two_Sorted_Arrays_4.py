class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ 二分查找 binary search 我的最新解，不区分nums1 nums2长短的做法，如果区分长短，cut 一定不会在长nums 的 0 index 左边，或last index 右边，比较简单
        """
        n1 = len(nums1)
        n2 = len(nums2)
        # cut 在哪个nums1 index前面: left1 -> right1是cut 可能的范围
        left1 = 0
        right1 = n1
        half_size = (n1 + n2) // 2
        while left1 < right1:
            mid1 = (left1 + right1 + 1) // 2
            # cut 左侧 个数 最多 比右侧少 1
            # mid1 + mid2 = (n1 + n2) // 2
            mid2 = half_size - mid1
            # cut 在 nums1 index 0 左側 ，意味着left1 要往右移动
            # cut 在 nums2 n2 右侧，意味着right2 要向左移动，也就是left1 就要向右
            # if mid1 < 1 or mid2 > n2:
            #    left1 = mid1
            # cut 在 nums2 index  0 左侧，意味着left2 要往右移动，等价于right1 要往左移动
            # cut 在 nums1 n1 右侧，意味着right1 要向左移动(这个好像不可能，加入left1为 n1,right1 is n1, mid1 == n1)
            # if mid2 < 0 or mid1 > n1： 
            #   right1 = mid1 - 1
            # cut左侧的所有值 要小于等于 右侧所有值
            # nums1[mid1 - 1] <= nums2[mid2] && nums2[mid2 - 1] <= nums1[mid1]
            # 他们的反面 nums1[mid1 - 1] > nums2[mid2] || nums2[mid2 - 1] > nums1[mid1]就是不符合条件的cut
            if mid2 < 0 or (mid1 >= 1 and mid2 < n2 and nums1[mid1 - 1] > nums2[mid2]):  # or mid1 > n1 
                right1 = mid1 - 1
            # elif 和 else 可以合併，因為都是關於移動left 邊界的
            # elif nums2[mid2 - 1] > nums1[mid1]:
            #    left1 = mid1 + 1
            else:
                left1 = mid1
        #print(left1, half_size - left1)
        if left1 < 1:
            # cut 在 nums1 0 index 左侧，pre1 肯定不成立
            pre1 = float(-inf)
        else:
            pre1 = nums1[left1 - 1]
        if half_size - left1 - 1 < 0:
            # cut 在 nums2 0 index 左侧，pre2 肯定不成立
            pre2 = float(-inf)
        else:
            pre2 = nums2[half_size - left1 - 1]
        if left1 >= n1:
            # cut 在 nums1 last index右侧， after1 肯定不成立
            after1 = float(inf)
        else:
            after1 = nums1[left1]
        if half_size - left1 < 0:
            # cut 在 nums2 0 index左侧， after2 肯定不成立
            after2 = float(-inf)
        elif half_size - left1 >= n2:
            # cut 在 nums2 last index右侧， after2 肯定不成立
            after2 = float(inf)
        else:
            after2 = nums2[half_size - left1]
        pre = max(pre1, pre2)
        after = min(after1, after2)
        #print(pre, after)
        if (n1 + n2) % 2 != 0:
            return after
        else:
            return (pre + after) / 2


class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ binary search: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/ 视频
        這個解法不好記。。。還是看双指针或者我的不区分大小数组的解吧。。。
        
        18:50 左右讲解有错误，正确描述是：幻灯片里，下面的两种情况不会出现，只可能出现上面的两种情况。
        TrustTheProcess 在https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/he-bing-yi-hou-zhao-gui-bing-guo-cheng-zhong-zhao-/ (好像已经删除了) 中的疑問：
        你好，请问 使得 nums1[i - 1] <= nums2[j] && nums2[j - 1] <= nums1[i] 这个条件为什么只取其中一个的反面进行判断呢。

        在参考代码1中

        if (nums1[i - 1] > nums2[j]) {
            // 下一轮搜索的区间 [left, i - 1]
            right = i - 1;
            } else {
            // 下一轮搜索的区间 [i, right]
            left = i;
            }
        如果第一个if不满足，那么else不就只满足nums1[i - 1] <= nums2[j]这个条件，&&后面的nums2[j - 1] <= nums1[i]这个条件并没有进行判断啊。

        此处还不理解，希望您能解惑
        作者給出解答：
        @lordcode 您好，这是写二分查找设计判别函数的一个小技巧。题目要我们找的元素满足的性质是：nums1[i - 1] <= nums2[j] && nums2[j - 1] <= nums1[i] ，它的形式是「条件 1 && 条件 2」。

        从不满足的性质去设计判别函数得到的条件会相对简单一点，这是因为 「条件 1 && 条件 2」的反面是 「条件 1取反」或者「条件 2 取反」。即：对其中一个条件取反，设计判别函数就可以逐步逼近，找到目标元素了。

        您所说的对后面那个条件取反，nums2[j - 1] <= nums1[i] 其实是另一版代码，我在视频题解里有讲到，两种写法是「或者」的关系，是没有必要放在一个方法里讨论的哦。

        不知道我说清楚没有，欢迎讨论。
        Cheng: 为什么循环出来之后能一定保证i,j满足nums2[j - 1] <= nums1[i]呢？
        答：首先需要想清楚的一个问题是，「中位数的分割线」一定存在，理由也很简单，因为非空数组的中位数一定存在。

        其实退出循环以后，是一定满足 nums1[i - 1] <= nums2[j] && nums2[j - 1] <= nums1[i]。

        编写代码的逻辑是逐渐排除掉错误的答案，因此编写 if 和 else 的时候对其中一个条件取反就可以了。这种两边向中间夹的过程，可以保证退出循环以后，能找到正确的分割线的位置。

        微波炉：这个算法只有在nums1的长度小于等于nums2的长度时才能正确运行，不然在某些用例下（如[1, 3]，[2])while循环中会发生数组索引越界的异常。所以第一步的nums1, nums2 = nums2, nums1不单单是为了缩减搜索范围，更是确保while循环不会发生数组越界访问。如果不想进行第一步的数组交换话，则要在while循环中加上一些必要的逻辑代码来防止发生数组索引越界，这样无论nums1是不是较短的数组，该算法都能正确运行。
        因为区分长短，假设cut 左边 最多比cut 右边 多 1个数，cut 一定不会在长nums 的 0 index 左边，或last index 右边，比较简单
        
        时间复杂度：O(\log(m+n))O(log(m+n))，其中 mm 和 nn 分别是数组 \textit{nums}_1nums1 和 \textit{nums}_2nums 2的长度。初始时有 k=(m+n)/2k=(m+n)/2 或 k=(m+n)/2+1k=(m+n)/2+1，每一轮循环可以将查找范围减少一半，因此时间复杂度是 O(\log(m+n))O(log(m+n))。

        空间复杂度：O(1)O(1)。

        """
        shorter_nums = nums1 if len(nums1) < len(nums2) else nums2
        longer_nums = nums1 if nums2 == shorter_nums else nums2
        m = len(shorter_nums)
        n = len(longer_nums)
        left = 0
        right = m
        left_size = (m + n + 1) // 2
        while left < right:
            i = (left + right + 1) // 2
            j = left_size - i
            if shorter_nums[i - 1] > longer_nums[j]:
                right = i - 1
            #elif longer_nums[j - 1] > shorter_nums[i]:
            #    left = i + 1
            else:
                left = i
        i = left
        j = left_size - i
        # print(i, j)
        shorter_nums_pre = shorter_nums[i - 1] if i >= 1 else -10 ** 6 - 1
        shorter_nums_after = shorter_nums[i] if i < m else 10 ** 6 + 1
        longer_nums_pre = longer_nums[j - 1] if j >= 1 else -10 ** 6 - 1
        longer_nums_after = longer_nums[j] if j < n else 10 ** 6 + 1
        return (max(shorter_nums_pre, longer_nums_pre) + min(shorter_nums_after, longer_nums_after)) / 2 if (m + n) % 2 == 0 else max(shorter_nums_pre, longer_nums_pre)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ 双指针，归并排序 merge sort;先合并 https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
        checkout solution to number 912
        时间复杂度：遍历全部数组 (m+n)(m+n)

        空间复杂度：开辟了一个数组，保存合并后的两个数组 O(m+n)O(m+n)
        """
        # merge
        m = 0
        n = 0
        nums = []
        len_1 = len(nums1)
        len_2 = len(nums2)
        while m < len_1 and n < len_2:
            if nums1[m] < nums2[n]:
                nums.append(nums1[m])
                m += 1
            else:
                nums.append(nums2[n])
                n += 1
        if m == len_1:
            nums.extend(nums2[n:])
        else:
            nums.extend(nums1[m:])
        print(nums)
        len_nums = len(nums)
        return nums[(len_nums - 1) // 2] if len_nums % 2 != 0 else (nums[(len_nums - 1) // 2] + nums[len_nums // 2]) / 2



class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ 双指针法 https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
        时间复杂度：遍历 len/2+1 次，len=m+n，所以时间复杂度依旧是 O(m+n)O(m+n)。

        空间复杂度：我们申请了常数个变量，也就是 m，n，len，left，right，aStart，bStart 以及 i。

        总共 8 个变量，所以空间复杂度是 O(1）O(1）。

        """
        # latest try
        nums1_pointer = 0
        nums2_pointer = 0
        n1 = len(nums1)
        n2 = len(nums2)
        counter = 0
        pre = after = None
        while counter <= (n1 + n2) // 2:
            pre = after
            if (nums1_pointer < n1 and nums2_pointer < n2 and nums1[nums1_pointer] < nums2[nums2_pointer]) or nums2_pointer >= n2:
                
                after = nums1[nums1_pointer]
                nums1_pointer += 1
            else:
                after = nums2[nums2_pointer]
                nums2_pointer += 1
            counter += 1
        if (n1 + n2) %2 == 0:
            return (pre +  after) / 2
        else:
            return after
    
        m = len(nums1)
        n = len(nums2)
        i = 0
        nums1_pointer = 0
        nums2_pointer = 0
        pre = after = -1
        while i <= (m + n) // 2:
            pre = after
            if nums1_pointer < m and (nums2_pointer >= n or nums1[nums1_pointer] < nums2[nums2_pointer]):
                after = nums1[nums1_pointer]
                nums1_pointer += 1
            else:
                after = nums2[nums2_pointer]
                nums2_pointer += 1
            # print(pre, after)
            i += 1
        return (pre + after) / 2 if (m + n) % 2 == 0 else after

