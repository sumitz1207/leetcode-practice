def wordPattern(self, p, r):
    f = lambda s: map({}.setdefault, s, range(len(s)))
    return f(p) == f(r.split())
