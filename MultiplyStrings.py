def multiply(n1, n2):
    final = [0] * (len(n1) + len(n2))
    pos = len(final)-1
    
    for n1 in reversed(n1):
        temp = pos
        for n2 in reversed(n2):
            final[temp] += int(n1) * int(n2)
            final[temp-1] += final[temp]/10
            final[temp] %= 10
            temp -= 1
        pos -= 1
        
    p = 0
    while p < len(product)-1 and final[p] == 0:
        p += 1

    return ''.join(map(str, final[p:]))
