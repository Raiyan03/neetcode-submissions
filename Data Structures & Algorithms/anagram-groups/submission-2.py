class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = defaultdict(list)
        for s in strs:
            count = [0] * 26 #this mean there are 26 characters which will be zero and after every time we encounter a character we will inject +1
            for c in s:
                # We will be subtracting the it with the ascii value of a every time to determine the index of 
                # Example: ascii'a' is 10 the ascii'b' will be 11 so on subtracting we will get the exact index
                count[ ord(c) - ord('a')] += 1
            #Converting it into tuple because list is a mutable data type which cannot be used as a key
            hashTable[tuple(count)].append(s) 
        print(hashTable.keys())
        return hashTable.values()