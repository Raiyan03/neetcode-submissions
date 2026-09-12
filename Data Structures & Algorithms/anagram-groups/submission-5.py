class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = defaultdict(list)
        outList = []
        for s in strs:
            alphList = [0] * 26
            for i in s:
                asci = ord(i) - ord('a')
                alphList[asci] = alphList[asci] + 1
            hashTable[tuple(alphList)].append(s)
        return hashTable.values()