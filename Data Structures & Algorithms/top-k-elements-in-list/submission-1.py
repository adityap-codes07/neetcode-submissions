class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1

        sorted_items = sorted(freq.items(), key = lambda x : x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
