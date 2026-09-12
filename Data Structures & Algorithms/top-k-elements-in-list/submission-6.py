class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        hashTable = {}

        for num in nums:
            hashTable[num] = 1 + hashTable.get(num, 0)

        for key, value in hashTable.items():
            freq[value].append(key)

        outList = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                outList.append(j)
                if len(outList) == k:
                    return outList

