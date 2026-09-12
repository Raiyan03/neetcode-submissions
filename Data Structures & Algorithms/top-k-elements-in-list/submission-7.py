class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        tables = [[] for i in range(len(nums)+ 1)]
        out = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for key, v in count.items():
            tables[v].append(key)
        
        for n in range(len(tables) -1, -1, -1):
            for c in tables[n]:
                out.append(c)
                if len(out) == k:
                    return out
                    