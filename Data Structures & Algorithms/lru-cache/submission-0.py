class ListNode:
    def __init__(
        self,
        key: int = 0,
        value: int = 0,
        prev: Optional["ListNode"] = None,
        next: Optional["ListNode"] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> node, not key -> value
        self.hm = {}

        # left.next is the least recently used node.
        # right.prev is the most recently used node.
        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: ListNode) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_at_right(self, node: ListNode) -> None:
        previous_most_recent = self.right.prev

        previous_most_recent.next = node
        node.prev = previous_most_recent

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        node = self.hm[key]

        # It was just accessed, so it becomes most recently used.
        self.remove(node)
        self.insert_at_right(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            old_node = self.hm[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.hm[key] = node
        self.insert_at_right(node)

        if len(self.hm) > self.capacity:
            # Node immediately after left is least recently used.
            lru = self.left.next
            self.remove(lru)
            del self.hm[lru.key]