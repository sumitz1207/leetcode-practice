class Solution(object):
    def intReplace(self, num):
        rotate = 0
        while num > 1:
            rotate += 1
            if num % 2 == 0:
                num //= 2
            elif num % 4 == 1 or num == 3:
                num -= 1
            else:
                num += 1
        return rotate
