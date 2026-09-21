class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + '#' + s for s in strs)
    def decode(self, s: str) -> List[str]:
        i, ans = 0, []
        while i < len(s):
            end = s.find('#', i)
            length = int(s[i:end])
            ans.append(s[end+1:end+1+length])
            i = end+1+length
        return ans