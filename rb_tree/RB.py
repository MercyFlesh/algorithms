import matplotlib.pyplot as plt
from pylab import rcParams


class _node:
    def __init__(self, key=None, val=None, red=True, left=None, right=None, parent=None):
       self.key = key
       self.val = val
       self.red = red
       self.left = left
       self.right = right
       self.parent = parent

    class none_leaf:
        def __init__(self):
            super().__init__()


class _none_leaf(_node):
    def __init__(self, parent):
        super().__init__(red=False, parent=parent)    


class RB:        
    def __init__(self):
        self.__root = None
        self.__size = 0


    def __iter__(self):
        arr = []
        self.__getlist(self.__root, arr)
        for i in arr:
            yield i


    def __getitem__(self, index):
        arr = []
        self.__getlist(self.__root, arr)
        return arr[index]


    def __getlist(self, root, arr=[], count=0):
        if root.key:
            count += 1
            self.__getlist(root.left, arr, count)
            arr.append(root)
            self.__getlist(root.right, arr, count)
        if count == self.__size:
            return arr


    def get_keys_list(self):
        arr = []
        self.__getlist(self.__root, arr)
        for i, n in zip(arr, range(len(arr))):
            arr[n] = i.key

        return arr           


    def print(self):
        arr = []
        for n in self:
            arr.append(n.key)
        print(arr)
        
        
    def find(self, key):
        find_node = self.__root
        if find_node:
            while find_node.key != key and find_node.key is not None:
                if find_node.key > key:
                    find_node = find_node.left
                else:
                    find_node = find_node.right
        if find_node and find_node.key:
            return find_node
        else:
            return None


    def _find_parent(self, key):
        parent_node = this_node = self.__root
        if this_node:
            while this_node.key is not None:
                parent_node = this_node
                if this_node.key > key:
                    this_node = this_node.left
                else:
                    this_node = this_node.right
        return parent_node


    def insert(self, key, val=None):
        new_node = _node(key, val)
        self.__size += 1
        parent_node = self._find_parent(key)
        if parent_node:
            new_node.parent = parent_node
            new_node.left = _none_leaf(new_node)
            new_node.right = _none_leaf(new_node)    
            
            if key < parent_node.key:
                parent_node.left = new_node
            else:
                parent_node.right = new_node
            self.__balance_insert(new_node)
        else:
            self.__root = new_node
            new_node.red = False
            new_node.right = _none_leaf(new_node)
            new_node.left = _none_leaf(new_node)
          

    def delete(self, key):
        delete_node = self.find(key)
        if delete_node:
            delete_color = delete_node.red
            self.__size -= 1

            if not delete_node.left.key and not delete_node.right.key:
                if delete_node is self.__root:
                    self.__root = None
                    return
                
                if delete_color == False:
                        self.__balance_delete(delete_node)
                if delete_node is delete_node.parent.left:
                    delete_node.parent.left = _none_leaf(delete_node.parent)   
                else:
                    delete_node.parent.right = _none_leaf(delete_node.parent) 
                return
             
            if delete_node.left.key and not delete_node.right.key:
                if not delete_node.parent:
                    self.__root = delete_node.left
                elif delete_node.parent.left is delete_node:
                    delete_node.parent.left = delete_node.left
                else:
                    delete_node.parent.right = delete_node.left
                delete_node.left.parent = delete_node.parent 
                target_node_for_balance = delete_node.left

            elif not delete_node.left.key and delete_node.right.key:
                if not delete_node.parent:
                    self.__root = delete_node.right              
                elif delete_node is delete_node.parent.left:
                    delete_node.parent.left = delete_node.right
                else:
                    delete_node.parent.right = delete_node.right
                delete_node.right.parent = delete_node.parent
                target_node_for_balance = delete_node.right
                
            else:
                next_node = delete_node.left
                while next_node.right.key:
                        next_node = next_node.right
                delete_color = next_node.red
                
                if next_node is not delete_node.left:
                    next_node.parent.right = next_node.left
                    next_node.left.parent = next_node.parent
                    if not delete_color:
                        target_node_for_balance = next_node.left
                    next_node.left = delete_node.left
                    next_node.left.parent =  next_node
                else:
                    target_node_for_balance = next_node.left
                   

                next_node.red = delete_node.red
                next_node.right = delete_node.right
                next_node.parent = delete_node.parent

                if delete_node is self.__root:
                    self.__root = next_node
                elif delete_node is delete_node.parent.left:
                    delete_node.parent.left = next_node
                else:
                    delete_node.parent.right = next_node

                delete_node.right.parent = next_node
            if not delete_color:
                self.__balance_delete(target_node_for_balance)
            
      
    def __balance_insert(self, target_node):
        while target_node.parent.red:
            grandfather = target_node.parent.parent
            if target_node.parent is grandfather.left:
                uncle = grandfather.right
                if uncle.key and uncle.red:
                        target_node.parent.red = False
                        uncle.red = False
                        grandfather.red = True
                        target_node = grandfather
                else:
                    if target_node is target_node.parent.right:
                        target_node = target_node.parent
                        self.__rotate_left(target_node)
                    
                    target_node.parent.red = False
                    grandfather = target_node.parent.parent
                    grandfather.red = True
                    self.__rotate_right(grandfather)    
            else:
                uncle = grandfather.left
                if uncle.red:
                        target_node.parent.red = False
                        uncle.red = False
                        grandfather.red = True
                        target_node = grandfather
                        if target_node.parent:
                            grandfather = target_node.parent.parent
                else:
                    if target_node is target_node.parent.left:
                        target_node = target_node.parent
                        self.__rotate_right(target_node)
                    target_node.parent.red = False
                    grandfather = target_node.parent.parent
                    grandfather.red = True
                    self.__rotate_left(grandfather)
            
            if target_node is self.__root:
                break
        self.__root.red = False


    def __balance_delete(self, target_node):
        while (not target_node.key or not target_node.red) and (target_node is not self.__root):
            if (target_node is target_node.parent.left):
                brother = target_node.parent.right
                if brother.key and brother.red:
                    brother.red = False
                    target_node.parent.red = True
                    self.__rotate_left(target_node.parent)
                    brother = target_node.parent.right
                
                elif brother.left.red or brother.right.red:
                    if not brother.right.red:
                        brother.left.red = False
                        brother.red = True
                        self.__rotate_right(brother)
                        brother = target_node.parent.right

                    if brother.right.key:
                        brother.right.red = False

                    brother.red = target_node.parent.red
                    target_node.parent.red = False
                    self.__rotate_left(target_node.parent)
                    target_node = self.__root
                
                else:
                    brother.red = True
                    target_node = target_node.parent
                    
            else:
                brother = target_node.parent.left
                if brother.key and brother.red:
                    brother.red = False
                    target_node.parent.red = True
                    self.__rotate_right(target_node.parent)
                    brother = target_node.parent.left
                
                elif brother.left.red or brother.right.red:
                    if not brother.left.red:
                        brother.right.red = False
                        brother.red = True
                        self.__rotate_left(brother)
                        brother = target_node.parent.left
                    brother.red = target_node.parent.red
                    target_node.parent.red = False
                    brother.left.red = False
                    self.__rotate_right(target_node.parent)
                    target_node = self.__root
                
                else:
                    brother.red = True
                    target_node = target_node.parent
        target_node.red = False
        self.__root.red = False


    def __rotate_right(self, rotate_node):
        buf_brother = rotate_node.left
        rotate_node.left = buf_brother.right
        if buf_brother.right:
            buf_brother.right.parent = rotate_node
        buf_brother.parent = rotate_node.parent
        if not rotate_node.parent:
            self.__root = buf_brother
        else:
            if rotate_node == rotate_node.parent.right:
                rotate_node.parent.right = buf_brother
            else:
                rotate_node.parent.left = buf_brother
        buf_brother.right = rotate_node
        rotate_node.parent = buf_brother
        

    def __rotate_left(self, rotate_node):
        buf_brother = rotate_node.right
        rotate_node.right = buf_brother.left
        if buf_brother.left.key:
            buf_brother.left.parent = rotate_node
        buf_brother.parent = rotate_node.parent
        if not rotate_node.parent:
            self.__root = buf_brother
        else:
            if rotate_node == rotate_node.parent.left:
                rotate_node.parent.left = buf_brother
            else:
                rotate_node.parent.right = buf_brother
        buf_brother.left = rotate_node
        rotate_node.parent = buf_brother


    def get_size(self):
        return self.__size


    def get_root(self):
        return self.__root
    

    def change_root(self, val=None):
        self.__root.val = val
    
    
    def set_value(self, key, val=None):
        this_node = self.__root
        while this_node.key != key:
            if key < this_node.key:
                this_node = this_node.left
            else:
                this_node = this_node.right
            if not this_node:
                return
        this_node.val = val
  

    def is_empty(self):
        if not self.__root:
            return True
        else:
            return False


    def __plot_node(self, node, show_none_leafs_flag, level=1, pos_x=0, pos_y=0):
        width = 2000 * (0.5 ** level)

        if not node.red: 
            plt.text(pos_x, pos_y, str(node.key), horizontalalignment = 'center', color='k', fontsize=12)
        else: 
            plt.text(pos_x, pos_y, str(node.key), horizontalalignment='center',color='r', fontsize=12)
    
        if node.left and (node.left.key or show_none_leafs_flag):
            p_x = [pos_x, pos_x - width]
            p_y = [pos_y - 1, pos_y - 15]

            if not node.left.red: 
                plt.plot(p_x, p_y,'k-')
            else: 
                plt.plot(p_x,p_y,'k-')
            self.__plot_node(node.left, show_none_leafs_flag, level + 1, pos_x - width, pos_y - 20)
    
        if node.right and (node.right.key or show_none_leafs_flag):
            self.__plot_node(node.right, show_none_leafs_flag, level + 1, pos_x + width, pos_y - 20)
            p_x = [pos_x, pos_x + width]
            p_y = [pos_y - 1, pos_y - 15]
            if node.right.red == 0:  
                plt.plot(p_x, p_y, 'k-')
            else: 
                plt.plot(p_x, p_y, 'k-')


    def show_tree(self, show_none_leafs_flag=False):
       node = self.__root
       rcParams['figure.figsize'] = (8, 5)
       fig, ax = plt.subplots()
       ax.axis('off')
       if not self.is_empty():
            self.__plot_node(node, show_none_leafs_flag)

       plt.show()


if __name__ == "__main__":
    test_cases = [
        30, 40, 25, 15, 26,
        28, 29, 10, 17, 8,
        20, 23, 21, 24, 6,
        4
    ]

    a = RB()
    for i in test_cases:
        a.insert(i)

    a.show_tree()
