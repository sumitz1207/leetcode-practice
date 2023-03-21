class Solution:
    def gameOfLife(self, b: List[List[int]]) -> None:
        m, n = len(b), len(b[0])
        d = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        for i in range(m):
            for j in range(n):
                l = 0
                for r, c in d:
                    nr, nc = i + r, j + c
                    if 0 <= nr < m and 0 <= nc < n and abs(b[nr][nc]) == 1: 
                        l += 1
                if b[i][j] == 1:
                    if l < 2 or l > 3:   
                        b[i][j] = -1
                else:
                    if l == 3:  
                        b[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if b[i][j] == 2:    b[i][j] = 1
                elif b[i][j] == -1: b[i][j] = 0
