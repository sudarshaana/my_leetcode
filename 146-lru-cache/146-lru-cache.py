class ListNode:
    def __init__(self, val, key = None, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        
        
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity;
        self.cache = dict()
        self.size = 0 
        
        # doubley connected linked list
        self.sentinel_head = ListNode(0)
        self.sentinel_tail = ListNode(0)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head
        
        # self.lr = self.sentinel_head
        # self.mr = self.sentinel_head
        
    def update_node(self, node):
        # removing the node
        node.prev.next = node.next 
        node.next.prev = node.prev
        
        # shifting to MRU
        prev_node = self.sentinel_tail.prev
        
        prev_node.next = node
        node.prev = prev_node
        
        node.next = self.sentinel_tail
        self.sentinel_tail.prev = node
        
    
    
    def get(self, key):
        
        if key in self.cache:
            node = self.cache[key]
            self.update_node(node)
            return node.val
        
        else:
            return -1
        
        
    def put(self, key, value):
        
        if key in self.cache:
            # update it
            node = self.cache[key]
            node.val = value
            self.update_node(node)
            
            
        else:
            # checking for size
            if self.size == self.capacity:
                # remove least used node from cache
                
                #self.show(self.sentinel_head)
                
                self.lr = self.sentinel_head.next
                
                
                to_remove = self.lr.key
                del self.cache[to_remove]
                
                # cache is full, remove LR data
                node_to_remove = self.lr
                self.sentinel_head.next = node_to_remove.next 
                node_to_remove.next.prev = self.sentinel_head
                self.lr = self.sentinel_head.next
                
                # adding new node
                node = ListNode(value, key)
                self.cache[key] = node
                
                
                # # shifting to MRU
                # self.mr.next = node
                # node.prev = self.mr
                # self.mr = node
                
                prev_point = self.sentinel_tail.prev
                prev_point.next = node
                node.prev = prev_point
                
                node.next = self.sentinel_tail
                self.sentinel_tail.prev = node
                
                # self.lr = self.sentinel_head.next
                # self.mr = self.sentinel_tail.prev
                
                
                
                #print("Capacity full {}:{}, removing {}, -> {}".format(key, value, to_remove, self.cache))
            
            else:
                #self.show(self.sentinel_head)
                
                self.size+=1
                node = ListNode(value, key)
                self.cache[key] = node
                
                
                # shifting to MRU
                # self.mr.next = node
                # node.prev = self.mr
                # self.mr = node
                
                prev_point = self.sentinel_tail.prev
                prev_point.next = node
                node.prev = prev_point
                
                node.next = self.sentinel_tail
                self.sentinel_tail.prev = node
                
                # self.lr = self.sentinel_head.next
                # self.mr = self.sentinel_tail.prev
                
                #print("Node k {}, v {} ".format(node.key, node.val))
                #print("Adding {}:{}, -> {}".format(key, value, self.cache))
                #print("From add")
                #self.show(self.sentinel_head)
                
 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)