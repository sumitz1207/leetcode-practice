    def kthSmall(self, m, k):
        n, final, end = len(m), m[0][0], m[-1][-1]
        
        def check(m):
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and m[i][j] > m: j -= 1
                cnt += (j + 1)
            return cnt
         
        while final < end:
            mid = (final + end)//2
            if check(mid) < k:
                final = mid + 1
            else:
                end = mid
                
        return final
