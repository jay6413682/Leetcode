class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """ greedy贪心 排序
        https://leetcode.cn/problems/queue-reconstruction-by-height/solution/xian-pai-xu-zai-cha-dui-dong-hua-yan-shi-suan-fa-g/
        渔（套路）：一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。

        在本题目中，我首先对数对进行排序，按照数对的元素 1 降序排序，按照数对的元素 2 升序排序。原因是，按照元素 1 进行降序排序，对于每个元素，在其之前的元素的个数，就是大于等于他的元素的数量，而按照第二个元素正向排序，我们希望 k 大的尽量在后面，减少插入操作的次数。
        为什么高个子在前：核心思想：高个子先站好位，矮个子插入到K位置上，前面肯定有K个高个子，矮个子再插到前面也满足K的要求
            矮个子插队，高个子看不见；所以我们可以先安排高个子的位置，再通过插队的方式安排矮个子的位置
        为什么k 小的 在前：
        “按照第二个元素正向排序，我们希望 k 大的尽量在后面，减少插入操作的次数。”不止是为了减少插入次数，也是为了保证正确性。 举个例子，在身高一样，k不一样的时候，譬如[5,2]和[5,3], 对于最后排完的数组，[5,2]必然在[5,3]的前面。所以如果遍历的时候[5,3]在前面，等它先插入完，这个时候它前面会有3个大于等于它的数组对，遍历到[5,2]的时候，它必然又会插入[5,3]前面（因为它会插入链表索引为2的地方），这个时候[5,3]前面就会有4个大于等于它的数组对了，这样就会出错。
        """
        # 对下面做法的优化
        # 先 按 h 从 大到小排序, 如果 h 一样 k 小的排前面
        people.sort(key=lambda x: [-x[0], x[1]])
        res = []
        for p in people:
            # # people已经排序过了：同一高度时k值小的排前面。
            res.insert(p[1], p)
        return res

        res = []
        # 先 按 h 从 大到小排序
        reversed_sorted_people = list(reversed(sorted(people)))
        # 如果 h 一样 k 小的排前面
        start_sort = None
        stop_sort = None
        # print(reversed_sorted_people)
        for i in range(1, len(reversed_sorted_people)):
            if reversed_sorted_people[i][0] == reversed_sorted_people[i - 1][0]:
                if start_sort is None:
                    start_sort = i - 1
                if i == len(reversed_sorted_people) - 1:
                    stop_sort = i
            else:
                if stop_sort is None and start_sort is not None:
                    stop_sort = i - 1
            if start_sort is not None and stop_sort is not None:
                # print(start_sort, stop_sort)
                for m in range(start_sort + 1, stop_sort + 1):
                    for n in range(m, start_sort, -1):
                        if reversed_sorted_people[n][1] < reversed_sorted_people[n - 1][1]:
                            reversed_sorted_people[n], reversed_sorted_people[n - 1] = reversed_sorted_people[n - 1], reversed_sorted_people[n]
                start_sort = None
                stop_sort = None
                # print(reversed_sorted_people)
        # print(reversed_sorted_people)
        for h, k in reversed_sorted_people:
            if k == 0:
                # k 是 0， 因为 res 中都是比他 h 大的，所以 一定 把 h k 插到最前面
                res.insert(0, [h, k])
            else:
                tmp_k = k
                # k > 0, 前面一定有数，把 h k 插到 前面 个数 正好为 k 的位置
                for i, (exist_h, exist_k) in enumerate(res):
                    if exist_h >= h:
                        tmp_k -= 1
                        if tmp_k == 0:
                            res.insert(i + 1, [h, k])
                            break
                # 否则 append 在尾部
                else:
                    res.append([h, k])
        return res


