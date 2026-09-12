class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list = [[] for i in range(len(nums)  + 1)]
        count = {}
        outList = []

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key, val in count.items():
            list[val].append(key)
        for i in range(len(list) - 1, -1, -1 ):
            for j in list[i]:
                outList.append(j)
                if len(outList) == k:
                    return outList
        return outList