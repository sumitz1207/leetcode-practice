class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = list(zip(*strs))
        final = ""
        for i in temp:
            if len(set(i))==1:
                final += i[0]
            else:
                break
        return final
