import hashlib
class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        self.key = hashlib.sha256(value) # 将数据的哈希值作为哈希表中的key

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node):
        if node is  None:
            return
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = node.next = None
        else:
            # 先将节点从队列中取出
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            # 将当前节点挪到队列头部
            node.next = self.head
            self.head = node
            node.prev = None

    def add_front(self, value):
        node = LinkListNode(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        return node

class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0 # 记录缓存的数量
        self.hash_table = {}
        self.elements = LinkedList()
        self.elements_tail = None

    def add(self, key, value):
        if key in self.hash_table: #看看数据是否已经存在
            node = self.hash_table[key]
            node.value = value # 将数据存入节点
            self.elements.move_to_front(node)
            return False  # 没有增加新节点
        elif self.current_size >= self.max_size:
            self.evict_one_entry() # 缓存不足，执行清除操作

        node = self.elements.add_front(value) # 增加一个新节点并挪到队列头部
        self.hash_table[key] = node # 让哈希表指向节点以便后面查询时提示查找速度
        self.elements_tail = self.elements.tai

        return True # 通知调用者有新节点生成

    def evict_one_entry(self):
        if not self.hash_table:
            return False # 当前哈希表为空，缓存没有数据

        node = self.elements_tail
        self.elements_tail = node.prev # 修改尾部节点
        if self.elements_tail is not None:
            self.elements_tail.next = None
        del self.hash_table[node.key] # 将节点从哈希表删除
        return True

    def get(self, key):
        if (key in self.hash_table) is False:
            return None
        node = self.hash_table[key]
        return node.value


