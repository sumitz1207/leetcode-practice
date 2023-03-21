class Solution(object):
    def intr(self, n):
        final = 0
        while n > 1:
            final += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return final
