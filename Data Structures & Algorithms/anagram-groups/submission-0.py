class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sortedS = sorted(i)
            res["".join(sortedS)].append(i)
        return list(res.values())