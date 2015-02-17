# 稳定性：https://www.cnblogs.com/codingmylife/archive/2012/10/21/2732980.html
# 稳定排序应用场景：https://www.cxyxiaowu.com/2573.html

# 世界上最快的排序算法——Timsort
# http://sunshuyi.vip/2020/03/26/leetcode/tim-sort/?hmsr=leetcode&hmpl=leetcode%2Dsort&hmcu=home&hmkw=home&hmci=none
# Timsort是由Tim Peters在2002年实现的，自Python 2.3以来，它一直是Python的标准排序算法。Java在JDK中使用Timsort对非基本类型进行排序。Android平台和GNU Octave还将其用作默认排序算法。
# Timsort是一种稳定的混合排序算法，同时应用了二分插入排序和归并排序的思想，在时间上击败了其他所有排序算法。它在最坏情况下的时间复杂度为O(nlogn)O(nlogn)优于快速排序；最佳情况的时间复杂度为O(n)O(n)，优于归并排序和堆排序。
# 由于使用了归并排序，使用额外的空间保存数据，TimSort空间复杂度是O(n)O(n)

# 性能对比小结：
# 1. 传统简单排序确实当数据量很小的时候也表现不错，但当数据量增大，其耗时也增大十分明显；
# 2. 冒泡，插入，选择三种排序中，当数据量很大时，选择排序性能会更好；
# 3. 堆排，希尔，归并，快排几种排序算法也表现不错，源于其时间复杂度达到了O(nlogn)O(nlogn)；
# 4. 随机快速排序性能确实表现十分亮眼，甚至有时比基数排序和桶排序还好，这可能也是快排如此流行的原因；
# 5. 线性排序中计数排序表现最好，但他们的限制也比较明显，只能处理范围内的正整数。
# ————————————————
# 版权声明：本文为CSDN博主「Monster丶Xu」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Hairy_Monsters/article/details/80154391


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ Selection sort https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        优点：交换次数最少。
        应用场景：「选择排序」看起来好像最没有用，但是如果在交换成本较高的排序任务中，就可以使用「选择排序」
        复杂度分析：

        时间复杂度：O(N^2)O(N 2)，这里 NN 是数组的长度；
        空间复杂度：O(1)O(1)，使用到常数个临时变量。

        不是一个稳定的排序算法
        """
        # 把最小的交换到前面
        i = 0
        n = len(nums)
        while i < n - 1:
            j = i + 1
            smallest_index = i
            while j < n:
                if nums[j] < nums[smallest_index]:
                    # select smallest
                    smallest_index = j
                j += 1
            # swap
            nums[i], nums[smallest_index] = nums[smallest_index], nums[i]
            # print(nums)
            i += 1
        return nums
        """
        # 把最大的交换到后面
        n = len(nums)
        for i in range(n - 1, -1, -1):
            largest = i
            for j in range(i):
                if nums[j] > nums[largest]:
                    largest = j
            # print(largest, i)
            nums[largest], nums[i] = nums[i], nums[largest]
        return nums
        """


class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ insertion sort
        https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        时间复杂度：O(N^2)O(N 2)，这里 NN 是数组的长度；
        空间复杂度：O(1)O(1)，使用到常数个临时变量。
        由于「插入排序」在「几乎有序」的数组上表现良好，特别地，在「短数组」上的表现也很好。因为「短数组」的特点是：每个元素离它最终排定的位置都不会太远。为此，在小区间内执行排序任务的时候，可以转向使用「插入排序」。
        是稳定的排序算法
        """
        """
        i = 1
        n = len(nums)
        while i < n:
            j = i
            temp = nums[j]
            while j > 0:
                # insert
                if temp < nums[j - 1]:
                    nums[j] = nums[j - 1]
                else:
                    break
                j -= 1
            nums[j] = temp
            # print(nums)
            i += 1
        return nums
        """
        # 把最小的交换到前面
        i = 1
        n = len(nums)
        while i < n:
            j = i
            while j > 0:
                # swap
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                else:
                    break
                j -= 1
            # print(nums)
            i += 1
        return nums
        """
        # 把最大的交换到后面
        n = len(nums)
        for i in range(n - 2, -1, -1):
            for j in range(i,  n - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                else:
                    break
        return nums
        """


class Solution8:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ bubble sort; https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        基本思想：外层循环每一次经过两两比较，把每一轮未排定部分最大的元素放到了数组的末尾；
        「冒泡排序」有个特点：在遍历的过程中，提前检测到数组是有序的，从而结束排序，而不像「选择排序」那样，即使输入数据是有序的，「选择排序」依然需要「傻乎乎」地走完所有的流程。

        因为这个排序的过程很像冒泡泡，找到最大的元素不停的移动到最后端，所以这个排序算法就叫冒泡排序。(https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/)
        冒泡排序的最大特点就是代码简单，短短的五行代码就能完成整个排序的操作。

        时间复杂度比较稳定不管怎样都需要O(n^2)O(n 2)次比较，所以是O(n^2)O(n 2)的时间复杂度。

        空间复杂度是O(1)O(1)，所有操作在原来的数组完成就可以了，不需要额外的空间。
        """
        # 用 sorted flag 优化
        n = len(nums)
        for i in range(n - 1, -1, -1):
            # 先默认数组是有序的，只要发生一次交换，就必须进行下一轮比较，
            # 如果在内层循环中，都没有执行一次交换操作，说明此时数组已经是升序数组
            sorted = True
            for j in range(0, i):
                if nums[j] > nums[j + 1]:
                    # swap
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    sorted = False
            if sorted:
                break
        return nums
        """
        # without optimization
        n = len(nums)
        for i in range(n - 1, -1, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
        """


class Solution3:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ merge sort / 归并排序 https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/
        时间复杂度：O(N \log N)O(NlogN)，这里 NN 是数组的长度；- master theorem / master theory, 主定理, a=2, b=2, d=1
        空间复杂度：O(N)O(N)，辅助数组与输入数组规模相当。
        「归并排序」比「快速排序」好的一点是，它借助了额外空间，可以实现「稳定排序」，Java 里对于「对象数组」的排序任务，就是使用归并排序
        """
        def merge_sort(nums, left, right):
            if left == right:
                return
            # divide and sort
            mid = (left + right) // 2
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)
            # merge the two sorted array
            left_pointer = left
            right_pointer = mid + 1
            # 如果数组的这个子区间本身有序，无需合并
            if nums[mid] <= nums[mid + 1]:
                return
            new_nums = []
            # print(left_pointer, right_pointer, left, right, mid)
            while left_pointer <= mid and right_pointer <= right:
                # 注意写成 < 就丢失了稳定性（相同元素原来靠前的排序以后依然靠前）
                if nums[left_pointer] <= nums[right_pointer]:
                    new_nums.append(nums[left_pointer])
                    left_pointer += 1
                else:
                    new_nums.append(nums[right_pointer])
                    right_pointer += 1
            # print(nums, new_nums, left_pointer, right_pointer)
            if left_pointer > mid:
                new_nums.extend(nums[right_pointer:right + 1])
            elif right_pointer > right:
                new_nums.extend(nums[left_pointer:mid + 1])
            nums[left:right + 1] = new_nums
            # print(nums)
        merge_sort(nums, 0, len(nums) - 1)
        return nums


class Solution4:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ quick sort
        # 倾斜tilt的问题 https://blog.csdn.net/GarfieldGCat/article/details/89735238，这里讲的倾斜不是 563 题https://codeleading.com/article/56771012685/的倾斜。而是指imbalance 即只有一边子树的情况 https://blog.csdn.net/GarfieldGCat/article/details/89507089
        关于quick sort的详解：https://zhuanlan.zhihu.com/p/57436476 
        其中推荐选择三数中值 或者 随机选择 ， 其推荐选择三数中值因为最有可能选择到数据的中值，其算法选择了双指针法
        对于很小的数组（N<=20），插入排序要比快速排序更好。因为快速排序有递归开销，并且插入排序是稳定排序。
        另外https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        列表大小等于或小于该大小（7），将优先于 quickSort 使用插入排序
        版本 1：基本***：把等于切分元素的所有元素分到了数组的同一侧，可能会造成递归树倾斜；不好： https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/ gif 图
        版本 2：双指针***：把等于切分元素的所有元素等概率地分到了数组的两侧，避免了递归树倾斜，递归树相对平衡；可以
        版本 3：三指针***：把等于切分元素的所有元素挤到了数组的中间，在有很多元素和切分元素相等的情况下，递归区间大大减少。当重复元素较多时，这个解应该是最好的
        这里有一个经验的总结：之所以***有这些优化，起因都是来自「递归树」的高度。关于「树」的算法的优化，绝大部分都是在和树的「高度」较劲。类似的通过减少树高度、使得树更平衡的数据结构还有「二叉搜索树」优化成「AVL 树」或者「红黑树」、「并查集」的「按秩合并」与「路径压缩」。

        但是因为版本三比较不好理解，我还是记住第二种双指针法吧 （https://zhuanlan.zhihu.com/p/57436476 ）

        复杂度：https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        时间复杂度：O(N \log N)O(NlogN)，这里 NN 是数组的长度；master theorem 导出 , a=2, b=2, d=1
        空间复杂度：O(\log N)O(logN)，这里占用的空间主要来自递归函数的栈空间。

        """
        def quick_sort(nums, left, right):
            # print(left, right)
            if left >= right:
                return
            # left，mid，right交换排序
            mid = (left + right) // 2
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[mid] < nums[left]:
                nums[mid], nums[left] = nums[left], nums[mid]
            if nums[mid] > nums[right]:
                nums[mid], nums[right] = nums[right], nums[mid]
            # print(nums)
            pivot = mid
            # mid为pivot，pivot与right - 1交换
            nums[pivot], nums[right - 1] = nums[right - 1], nums[pivot]
            pivot = right - 1
            i = left
            j = pivot - 1
            # left (i) 向右扫，pivot - 1 (j) 向左扫，左大右小交换，直到交错
            while i <= j:
                while nums[i] <= nums[pivot] and i <= j:
                    i += 1
                while nums[j] >= nums[pivot] and i <= j:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            # pivot 与 i 交换
            nums[pivot], nums[i] = nums[i], nums[pivot]
            pivot = i
            # print(nums, left, pivot, right)
            # pivot左边右边分别递归排序
            quick_sort(nums, left, pivot - 1)
            quick_sort(nums, pivot + 1, right)
        quick_sort(nums, 0, len(nums) - 1)
        return nums


class Solution5:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ heap sort; iterative solution; https://www.jianshu.com/p/d174f1862601
        similar to solution of https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        or https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/ （sift down 解法index 从零开始所以 chilidpos = pos * 2 + 1）
        时间复杂度稳定在O(nlogn)O(nlogn)，因为在构建堆的时候时间遍历数组对于每个元素需要进行O(logn)O(logn)次比较，时间复杂度是O(nlogn)O(nlogn)。在弹出每个元素重建堆需要O(logn)O(logn)的复杂度，时间复杂度也是O(nlogn)O(nlogn)，所以整体的时间复杂度是O(nlogn)O(nlogn)

        空间复杂度是O(1)O(1)，在原数组进行所有操作就可以了。

        堆排序是不稳定，堆得构建和重建的过程都会打乱元素的相对位置。(https://www.cnblogs.com/codingmylife/archive/2012/10/21/2732980.html)
        堆排序的代码量相对于其他的排序算法来说是比较多的，理解上也比较难，涉及到最大堆和二叉树等相关概念。虽然在实际使用中相对于快速排序不是那么好用，但是最坏情况下的O(nlogn)O(nlogn)的时间复杂度也是优于快排的。空间使用是恒定的，是优于归并排序。
        (https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/)
        """
        def sift_down(nums, start, end):
            x = start + 1
            z = end + 1
            y = x * 2
            while y <= z:
                if y <= end and nums[y - 1] < nums[y]:
                    y += 1
                if nums[x - 1] < nums[y - 1]:
                    # swap root with the larger leaf
                    nums[x - 1], nums[y - 1] = nums[y - 1], nums[x - 1]
                    x = y
                    y *= 2
                else:
                    break
        n = len(nums)
        root_counts = n // 2
        # e.g. roots index are 4, 3, 2, 1
        # line 25 and line 26 are for heapify
        # 将数组整理成堆
        for i in range(root_counts - 1, -1, -1):
            # 只需要从 i = (len - 1) / 2 这个位置开始逐层下移
            sift_down(nums, i, n - 1)
        # print(nums)
        for j in range(0, n - 1):
            # swap top root with the last
            # 把堆顶元素（当前最大）交换到数组末尾
            nums[0], nums[n - j - 1] = nums[n - j - 1], nums[0]
            # print(nums)
            # heapify the rest
            # 下标 0 位置下沉操作，使得区间 [0, i] 堆有序
            sift_down(nums, 0, n - j - 2)
            # print(nums)
        return nums


class Solution6:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ heap sort; recursive solution; https://www.jianshu.com/p/d174f1862601
        similar to solution of https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/
        or https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/ （sift down 解法index 从零开始所以 chilidpos = pos * 2 + 1） (adjust_heap 最后一行应该是adjust_heap(nums, chilidpos, endpos))
        时间复杂度稳定在O(nlogn)O(nlogn)，因为在构建堆的时候时间遍历数组对于每个元素需要进行O(logn)O(logn)次比较，时间复杂度是O(nlogn)O(nlogn)。在弹出每个元素重建堆需要O(logn)O(logn)的复杂度，时间复杂度也是O(nlogn)O(nlogn)，所以整体的时间复杂度是O(nlogn)O(nlogn)
        或可从其recursive solution 通过master theory 求得
        空间复杂度是stack space n*logn ？

        堆排序是不稳定，堆得构建和重建的过程都会打乱元素的相对位置。(https://www.cnblogs.com/codingmylife/archive/2012/10/21/2732980.html)
        堆排序的代码量相对于其他的排序算法来说是比较多的，理解上也比较难，涉及到最大堆和二叉树等相关概念。虽然在实际使用中相对于快速排序不是那么好用，但是最坏情况下的O(nlogn)O(nlogn)的时间复杂度也是优于快排的。空间使用是恒定的，是优于归并排序。
        (https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/)
        """
        def sift_down(nums, start, end):
            x = start + 1
            z = end + 1
            y = x * 2
            # print(nums, x, y, z)
            if x >= z or y > z:
                return
            if y <= end and nums[y - 1] < nums[y]:
                y += 1
            if nums[x - 1] < nums[y - 1]:
                # swap root with the larger leaf
                nums[x - 1], nums[y - 1] = nums[y - 1], nums[x - 1]
                x = y
                sift_down(nums, x - 1, end)

        n = len(nums)
        root_counts = n // 2
        # e.g. roots index are 4, 3, 2, 1
        # line 25 and line 26 are for heapify
        # 将数组整理成堆
        for i in range(root_counts - 1, -1, -1):
            # 只需要从 i = (len - 1) / 2 这个位置开始逐层下移
            sift_down(nums, i, n - 1)
        # print('heapify: {}'.format(nums))
        for j in range(0, n - 1):
            # swap top root with the last
            # 把堆顶元素（当前最大）交换到数组末尾
            nums[0], nums[n - j - 1] = nums[n - j - 1], nums[0]
            # print('before sift down {}'.format(nums))
            # heapify the rest
            # 下标 0 位置下沉操作，使得区间 [0, i] 堆有序
            sift_down(nums, 0, n - j - 2)
        return nums


class Solution7:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ shell sort; 从后往前 https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/
        从前往后的解法比较麻烦，没看：https://www.cnblogs.com/open-yang/p/11367089.html

        非稳定排序，内排序；

        希尔排序的时间复杂度和增量序列是相关的。

        {1,2,4,8,...}这种序列并不是很好的增量序列，使用这个增量序列的时间复杂度（最坏情形）是O(n^2)O(n2)；

        Hibbard提出了另一个增量序列{1,3,7，...,2^k-1}1,3,7，...,2k−1，这种序列的时间复杂度(最坏情形)为O(n^{1.5})O(n 1.5；

        Sedgewick提出了几种增量序列，其最坏情形运行时间为O(n^{1.3})O(n 1.3)，其中最好的一个序列是{1,5,19,41,109,...}；
        https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/:
        Donald Shell于1959年发布了这种排序算法，运行时间在很大程度上取决于它使用的间隔，在实际使用中，其时间复杂度仍然是一个悬而未决的问题，基本在O(n^2)O(n 2)和O(n^{4/3})O(n 4/3)之间。

        空间复杂度是O(1)O(1)，是原地算法。

        这个算法是不稳定的，里面有很多不相邻元素的交换操作。
        """
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i - gap >= 0 and nums[i] < nums[i - gap]:
                    nums[i], nums[i - gap] = nums[i - gap], nums[i]
                    i -= gap
            gap //= 2
        return nums


class Solution9:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ Counting Sort/计数排序; linear: https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/
        动图：https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/

        计数排序能够将时间复杂度降低到O(n+r)O(n+r)（r为数组元素变化范围），不过这是对于数组元素的变化范围不是特别大。随着范围的变大，计数排序的性能就会逐渐降低。

        空间复杂度为O(n+r)O(n+r)，随着数组元素变化范围的增大，空间复杂度也会变大。

        计数排序是稳定的，原来排在前面的相同在计数的时候，仍然是排在每个计数位置的前面，在最后复原的时候也是从每个计数位的前面开始复原，所以最后相对位置还是相同的。
        （https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/）
        关于其稳定性：https://stackoverflow.com/questions/2572195/how-is-counting-sort-a-stable-sort/17111445

        有说他是external sort 但 网上也有说不是。https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/
        https://medium.com/basecs/counting-linearly-with-counting-sort-cd8516ae09b3
        """
        ma = mi = nums[0]
        # find max val and min val
        for n in nums:
            if n > ma:
                ma = n
            if n < mi:
                mi = n
        # create a list, its index map to a nums val. it's size needs to be range of nums plus one
        temp = [0] * (ma - mi + 1)
        for n in nums:
            temp[n - mi] += 1
        j = 0
        # enumerate through the counters and put val back to nums
        for i, m in enumerate(temp):
            while m > 0:
                nums[j] = i + mi
                j += 1
                m -= 1
        return nums


class Solution11:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ 桶排序; bucket sort;桶排序是计数排序的升级版 linear: https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/ 稳定排序，时间复杂度O(n + k)O(n+k)，k为桶的个数。

        复杂度深入分析
        用排序主要适用于均匀分布的数字数组，在这种情况下能够达到最大效率 : 
        https://dailc.github.io/2016/12/03/baseKnowlenge_algorithm_sort_bucketSort.html

        有说他是external sort 但 网上也有说不是。
        """

        def bucket_sort(nums, bucket_size):
            if len(nums) < 2:
                return nums
            # get max val and min val
            ma = mi = nums[0]
            for n in nums:
                if n > ma:
                    ma = n
                if n < mi:
                    mi = n
            res = []
            bucket_counts = (ma - mi) // bucket_size + 1
            buckets = [[] for _ in range(bucket_counts)]
            # put nums in buckets
            for num in nums:
                buckets[(num - mi) // bucket_size].append(num)
            # sort in buckets
            # print("buckets: {}".format(buckets))
            for bucket in buckets:
                if not bucket:
                    continue
                if len(bucket) == 1 or bucket_size == 1:
                    res.extend(bucket)
                else:
                    # every nums in the same bucket, make bucket smaller
                    if bucket_counts == 1:
                        bucket_size -= 1
                    res.extend(bucket_sort(bucket, bucket_size))
            return res
        return bucket_sort(nums, 10)


class Solution10:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ 基数排序; Radix sort; linear: https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/

        稳定排序，时间复杂度 posCount * (n + n)posCount∗(n+n) ，其中 posCount 为数组中最大元素的最高位数；简化下得：O( k *n )；其中k为常数，n为元素个数。
        
        有说他是external sort 但 网上也有说不是。
        """
        # max val and min val
        ma = mi = nums[0]
        for n in nums:
            if n > ma:
                ma = n
            if n < mi:
                mi = n
        # have to deal positive value only
        # 最大位数
        digits_count = len(str(ma - mi))
        # create 10 (0 - 9) buckets
        buckets = [[] for _ in range(10)]
        # 从个位开始
        div = 1
        mod = 10
        while digits_count > 0:
            # 根据该位的数字放进不同的buckets
            for num in nums:
                num = num - mi
                digit = num % mod // div
                buckets[digit].append(num)
            # print(buckets)
            digits_count -= 1
            div *= 10
            mod *= 10
            # put the numbers in the bucket back to nums
            i = 0
            for b in buckets:
                for n in b:
                    nums[i] = n + mi
                    i += 1
            # reset buckets
            buckets = [[] for _ in range(10)]
        return nums


class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution12:

    def build_bst(self, nums):
        def add_node(root, num):
            if not root:
                return Node(num)
            if num < root.val:
                root.left = add_node(root.left, num)
            else:
                root.right = add_node(root.right, num)
            return root
        root = None
        for num in nums:
            root = add_node(root, num)
        return root

    def inorder_traverse(self, root):
        if not root:
            return []
        res = []
        if root.left:
            res.extend(self.inorder_traverse(root.left))
        res.append(root.val)
        if root.right:
            res.extend(self.inorder_traverse(root.right))
        return res

    def inorder_traverse2(self, root, nums, i_list):
        # must use i list to store which index of nums have been updated already, 光传数字不行
        if not root:
            return
        if root.left:
            self.inorder_traverse2(root.left, nums, i_list)
        nums[i_list[0]] = root.val
        i_list[0] += 1
        if root.right:
            self.inorder_traverse2(root.right, nums, i_list)

    def sortArray(self, nums: List[int]) -> List[int]:
        """ BST sort; binary search tree search: https://leetcode-cn.com/problems/sort-an-array/solution/shi-er-chong-pai-xu-suan-fa-bao-ni-man-yi-dai-gift/ 稳定排序，时间复杂度O(n + k)O(n+k)，k为桶的个数。

        时间复杂度上面根据原数组变化比较大，最差情况是整个数组是已经排好序的，这样二叉树会变成一个链表结构，时间复杂度退化到了O(n^2)O(n 2)，但是最优和平均情况下时间复杂度在O(nlogn)O(nlogn)水平。

        空间复杂度是O(n)O(n)，因为要构建一个包含n个元素的二叉搜索树。

        这个算法是稳定，在构建二叉树的过程中能够保证元素顺序的一致性。

        """
        root = self.build_bst(nums)
        return self.inorder_traverse(root)
        # or inplace change, this will save space complexity
        # self.inorder_traverse2(root, nums, [0])
