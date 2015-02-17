class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ binary search: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/ 视频
        18:50 左右讲解有错误，正确描述是：幻灯片里，下面的两种情况不会出现，只可能出现上面的两种情况。
        TrustTheProcess 在https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/he-bing-yi-hou-zhao-gui-bing-guo-cheng-zhong-zhao-/ 中的疑問：
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

