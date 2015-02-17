class Solution:
    def totalFruit(self, s: List[int]) -> int:
        # my solution, meet template 1 in numbers sheet
        # similar to https://leetcode-cn.com/problems/fruit-into-baskets/solution/zhong-gui-zhong-ju-bo-diao-ma-jia-gai-ti-ben-zhi-j/
        left = 0
        right = 0
        n = len(fruits)
        number_counter_map = defaultdict(int)
        res = 0
        while right < n:
            number_counter_map[fruits[right]] += 1
            # print(number_counter_map)
            while len(number_counter_map) > 2:
                if number_counter_map[fruits[left]] > 1:
                    number_counter_map[fruits[left]] -= 1
                else:
                    del number_counter_map[fruits[left]]
                left += 1
            window_length = right - left + 1
            # print(number_counter_map, window_length, left, right)
            if window_length > res:
                res = window_length
            right += 1
        return res
        
        """
        # 这个解法不好懂，算了
        char_count_mapping = {}
        substr_start = 0
        max_len = 0
        for i, chrt in enumerate(s):
            if chrt not in char_count_mapping:
                char_count_mapping[chrt] = 1
            else:
                char_count_mapping[chrt] += 1
            if len(char_count_mapping) > 2:
                max_len = max_len if max_len > i - substr_start else i - substr_start
                while substr_start < i:
                    char_count_mapping[s[substr_start]] -= 1
                    if char_count_mapping[s[substr_start]] == 0:
                        del char_count_mapping[s[substr_start]]
                        substr_start += 1
                        break
                    substr_start += 1
            else:
                max_len = max_len if i - substr_start + 1 < max_len else i - substr_start + 1
        return max_len
        """
        
        """
        # my solution, not using left pointer but idea is similar
        right = 0
        n = len(fruits)
        window = deque()
        uniques = set()
        res = 0
        while right < n:
            if fruits[right] not in window:
                uniques.add(fruits[right])
            window.append(fruits[right])
            right += 1
            while len(uniques) > 2:
                window.popleft()
                uniques = set(window)
            if len(window) > res:
                res = len(window)
        return res
        """
        """
        # my solution but not meet the template
        left = 0
        right = 0
        n = len(fruits)
        number_counter_map = defaultdict(int)
        res = 1
        number_counter_map[fruits[0]] += 1
        while right < n:
            right += 1
            if right == n:
                break
            number_counter_map[fruits[right]] += 1
            # print(number_counter_map)
            while len(number_counter_map) > 2:
                if number_counter_map[fruits[left]] > 1:
                    number_counter_map[fruits[left]] -= 1
                else:
                    del number_counter_map[fruits[left]]
                left += 1
            window_length = right - left + 1
            # print(number_counter_map, window_length, left, right)
            if window_length > res:
                res = window_length
        return res
                