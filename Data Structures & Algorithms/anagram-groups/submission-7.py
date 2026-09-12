class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = defaultdict(list)
        for word in strs:
            alphaSet = [0] * 26
            for i in word:
                index = ord(i) - ord('a')
                alphaSet[index] += 1
            hashTable[tuple(alphaSet)].append(word)
        return hashTable.values() 
