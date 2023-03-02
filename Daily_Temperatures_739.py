class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ monotonic stack/单调栈 我的解 """
        stack = []
        # mapping between current index and index of next larger element
        curr_to_next_larger_i_map = {}
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                popped_i = stack.pop()
                curr_to_next_larger_i_map[popped_i] = i
            stack.append(i)
        res = []
        n = len(temperatures)
        for i in range(n):
            next_larger_i = curr_to_next_larger_i_map.get(i, i)
            res.append(next_larger_i - i)
        return res
