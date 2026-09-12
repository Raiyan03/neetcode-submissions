class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet = { }
        rList = []
        if len(strs) == 1:
            return  [[strs[0]]]
        for n, i in enumerate(strs):
            sortedStr = ''.join(sorted(i))
            if sortedStr not in hashSet:
                hashSet[sortedStr] = [i]
            else:
                hashSet[sortedStr].append(i)

        for i in hashSet:
            rList.append(hashSet[i])
        return rList        