from node import Node

def comp_id(node_1,node_2) :
    if node_1.key < node_2.key :
        return 1
    if node_1.key > node_2.key :
        return -1
    return 0
def comp_capacity(node_1, node_2):
    if node_1.key < node_2.key:
        return 1
    elif node_1.key > node_2.key:
        return -1
    else:
        if node_1.value < node_2.value:
            return 1
        elif node_1.value > node_2.value:
            return -1
        else:
            return 0


class AVLTree:
    def __init__(self, compare_function = comp_id):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.size += 1

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)

        cmp = self.comparator(node, Node(key, value))
        if cmp < 0:
            node.left = self._insert(node.left, key, value)
        elif cmp > 0:
            node.right = self._insert(node.right, key, value)
        else:
            # Node with same capacity and key already exists
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)
        if balance > 1:
            if self.comparator(node.left, Node(key, value)) < 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        elif balance < -1:
            if self.comparator(node.right, Node(key, value)) > 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, node):
        pivot = node.right
        node.right = pivot.left
        pivot.left = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        pivot.height = 1 + max(self._get_height(pivot.left), self._get_height(pivot.right))

        return pivot

    def _right_rotate(self, node):
        pivot = node.left
        node.left = pivot.right
        pivot.right = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        pivot.height = 1 + max(self._get_height(pivot.left), self._get_height(pivot.right))

        return pivot




    def find_suitable(self, key):
        p = Node(key)
        return self._find_suitable(self.root, p).value if self._find_suitable(self.root, p) is not None else None
    def _find_suitable(self, root, p):
        if root is None:
            return None
        cmp = self.comparator(root, p)
        poss = None
        while root is not None:
            if cmp<0:
                root = root.right
            elif cmp>0:
                poss = root
                root = root.left
            else:
                return root
        return poss
    
    def search(self,key, value=None):
        p = Node(key, value)
        return self._search(self.root,p).value if self._search(self.root,p) is not None else None
    
    def _search(self, root, p):
        if root is None:
            return None

        cmp = self.comparator(root, p)
        if cmp < 0:
            return self._search(root.left, p)
        elif cmp > 0:
            return self._search(root.right, p)
        else:
            return root
    def find_least(self):
        return self._find_least(self.root).key
    def _find_least(self, root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root
    def find_greatest(self):
        return self._find_greatest(self.root).key
    def _find_greatest(self, root):
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root

    def delete(self, key, value=None):
        p = Node(key, value)
        self.root = self._delete(self.root, p)
        self.size -= 1

    def _delete(self, root, p):
        if root is None:
            return root


        cmp = self.comparator(root, p)
        if cmp < 0:
            root.left = self._delete(root.left, p)
        elif cmp > 0:
            root.right = self._delete(root.right,p)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.value = temp.value
            root.key = temp.key
            root.right = self._delete(root.right, temp)

        if root is None:
            return None

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)
        if balance > 1:
            if self._get_balance(root.left) >= 0:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
        elif balance < -1:
            if self._get_balance(root.right) <= 0:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root
        
        
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left)
            yield
            self._in_order(node.right)










