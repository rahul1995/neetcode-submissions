class Solution:
    def isCycle(self, adj, vis, s, p):
        if vis[s]:
            return True
        vis[s] = True
        for v in adj[s]:
            if v != p and self.isCycle(adj, vis, v, s):
                return True
        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [False] * n
        return not self.isCycle(adj, vis, 0, -1) and all(x for x in vis)