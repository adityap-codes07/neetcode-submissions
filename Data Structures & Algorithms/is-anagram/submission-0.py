class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ele_s = []
        for i in s:
            ele_s.append(i)
        ele_t = []
        for i in t:
            ele_t.append(i)
        ele_s.sort()
        ele_t.sort()
        if len(s) != len(t):
            return False
        if ele_s == ele_t:
            return True
        return False
