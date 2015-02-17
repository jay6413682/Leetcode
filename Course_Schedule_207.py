class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ BFS, 有向无环图(DAG), 拓扑排序, topology sort,  邻接表 adjacency, indegree入度
        https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
        时间复杂度 O(N + M)O(N+M)： 遍历一个图需要访问所有节点和所有临边，NN 和 MM 分别为节点数量和临边数量；
        若课程安排图中存在环，一定有节点的入度始终不为 0： 因為解法是從indegree 為0的vertex 擴散搜索，因為環的vertex indegree 必 >= 1,所以其永远不会被压入栈
        也就不会被遍历到，numCourses 也不会为0
        概念：https://blog.csdn.net/weixin_46072771/article/details/106646721
        https://www.jianshu.com/p/2f344d31e169
        图中的顶点有度的概念：
        度(Degree)：所有与它连接点的个数之和
        入度(Indegree)：存在于有向图中，所有接入该点的边数之和
        出度(Outdegree)：存在于有向图中，所有接出该点的边数之和
        另外，邻接表不需要用list of linked list来表示。 list of list 也可，比如https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
        """
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
        # dfs/back tracing: similar to https://leetcode-cn.com/problems/course-schedule/solution/shen-du-you-xian-bian-li-hui-su-mo-ni-by-mkxc/
        adjacent_list = [[] for _ in range(numCourses)]
        flags = [0] * numCourses
        for curr, pre in prerequisites:
            adjacent_list[pre].append(curr)

        def dfs(i, adjacent_list, flags):
            # flag == -1 -> visited by other route
            # flag == 1 -> visited by same route
            # flag == 0 -> not visited
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacent_list[i]:
                no_circle = dfs(j, adjacent_list, flags)
                if not no_circle:
                    return False
            flags[i] = -1
            return True
        for i in range(numCourses):
            if not dfs(i, adjacent_list, flags):
                return False
        return True
        """


