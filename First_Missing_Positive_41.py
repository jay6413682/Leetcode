class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        原地hash
        https://leetcode.cn/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
        简单的来说，哈希表是一种表结构，我们可以直接根据给定的key值通过hash函数计算出目标位置。
        哈希表可以理解为一维数组。因为只是单一的坐标。当然如果考虑到哈希碰撞，理解为二维数组也无不可。
        这道题里哈希函数的规则特别简单，那就是数值为 i 的数映射到下标为 i - 1 的位置。
        说明：while 循环不会每一次都把数组里面的所有元素都看一遍。如果有一些元素在这一次的循环中被交换到了它们应该在的位置，那么在后续的遍历中，由于它们已经在正确的位置上了，代码再执行到它们的时候，就会被跳过。
        平均下来，每个数只需要看一次就可以了，while 循环体被执行很多次的情况不会每次都发生。这样的复杂度分析的方法叫做均摊复杂度分析。
        """
        n = len(nums)
        i = 0

        while i < n:
            '''
            suan-tou-wang-ba comments:
            只有在 nums[i] 是 [1, len] 之间的数，并且不在自己应该呆的位置， nums[i] != i + 1 ，
            并且 它应该呆的位置没有被同伴占有（即存在重复值占有）    nums[nums[i] - 1] != nums[i] 的时候才进行交换
                
            为什么使用 while ？ 因为交换后，原本 i 位置的 nums[i] 已经交换到了别的地方，
            交换后到这里的新值不一定是适合这个位置的，因此需要重新进行判断交换
            如果使用 if，那么进行一次交换后，i 就会 +1 进入下一个循环，那么交换过来的新值就没有去找到它该有的位置
            比如 nums = [3, 4, -1, 1] 当 3 进行交换后， nums 变成 [-1，4，3，1]，
            此时 i == 0，如果使用 if ，那么会进入下一个循环， 这个 -1 就没有进行处理
            '''
            while 1 <= nums[i] <= n and nums[i] - 1 != i and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # 注意不能是 nums[i], nums[nums[i] - 1]  = nums[nums[i] - 1], nums[i]
                # 因为如果nums[i] 已经被修改了，后面nums[nums[i] - 1] 的 index nums[i] - 1 也变了
            i += 1
        for i, num in enumerate(nums):
            if num - 1 != i:
                return i + 1
        return n + 1
