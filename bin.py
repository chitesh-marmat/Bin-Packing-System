from avl import *
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.objects= AVLTree(comp_id)

    def add_object(self, object):
        # Implement logic to add an object to this bin
        if self.capacity >= object.size:
            self.capacity-=object.size
            self.objects.insert(object.object_id,object)
        else:
            raise Exception("Insufficient capacity")

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        obj = self.objects.search(object_id,None)
        self.capacity+=obj.size
        if obj is not None:
            self.objects.delete(obj,object_id)
        else:
            raise Exception("Object not in bin")
    
    def give_list(self):
        lst=[]
        def inorder(node):
            if(node):
                inorder(node.left)
                lst.append(node.key)
                inorder(node.right)
        inorder(self.objects.root)
        return lst
