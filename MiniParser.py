class Solution:
    def deserialize(self, s):
        sta, n, l = [], "", None
        for c in s:
            if c.isdigit() or c == "-": n += c
            elif c == "," and n:
                sta[-1].add(nest(int(n)))
                n = ""
            elif c == "[":
                elem = nest()
                if sta: sta[-1].add(elem)
                sta.append(elem)
            elif c == "]":
                if n:
                    sta[-1].add(nest(int(n)))
                    n = ""
                l = sta.pop()
        return l if l else nest(int(n))
