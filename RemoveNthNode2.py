class Solution:
    def remove(self, h, n):
        def remove(h):
            if not h:
                return 0, h
            i, h.next = rem(h.next)
            return i+1, (h, h.next)[i+1 == n]
        return rem(h)[1]
