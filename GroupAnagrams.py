from collections import defaultdict

class Solution:
    def ga(self, strs: List[str]) -> List[List[str]]:
        help = defaultdict(list)
        for i in strs:
            help[tuple(sorted(i))].append(i)
        return list(help.values())
