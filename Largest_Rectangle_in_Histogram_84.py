class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # mono stack 单调栈
        # 类似：https://blog.csdn.net/Hanx09/article/details/108434955
        heights = [0] + heights + [0]
        max_area = 0
        stack = []
        # 当前位置 -> 左边界 （第一个严格比当前位置高度小的位置）
        left_map = {}
        # 前面位置 -> 右边界 （第一个不比前面位置高度大（小于等于）的位置）的mapping
        right_map = {}
        length = len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                # 例子：[5,5,1,7,1,1,5,2,7,6]
                # 如果现在高度 小于 或等于 前一个高度，确定前一个 对应右边界 为当前，同时将前一个弹出
                # 如果 当前高度 等于 前一个 高度， 前一个的右边界为扫描到 当前位置时的 右边界，并不是它真正的右边界，但这无所谓，因为 继续向前扫描时，最终会扫到 最后一个高度相等的位置的右侧位置，如果这个位置比前一个位置高度小，则确认了前一个位置的右边界为当前位置，如果这个位置比前一个位置高度大，则继续扫描，直到扫到一个位置比前面最后一个高度相等的位置高度小，这时候不断弹出stack，直到把最后一个高度相等的位置的右边界设成当前位置
                # 也可以 heights[stack[-1]] > heights[i]，比如 https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/dong-hua-yan-shi-dan-diao-zhan-84zhu-zhu-03w3/ 差别是第一个 与后面高度相等的位置的左边界准确，但后面高度相等的左边界不准确
                right_map[stack[-1]] = i
                stack.pop()
            if stack:
                left = stack[-1] + 1
            else:
                left = i
            left_map[i] = left
            stack.append(i)
        # print(left_map, right_map)
        for i in range(1, length - 1):
            left = left_map[i]
            right = right_map[i] if i in right_map else length - 1
            area = (right - left) * heights[i]
            max_area = max_area if max_area > area else area
        return max_area
