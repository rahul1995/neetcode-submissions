class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ltr, rtl, balls = [0]*n, [0]*n, 0
        for i in range(n):
            ltr[i] += (0 if i == 0 else ltr[i-1]) + balls
            balls += int(boxes[i])
        balls = 0
        for i in range(n-1, -1, -1):
            rtl[i] += (0 if i == n-1 else rtl[i+1]) + balls
            balls += int(boxes[i])
        return [ltr[i]+rtl[i] for i in range(n)]