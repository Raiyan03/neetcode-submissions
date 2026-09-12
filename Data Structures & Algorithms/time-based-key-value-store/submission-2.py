class TimeMap:

    def __init__(self):
        self.hashTable = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashTable[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.hashTable.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp >= values[mid][1]:
                res = values[mid][0]
                l  = mid + 1
            elif timestamp <= values[mid][1]:
                r = mid - 1
            else:
                return values[mid][0]
        return res