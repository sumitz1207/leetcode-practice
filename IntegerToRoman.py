def integerToRoman(self, n):
    v = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    num = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    final, i = "", 0
    while n:
        final += (n//v[i]) * num[i]
        n %= v[i]
        i += 1
    return final
