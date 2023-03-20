class Solution:
# @return an integer
def divide(self, dividend, divisor):
    p = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    r = 0
    while dividend >= divisor:
        t, i = divisor, 1
        while dividend >= t:
            dividend -= t
            r += i
            i <<= 1
            t <<= 1
    if not p:
        r = -r
    return min(max(-2147483648, r), 2147483647)
