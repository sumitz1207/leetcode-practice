class Solution:
    def rotate(self, final, i):
        j = len(final)
        i = i % j
        final[:] = final[j-i:] + final[:j-i]
