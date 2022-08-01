
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTree:
    def __init__(self):
        self.root = None
    
    def search(self, root, val):
        if root == None:
            return False
        if val ==  root.val:
            return True
        elif val > root.val:
            return self.search(root.right, val)
        else:
            return self.search(root.left, val)
        
        
    def add(self, root, val):
        
        if not root:
            return TreeNode(val)
        
        # assuming no duplicate value
        if val > root.val:
            root.right = self.add(root.right, val)
            #print("adding to right ", val, "After ", root.right.val)
        elif val == root.val:
            #print("adding to duplicate ", val)
            return root
        else:
            root.left = self.add(root.left, val)    
            #print("adding to left ", val, "After ", root.left.val)
        
        return root
            
            
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(left, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    
    def remove(self, root, val):
        if not root:
            return root
        
        if val > root.val:
            root.right = self.remove(root.right, val)
        elif val < root.val:
            root.left = self.remove(root.left, val)
        else:
            # here is the value
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                self.remove(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                self.remove(root.left, root.val)
        return root
    
    def contains(self, root, val):
        return self.search(root, val)

class Bucket:

    def __init__(self):
        self.bst = BSTree()
    
    def add(self, value):
        self.bst.root = self.bst.add(self.bst.root, value)
        
    def remove(self, value):
        self.bst.root = self.bst.remove(self.bst.root, value)
        
    def contains(self, value):
        return self.bst.contains(self.bst.root, value)
        
        

class MyHashSet:

    def __init__(self):
        self.key = 919
        self.bucket = [Bucket() for i in range(self.key)] 
                
    def _get_hash(self, key):
        return key%self.key
    
    def add(self, key):
        hash_key = self._get_hash(key)
        #print("HashKey for adding ", hash_key)
        self.bucket[hash_key].add(key)
        
    def remove(self, key):
        hash_key = self._get_hash(key)
        self.bucket[hash_key].remove(key)
        
    def contains(self, key):
        hash_key = self._get_hash(key)
        return self.bucket[hash_key].contains(key)
        