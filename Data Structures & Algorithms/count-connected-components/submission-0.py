class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(s):
            vis[s] = True
            for v in adj[s]:
                if not vis[v]:
                    dfs(v)
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans, vis = 0, [False]*n
        for i in range(n):
            if not vis[i]:
                dfs(i)
                ans += 1
        return ans