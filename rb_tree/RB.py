import matplotlib.pyplot as plt
from pylab import rcParams

class _node:
    def __init__(self, key = None, val = None, red = True, left = None, right = None, parent = None):
       self.key = key
       self.val = val
       self.red = red
       self.left = left
       self.right = right
       self.parent = parent

            
class RB:        
    def __init__(self):
        self.__root = None
        self.__count = 0

    def __iter__(self):
        arr = []
        self.__getlist(self.__root, arr)
        for i in arr:
            yield i

    def __getitem__(self, index):
        arr = []
        self.__getlist(self.__root, arr)
        return arr[index]
    
    def __getlist(self, root, arr = [], count = 0):
        if root != None:
            count += 1
            self.__getlist(root.left, arr, count)
            arr.append(root)
            self.__getlist(root.right, arr, count)
        if count == self.__count:
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
        
        """
        self.__getlist(self.__root, arr)
        for n, i in zip(arr, range(len(arr))):
            arr[i] = n.key
        print(arr)
        """
        
        
    def insert(self, key, val = None):
        new_node = _node(key, val)
        this_node = self.__root
        self.__count += 1
        if this_node != None:
            while this_node != None:
                parent_node = this_node
                if this_node.key > key:
                    this_node = this_node.left
                else:
                    this_node = this_node.right
                
            new_node.parent = parent_node
            if key < parent_node.key:
                parent_node.left = new_node
            else:
                parent_node.right = new_node

            self.__balance_insert(new_node)
        else:
            new_node.red = False
            self.__root = new_node
            #new_node.left = _node(red=False)
            #new_node.right = _node(red=False)
          
            
    def delete(self, key):
        this_node = self.__root
        if this_node != None:
            while this_node.key != key:
                if this_node == None:
                    return
                if this_node.key > key:
                    this_node = this_node.left
                else:
                    this_node = this_node.right
            
            color = this_node.red
            original_color = this_node.red
            self.__count -= 1
            if (this_node.left == None) & (this_node.right == None):
                if color == False:
                        self.__balance_delete(this_node, original_color)
                if this_node is this_node.parent.left:
                    this_node.parent.left = None    #_node(red=False)
                else:
                    this_node.parent.right = None     #_node(red=False)

                return
             
            if (this_node.left != None) & (this_node.right == None):
                if this_node.parent == None:
                    self.__root = this_node.left
                elif this_node.parent.left is this_node:
                    this_node.parent.left = this_node.left
                else:
                    this_node.parent.right = this_node.left
                this_node.left.parent = this_node.parent 
                this_node = this_node.left
                x = this_node

            elif (this_node.left == None) & (this_node.right != None):
                if this_node.parent == None:
                    self.root = this_node.right              
                elif this_node is this_node.parent.left:
                    this_node.parent.left = this_node.right
                else:
                    this_node.parent.right = this_node.right
                this_node.right.parent = this_node.parent
                this_node = this_node.right
                x = this_node
                
            else:
                next = this_node.left
                if next.right != None:
                    while next.right != None:
                        next = next.right
                color = next.red
                if next is not this_node.left:
                    next.parent.right = next.left
                    if color == False:
                        x = next.left

                    if next.left != None:
                        next.left.parent = next.parent
                    else:
                        x = _node(red=False, parent=next.parent)
                            
                    next.left = this_node.left
                    next.left.parent =  next
                elif next.left != None:
                    x = next.left
                else:
                    x = _node(red=False, parent=next)
                   

                next.red = original_color
                next.right = this_node.right
                next.parent = this_node.parent

                if this_node is self.__root:
                    self.__root = next
                elif this_node is this_node.parent.left:
                    this_node.parent.left = next
                else:
                    this_node.parent.right = next

                this_node = next
                next.right.parent = next
            if color == False:
                self.__balance_delete(x, original_color)
            
      
    def __balance_insert(self, new_node):
        grandfather = new_node.parent.parent
        while new_node.parent.red:    
            if new_node.parent is grandfather.left:
                uncle = grandfather.right
                if uncle != None:
                    if uncle.red:
                        new_node.parent.red = False
                        uncle.red = False
                        grandfather.red = True
                        new_node = grandfather
                else:
                    if new_node is new_node.parent.right:
                        new_node = new_node.parent
                        self.__rotate_left(new_node)
                    
                    new_node.parent.red = False
                    grandfather = new_node.parent.parent
                    grandfather.red = True
                    self.__rotate_right(grandfather)    
            else:
                uncle = grandfather.left
                
                if uncle != None and uncle.red:
                        new_node.parent.red = False
                        uncle.red = False
                        grandfather.red = True
                        new_node = grandfather
                        if new_node.parent != None:
                            grandfather = new_node.parent.parent
                else:
                    if new_node is new_node.parent.left:
                        new_node = new_node.parent
                        self.__rotate_right(new_node)
                    new_node.parent.red = False
                    grandfather = new_node.parent.parent
                    grandfather.red = True
                    self.__rotate_left(grandfather)
            if new_node is self.__root:
                break
        self.__root.red = False


    def __balance_delete(self, del_node, original_color):
        while (del_node == None or del_node.red == False) & (del_node != self.__root):
            if (del_node is del_node.parent.left) or (del_node.key == None and del_node.parent.left == None):
                brother = del_node.parent.right
                if brother != None and brother.red:
                    brother.red = False
                    del_node.parent.red = True
                    self.__rotate_left(del_node.parent)
                    brother = del_node.parent.right
                if ((brother.left != None) and (brother.left.red == True)) or (brother.right != None and brother.right.red == True):
                    if brother.right != None and brother.right.red == False:
                        brother.left.red = False
                        brother.red = True
                        self.__rotate_right(brother)
                        brother = del_node.parent.right

                    if brother.right != None:
                        brother.right.red = False

                    brother.red = del_node.parent.red
                    del_node.parent.red = False
                    self.__rotate_left(del_node.parent)
                    del_node = self.__root
                else:
                    #when childs black
                    brother.red = True
                    del_node = del_node.parent
                    
            else:
                brother = del_node.parent.left
                if brother != None and brother.red:
                    brother.red = False
                    del_node.parent.red = True
                    self.__rotate_right(del_node.parent)
                    brother = del_node.parent.left
                if ((brother.left != None) and (brother.left.red == True)) or (brother.right != None and brother.right.red == True):
                    if brother.left and brother.left.red == False:
                        brother.right.red = False
                        brother.red = True
                        self.__rotate_left(brother)
                        brother = del_node.parent.left
                    brother.red = del_node.parent.red
                    del_node.parent.red = False
                    brother.left.red = False
                    self.__rotate_right(del_node.parent)
                    del_node = self.__root
                else:
                    brother.red = True
                    del_node = del_node.parent
        del_node.red = False
        self.__root.red = False


    def __rotate_right(self, rotate_node):
        buf_brother = rotate_node.left
        rotate_node.left = buf_brother.right
        if buf_brother.right != None:
            buf_brother.right.parent = rotate_node
        buf_brother.parent = rotate_node.parent
        if rotate_node.parent == None:
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
        if buf_brother.left != None:
            buf_brother.left.parent = rotate_node
        buf_brother.parent = rotate_node.parent
        if rotate_node.parent == None:
            self.__root = buf_brother
        else:
            if rotate_node == rotate_node.parent.left:
                rotate_node.parent.left = buf_brother
            else:
                rotate_node.parent.right = buf_brother
        buf_brother.left = rotate_node
        rotate_node.parent = buf_brother


    def get_count(self):
        return self.__count


    def get_root(self):
        return self.__root
    

    def change_root(self, val = None):
        self.__root.val = val 
    

    def get_node(self, key):
        this_node = self.__root
        while this_node.key != key:
            if key < this_node.key:
                this_node = this_node.left
            else:
                this_node = this_node.right
            if this_node == None:
                return

        return this_node
    
    
    def set_value(self, key, val = None):
        this_node = self.__root
        while this_node.key != key:
            if key < this_node.key:
                this_node = this_node.left
            else:
                this_node = this_node.right
            if this_node == None:
                return

        this_node.val = val
  
    def is_empty(self):
        if self.__root == None:
            return True
        else:
            return False

    def __plot_node(self, node, level = 1, pos_x = 0, pos_y = 0):
        width = 2000 * (0.5 ** level)

        if node != None and node.red == 0: 
            plt.text(pos_x, pos_y, str(node.key), horizontalalignment = 'center', color='k', fontsize = 12)
        else: 
            plt.text(pos_x, pos_y, str(node.key), horizontalalignment='center',color = 'r', fontsize = 12)
    
        if node != None and node.left != None:
            p_x = [pos_x, pos_x - width]
            p_y = [pos_y - 1, pos_y - 15]

            if node.left != None and node.left.red == 0: 
                plt.plot(p_x, p_y,'k-')
            else: 
                plt.plot(p_x,p_y,'k-')
            self.__plot_node(node.left, level + 1, pos_x - width, pos_y - 20)
    
        if node != None and node.right != None:
            self.__plot_node(node.right, level + 1, pos_x + width, pos_y - 20)
            p_x = [pos_x, pos_x + width]
            p_y = [pos_y - 1, pos_y - 15]
            if node.right != None and node.right.red == 0:  
                plt.plot(p_x, p_y, 'k-')
            else: 
                plt.plot(p_x, p_y, 'k-')


    def show_tree(self):
       node = self.__root
       rcParams['figure.figsize'] = (8, 5)
       fig, ax = plt.subplots()
       ax.axis('off')
       if not self.is_empty():
            self.__plot_node(node)

       plt.show()




if __name__ == "__main__":
    test_cases = [
        0, 1, 2, 3, 4, 5, 6, 7,
        8, 9, 10, 11, 12, 13, 14, 
        15, 16, 17, 18, 18, 20, 21
    ]
    a = RB()
    for i in test_cases:
        a.insert(i)
    a.delete(0)
    a.delete(2)
    a.delete(5)
    a.delete(7)
    a.delete(18)
    a.delete(9)
    a.delete(17)
    a.delete(20)
    a.delete(16)
    a.show_tree()