class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ ord(j) - ord('a') ] += 1
            hashTable[tuple(count)].append(i)
        return hashTable.values()