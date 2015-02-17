class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """ Flood Fill 算法/dfs
        解法1 https://leetcode-cn.com/problems/flood-fill/solution/flood-fill-suan-fa-mo-xing-xiang-jie-dfsbfsbing-ch/
        注意 上面解在边界判断时 应判断小于0的情况
        如果初始颜色就是newColor，那么当递归回到原点image[r][c] == start_color， 再次进入dfs，死循环
        如果初始颜色不是newColor，那么当递归回到原点image[r][c] ！= start_color，return
        但是 为什么初始color == newColor 就可以直接返回呢：若周围color == newColor，不用变，若周围color ！= newcolor，无法floodfill
        解法二：根据 乐观的ck_Go https://leetcode-cn.com/problems/flood-fill/solution/python3-dfs-yu-bfs-liang-chong-fang-fa-san-chong-s/  的问题，使用visited
        但实际上没啥用：
        jimmy00745
        2019-08-09
        @乐观的ck_Go 是这样的，因为标记是否已经访问过要占据额外的空间，通常使用的方法是一个哈希集。而在这道题里面，我们可以根据“点的颜色 == 染的目标色”来判断这个点是否访问过。因此，哈希集的设置会有些多余了，更好的解决方式就是把特殊情况放到开头处理掉。
        """
        # 解法一：
        length = len(image[0])
        width = len(image)
        start_color = image[sr][sc]
        if start_color == newColor:
            return image
        def dfs(r, c):
            if r < 0 or r >= width or c < 0 or c >= length:
                return
            if image[r][c] != start_color:
                return                
            image[r][c] = newColor
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                dfs(new_r, new_c)
        dfs(sr, sc)
        return image
        '''
        # 解法二
        length = len(image[0])
        width = len(image)
        visited = [[False] * length for _ in range(width)]
        start_color = image[sr][sc]
        def dfs(r, c):
            if r < 0 or r >= width or c < 0 or c >= length:
                return
            if image[r][c] != start_color:
                return
            if visited[r][c]:
                return            
            image[r][c] = newColor
            visited[r][c] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                dfs(new_r, new_c)
        dfs(sr, sc)
        return image
        '''


class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """ Flood Fill 算法/bfs
        https://leetcode-cn.com/problems/flood-fill/solution/flood-fill-suan-fa-mo-xing-xiang-jie-dfsbfsbing-ch/
        注意 上面解在边界判断时 应判断小于0的情况
        如果初始颜色就是newColor，那么当递归回到原点image[r][c] == start_color， 再次进入dfs，死循环
        如果初始颜色不是newColor，那么当递归回到原点image[r][c] ！= start_color，return
        但是 为什么初始color == newColor 就可以直接返回呢：若周围color == newColor，不用变，若周围color ！= newcolor，无法floodfill
        注意
            这里特别要提醒的是，一定要在添加到队尾的同时修改颜色值，不要在出队列时再修改颜色值。

            也就是说修改颜色的代码，要放在标注2处，不能放在标注1处

        解释
            如果等到出队列时再修改颜色值，那对于已经添加到队列中的像素点，虽然他们已经在队列中，但颜色并未及时修改。如果此时出队列的像素点正好位于某个已经在队列中的像素点旁边，那这个已经在队列中的像素点，就会被重复添加到队尾了。

            轻则导致耗时增加，严重的话会出现提交超时错误。

        """
        length = len(image[0])
        width = len(image)
        start_color = image[sr][sc]
        if start_color == newColor:
            return image
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = newColor
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            (r, c) = queue.popleft()
            # 标注1
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                if new_r >= 0 and new_r < width and new_c >= 0 and new_c < length and image[new_r][new_c] == start_color:
                    queue.append((new_r, new_c))
                    # 标注2
                    image[new_r][new_c] = newColor
        return image


"""
也可以用并查集unionfind 但是代码比较长： https://leetcode-cn.com/problems/flood-fill/solution/flood-fill-suan-fa-mo-xing-xiang-jie-dfsbfsbing-ch/
"""