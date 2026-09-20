class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        uniq = set()
        for w in words:
            for c in w:
                uniq.add(c)
        n = len(words)
        adj, inorder = defaultdict(list), defaultdict(int)
        for i in range(n-1):
            s1, s2 = words[i], words[i+1]
            j = 0
            while j < len(s1) and j < len(s2) and s1[j] == s2[j]:
                j += 1
            if j == len(s2) and j != len(s1):
                return ''
            if j < len(s1) and j < len(s2):
                adj[s1[j]].append(s2[j])
                inorder[s2[j]] += 1
        q, ans = deque(), ''
        for node in uniq:
            if inorder[node] == 0:
                q.append(node)
        while q:
            u = q.popleft()
            ans += u
            for v in adj[u]:
                inorder[v] -= 1
                if inorder[v] == 0:
                    q.append(v)
        return ans if len(ans) == len(uniq) else ''
