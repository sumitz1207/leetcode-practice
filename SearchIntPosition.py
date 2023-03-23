class Solution:
    def searchI(self, n, t):
        final, e = 0, len(n)
        while final < e:
            m = (final + e)//2
            if n[m] >= t:
                e = m
            else:
                final = m + 1
        return final
