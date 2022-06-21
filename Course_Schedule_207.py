class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ BFS, 有向无环图(DAG), 拓扑排序, topology sort,  邻接表 adjacency, indegree入度
        https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
        时间复杂度 O(N + M)O(N+M)： 遍历一个图需要访问所有节点和所有临边，NN 和 MM 分别为节点数量和临边数量；
        概念：https://blog.csdn.net/weixin_46072771/article/details/106646721
        https://www.jianshu.com/p/2f344d31e169
        图中的顶点有度的概念：
        度(Degree)：所有与它连接点的个数之和
        入度(Indegree)：存在于有向图中，所有接入该点的边数之和
        出度(Outdegree)：存在于有向图中，所有接出该点的边数之和
        另外，邻接表不需要用list of linked list来表示。 list of list 也可，比如https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
        """
        # bfs/Kahn's Algorithm: repeatedly remove nodes without any dependencies (没有indegree入度) from the graph and add them to the topological ordering. （DAG没有有向环，没有入度的节点不能形成有向环，去掉它，剩下的图仍然是与原图类别相同（DAG or not））：
        # https://www.youtube.com/watch?v=cIBFEhD77b4
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        # Get the indegree and adjacency of every course.
        for curr, pre in prerequisites:
            indegrees[curr] += 1
            adjacency[pre].append(curr)
        # stack = []
        queue = deque()
        # # Get all the courses with the indegree of 0.
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                # stack.append(i)
                queue.append(i)
        # BFS
        while queue:
        # while stack:
            # pre = stack.pop()
            pre = queue.popleft()
            numCourses -= 1
            currs = adjacency[pre]
            for curr in currs:
                indegrees[curr] -= 1
                if indegrees[curr] == 0:
                    # stack.append(curr)
                    queue.append(curr)
        return numCourses == 0
        """
        # dfs 优化解，不会重复搜索已经搜过的路径
        # 没有bfs 好理解, 重点理解bfs, 而且bfs 方法不仅能 求是否有directed cycle 还能求 topology sort
        # related to the dfs way to topologic sort (no circle detection): dfs：Pick an unvisited node。Beginning with the selected node, do a Depth First Search (DFS) exploring only unvisited nodes. On the recursive callback of the DFS, add the current node to the topological ordering in reverse order.
        # www.youtube.com/watch?v=eL-KzMXSXXI&t=34s
        # dfs/back tracing: similar to https://leetcode-cn.com/problems/course-schedule/solution/shen-du-you-xian-bian-li-hui-su-mo-ni-by-mkxc/
        adjacent_list = [[] for _ in range(numCourses)]
        flags = [0] * numCourses
        for curr, pre in prerequisites:
            adjacent_list[pre].append(curr)

        def dfs(i, adjacent_list, flags):
            # dfs ：从i节点起步 是否不存在环，若存在环直接返回 False 否则return true
            # flag == -1 -> visited by other route 已被其他节点启动的 DFS搜索 访问
            # flag == 1 -> visited by same route 已被本轮 DFS 搜索 访问
            # flag == 0 -> not visited
            if flags[i] == -1: # 说明当前访问节点已被其他节点启动的 DFS 访问，无需再重复搜索，直接返回 True。
                return True
            if flags[i] == 1: # 说明在本轮 DFS 搜索中节点 i 被第 2 次访问，即 课程安排图有环 ，直接返回 False。
                return False
            flags[i] = 1
            for j in adjacent_list[i]:
                no_circle = dfs(j, adjacent_list, flags)
                if not no_circle:
                    return False
            flags[i] = -1
            return True
        for i in range(numCourses):
            # 从每个节点起步 是否存在环
            # flags[i] == 0 not necessary as if it is not 0 dfs will return right away
            if flags[i] == 0 and not dfs(i, adjacent_list, flags):
                return False
        return True
        """
        '''
        # dfs 未优化解 https://leetcode.cn/problems/course-schedule/solution/dfs-jian-tu-dfs207-ke-cheng-biao-by-fe-lucifer/
        visited = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        def dfs(i):
            # dfs：从i 开始的 搜索 是否没有环
            # 已被本轮 DFS 搜索 访问过，有环
            if visited[i] == 1:
                return False
            # 从i搜索开始，
            visited[i] = 1
            for j in adjacency[i]:
                if not dfs(j):
                    return False
            # 从i 开始的搜索结束，重制i为未搜索过
            visited[i] = 0
            return True
        for cur, pre in prerequisites:
            adjacency[cur].append(pre)
        for i in range(numCourses):
            # 重复搜索， 哪怕i已经搜过 ，还会再搜一次，O（2n）时间复杂度
            if not dfs(i):
                return False
        return True
        '''


