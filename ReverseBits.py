class Solution:
    def final(self, n):
        o='{0:032b}'.format(n)
        r=o[::-1]
        return int(r,2)
