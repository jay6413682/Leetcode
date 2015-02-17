class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """ binary search; java solution: https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/solution/xun-zhao-bi-mu-biao-zi-mu-da-de-zui-xiao-zi-mu-by-/
        时间复杂度：O(\log N)O(logN)。NN 指的是 letters 的长度，我们只查看数组中的 \log nlogn 个元素。
        空间复杂度：O(1)O(1)。只使用了指针。

        """
        n = len(letters)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        if letters[left] <= target:
            return letters[0]
        return letters[left]
        """
        # my own solution
        left = 0
        right = len(letters) - 1
        target = chr(ord(target) + 1)
        if target > letters[right]:
            return letters[0]
        while left < right:
            mid = (left + right) // 2
            if letters[mid] == target:
                return target
            elif letters[mid] < target:
                left = mid + 1
            else:
                right = mid
        return letters[left]
        """


class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """ https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/solution/xun-zhao-bi-mu-biao-zi-mu-da-de-zui-xiao-zi-mu-by-/
        时间复杂度：O(N)O(N)。NN 指的是 letters 的长度，我们扫描数组的每个元素。
        空间复杂度：O(1)O(1)。只使用了指针。
        """
        for l in letters:
            if l > target:
                return l
        return letters[0]
