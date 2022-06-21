class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """ 回溯，backtracking 超时 """
        def dfs(route, fuel_left, s):
            # print(route, fuel_left, s)
            counts = 0
            if fuel_left < 0:
                return 0
            if fuel_left == 0:
                if route[-1] != finish:
                    return 0
                else:
                    return 1
            if fuel_left > 0:
                if route[-1] == finish:
                    counts += 1
            
            for i, l in enumerate(locations):
                if i != s:
                    route.append(i)
                    counts += dfs(route, fuel_left - abs(l - locations[route[-2]]), i)
                    route.pop()
            return counts
        return dfs(deque([start]), fuel, start)


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """ memorization 记忆化搜素，根据我自己的回溯算法（dfs），https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247485297&idx=1&sn=5ee4ce31c42d368af0653f60aa263c82&chksm=fd9cac6ecaeb25787e6da90423c5467e1679da0a8aaf1a3445475199a8f148d8629e851fea57&token=1459317048&lang=zh_CN&scene=21#wechat_redirect 以及 模版写成
        int g[MAXN];
        int f(状态参数) {
            if (g[规模] != 无效数值) return g[规模];
            if (终止条件) return 最小子问题解;
            g[规模] = f(缩小规模);
            return g[规模];
        }
        int main() {
            // ...
            memset(g, 无效数值, sizeof(g));
            // ...
        }
        暗合https://oi-wiki.org/dp/memo/ 方法二
        方法一
        1. 把这道题的 dp 状态和方程写出来
        2. 根据它们写出 dfs 函数
        3. 添加记忆化数组
        方法二
        1. 写出这道题的暴搜程序（最好是 dfs)
        2. 将这个 dfs 改成“无需外部变量”的 dfs
        3. 添加记忆化数组
        """
        # mem[fuel][i] 代表从位置 i 出发，当前剩余的油量为 fuel 的前提下，到达目标位置的「路径数量」。
        # 之所以能采取「缓存中间结果」这样的做法，是因为「在 i 和 fuel 确定的情况下，其到达目的地的路径数量是唯一确定的」。
        n = len(locations)
        m = fuel + 1
        mem = [[-1 for _ in range(n)] for _ in range(m)]
        mod = 10 ** 9 + 7
        def dfs(fuel_left, s):
            '''
            计算「路径数量」
            return 在位置 s 出发，油量为 fuel_left 的前提下，到达 end 的「路径数量」
            '''
            # 油量<0, 说明无法到达任何位置，return 0
            if fuel_left < 0:
                return 0
            #  if (g[规模] != 无效数值) return g[规模];
            if mem[fuel_left][s] != -1:
                return mem[fuel_left][s]

            # base case 1：如果油量为 0，且不在目标位置
            # 将结果 0 写入缓存器并返回
            # 如果油量为零，且在目标位置，将结果 1 写入缓存器并返回
            if fuel_left == 0:
                if s != finish:
                    mem[fuel_left][s] = 0
                    return 0
                else:
                    mem[fuel_left][s] = 1
                    return 1
            # 优化 如果一步到达不了，说明从位置 s 不能到达 finish 位置
            # 将结果 0 写入缓存器并返回
            need = abs(locations[s] - locations[finish]);
            if need > fuel_left:
                mem[fuel_left][s] = 0
                return 0
            count = 0
            # 油量> 0，且已到达finish，那么本身就算一条路径，count = 1
            if fuel_left > 0:
                if s == finish:
                    count = 1
            for i, l in enumerate(locations):
                if i != s:
                    next_fuel_left = fuel_left - abs(l - locations[s])
                    if next_fuel_left > 0 and mem[next_fuel_left][i] != -1:
                        count += mem[next_fuel_left][i]
                    else:
                        count += dfs(next_fuel_left, i)
                    count = count % mod
            mem[fuel_left][s] = count
            # print(mem)
            return mem[fuel_left][s]
        
        return dfs(fuel, start)


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """ 通过 记忆化搜索 得到 dp 解
        我做的时候完全是根据 memorization 的解改一改过来的，实际上可以
        1. 从 DFS 方法签名出发。分析哪些入参是可变的，将其作为 DP 数组的维度；将返回值作为 DP 数组的存储值。
        2. 从 DFS 的主逻辑可以抽象中单个状态的计算方法。
        其中第一点对应了「动态规划」的「状态定义」，第二点对应了「动态规划」的「状态方程转移」。
        """
        # dp[fuel][i] 代表从位置 i 出发，当前剩余的油量为 fuel 的前提下，到达目标位置的「路径数量」。
        # 之所以能采取「缓存中间结果」这样的做法，是因为「在 i 和 fuel 确定的情况下，其到达目的地的路径数量是唯一确定的」
        n = len(locations)
        m = fuel + 1
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        mod = 10 ** 9 + 7
        for fuel_left in range(m):
            for s in range(n):
                if fuel_left == 0:
                    # if fuel left is 0, and we are not at finish, number of routes is 0
                    if s != finish:
                        dp[fuel_left][s] = 0
                    else:
                        # if fuel left is 0, and we are at finish, number of routes is 1
                        dp[fuel_left][s] = 1
                else:
                    # 优化 如果一步到达不了，说明从位置 s 不能到达 finish 位置
                    # 将结果 0 写入缓存器并返回
                    need = abs(locations[s] - locations[finish]);
                    if need > fuel_left:
                        dp[fuel_left][s] = 0
                    else:
                        count = 0
                        if fuel_left > 0 and s == finish:
                            # 油量> 0，且已到达finish，那么本身就算一条路径，count = 1
                            count = 1
                        # 从s 到 finish 的路径和 等于从其他所有点到finish 路径和 之和
                        for i, l in enumerate(locations):
                            if i != s:
                                next_fuel_left = fuel_left - abs(l - locations[s])
                                if next_fuel_left >= 0:
                                    count += dp[next_fuel_left][i]
                                count = count % mod
                        dp[fuel_left][s] = count
        return dp[fuel][start]
