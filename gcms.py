from bin import *
from avl import *
from object import *
from exceptions import *
from node import *

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin_id_tree = AVLTree()
        self.obj_id_tree = AVLTree()
        self._bin_tree = AVLTree(comp_capacity)



    def add_bin(self, bin_id, capacity):
        bin = Bin(bin_id, capacity)
        self.bin_id_tree.insert(bin_id,bin)
        self._bin_tree.insert(capacity,bin_id)


    def add_object(self, object_id, size, color):
        object = Object(object_id, size, color)
        if color == Color.BLUE:
            bin_id=self._find_bin_compact_fit_least_id(object)

        elif color == Color.YELLOW:
            bin_id=self._find_bin_compact_fit_greatest_id(object)

        elif color == Color.RED:
            bin_id=self._find_bin_largest_fit_least_id(object)

        elif color == Color.GREEN:
            bin_id=self._find_bin_largest_fit_greatest_id(object)
        # print(bin_id)
        if(bin_id!=None):
            # print(bin_id)
            self.obj_id_tree.insert(object_id,object)
            bin=self.bin_id_tree.search(bin_id,None)
            self._bin_tree.delete(bin.capacity,bin_id)
            bin.add_object(object)
            self._bin_tree.insert(bin.capacity,bin_id)
            object.bin_id=bin_id
        else:
            raise NoBinFoundException



        

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        obj=self.obj_id_tree.search(object_id,None)
        if(obj!=None):
            self.obj_id_tree.delete(object_id,None)
            bin_id=obj.bin_id
            bin=bin_id.search(bin_id,None)
            bin.remove_object(object_id)
        else:
            return None

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        bin = self.bin_id_tree.search(bin_id,None)
        if(bin):
            return (bin.capacity,bin.give_list())


    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        obj=self.obj_id_tree.search(object_id,None)
        if(obj!=None):
            return obj.bin_id

    # def _find_bin(self, object_node):
    #     # Find the bin that can accommodate the object based on its color
    #     if object_node.color == Color.BLUE:
    #         return self._find_bin_compact_fit_least_id(object_node)
    #     elif object_node.color == Color.YELLOW:
    #         return self._find_bin_compact_fit_greatest_id(object_node)
    #     elif object_node.color == Color.RED:
    #         return self._find_bin_largest_fit_least_id(object_node)
    #     elif object_node.color == Color.GREEN:
    #         return self._find_bin_largest_fit_greatest_id(object_node)
    #     else:
    #         raise Exception("Invalid color code")


    def _find_bin_compact_fit_least_id(self, object_node):
        best_size=float('inf')
        curr=self._bin_tree.root
        while curr:
            if(curr.key>=object_node.size):
                best_size=min(best_size,curr.key)
                curr=curr.left
            else:
                curr=curr.right
        if(best_size==float('inf')):
            return None
        curr=self._bin_tree.root
        best_id=float('inf')
        while curr:
            if(curr.key==best_size):
                best_id=min(curr.value,best_id)
                curr=curr.left
            elif(curr.key>best_size):
                curr=curr.left
            else:
                curr=curr.right
        return best_id

    def _find_bin_compact_fit_greatest_id(self, object_node):
        # done
        best_size=float('inf')
        curr=self._bin_tree.root
        while curr:
            if(curr.key>=object_node.size):
                best_size=min(best_size,curr.key)
                curr=curr.left
            else:
                curr=curr.right
        if(best_size==float('inf')):
            return None
        curr=self._bin_tree.root
        best_id=-float('inf')
        while curr:
            if(curr.key==best_size):
                best_id=max(curr.value,best_id)
                curr=curr.right
            elif(curr.key>best_size):
                curr=curr.left
            else:
                curr=curr.right
        return best_id

    def _find_bin_largest_fit_least_id(self, object_node):
        # DONE
        best_size=-float('inf')
        curr=self._bin_tree.root
        while curr:
            if(curr.key>=object_node.size):
                best_size=max(best_size,curr.key)
                curr=curr.right
            else:
                curr=curr.right
        if(best_size==-float('inf')):
            return None
        curr=self._bin_tree.root
        best_id=float('inf')
        while curr:
            if(curr.key==best_size):
                best_id=min(curr.value,best_id)
                curr=curr.left
            elif(curr.key>best_size):
                curr=curr.left
            else:
                curr=curr.right
        return best_id

    def _find_bin_largest_fit_greatest_id(self, object_node):
        # DONE
        best_size=-float('inf')
        curr=self._bin_tree.root
        while curr:
            if(curr.key>=object_node.size):
                best_size=max(best_size,curr.key)
                curr=curr.right
            else:
                curr=curr.right
        if(best_size==-float('inf')):
            return None
        curr=self._bin_tree.root
        best_id=-float('inf')
        while curr:
            if(curr.key==best_size):
                best_id=max(curr.value,best_id)
                curr=curr.right
            elif(curr.key>best_size):
                curr=curr.left
            else:
                curr=curr.right
        return best_id
        

    def bins(self):
        tree=self._bin_tree
        lst=[]
        def traverse(node):
            if(node!=None):
                traverse(node.left)
                lst.append((node.key,node.value))
                traverse(node.right)
        traverse(tree.root)
        print(lst)
    def binsid(self):
        tree=self.bin_id_tree
        lst=[]
        def traverse(node):
            if(node!=None):
                traverse(node.left)
                lst.append((node.key))
                traverse(node.right)
        traverse(tree.root)
        print(lst)







    
    