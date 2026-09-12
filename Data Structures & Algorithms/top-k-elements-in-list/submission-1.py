class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list = [[] for i in range(len(nums)  + 1)]
        print(list)
        count = {}
        outList = []
        for num in nums: 
            count[num] = count.get(num, 0) + 1
        for key, value in count.items():
            list[value].append(key)
        index = len(nums)
        for i in range(len(nums), 0, -1):
            print(i)
            if len(list[i]) == 0:
                continue
            for l in list[i]:
                outList.append(l)
            if len(outList) == k:
                return outList
        return outList        