class Solution:
    def trap(self, height: List[int]) -> int:
        # mono stack 单调栈
        # https://blog.csdn.net/Hanx09/article/details/108434955
        mono_decrease_i_stack = []
        length = len(height)
        water_area = 0
        for i in range(length):
            while mono_decrease_i_stack and height[mono_decrease_i_stack[-1]] < height[i]:
                right = i
                right_height = height[i]
                bottom = mono_decrease_i_stack.pop()
                bottom_height = height[bottom]
                if mono_decrease_i_stack:
                    left = mono_decrease_i_stack[-1]
                    left_height = height[left]
                    # should be right - left - 1 instead of right - bottom, for example [4,2,0,3,2,5]
                    water_area += (min(left_height, right_height) - bottom_height) * (right - left - 1)
            mono_decrease_i_stack.append(i)
        return water_area
