class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = defaultdict(int)
        for n in nums:
            hs[n] += 1
        
        ls = []
        for key,v in hs.items():
            heapq.heappush(ls,[-v,key])
        
        res = []
        i = 0
        while i < k:
            res.append(heapq.heappop(ls)[1])
            i += 1
        return res