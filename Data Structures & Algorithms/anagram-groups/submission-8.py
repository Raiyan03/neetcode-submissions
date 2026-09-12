class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet = defaultdict(list)

        for s in strs:
            table = [0] * 26
            for i in s:
                table[ord(i) - ord('a')] += 1
            hashSet[tuple(table)].append(s)
        
        return list(hashSet.values())
