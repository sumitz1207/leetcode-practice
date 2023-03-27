class Solution:
    def removeNthFromEnd(self, h, x):
        def index(n):
            if not n:
                return 0
            i = index(n.next) + 1
            if i > x:
                n.next.val = n.val
            return i
        index(h)
        return h.next
