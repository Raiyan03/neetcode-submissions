class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashMap ={}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.tail.prev
        next = self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        self.remove(self.hashMap[key])
        self.insert(self.hashMap[key])
        return self.hashMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        self.hashMap[key] = Node(key, value)
        self.insert(self.hashMap[key])
        if len(self.hashMap.keys()) > self.cap:
            temp = self.head.next
            self.remove(temp)
            del self.hashMap[temp.key]
