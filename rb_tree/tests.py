from RB import RB
import unittest

class rb_tree_test(unittest.TestCase):
    def test_get_root(self):
        a = RB()
        self.assertIsNone(a.get_root())
        a.insert(5)
        self.assertEqual(a.get_root().key, 5)

    def test_get_node(self):
        a = RB()
        a.insert(5)
        a.insert(7)
        a.insert(10)
        self.assertIsNone(a.find(15))
        self.assertEqual(a.find(5).key, 5)
        self.assertEqual(a.find(7).key, 7)
        self.assertEqual(a.find(10).key, 10)
        self.assertIs(a.find(5), a[0])
        self.assertIs(a.find(7), a[1])
        self.assertIs(a.find(10), a[2])


    def test_get_keys_list(self):
        a = RB()
        a.insert(7)
        a.insert(5)
        a.insert(10)
        ok_keys = [5, 7, 10]
        self.assertEqual(a.get_keys_list(), ok_keys)


    def test_insert(self):
        a = RB()
        cases_keys = [5, 4, 12, 7, 14, 6, 9, 8, 11, 10]
        """
        7_b: key_color
          __7_b_____
         /          \
       _5_b_         12_b
      /     \       /    \
    4_b      6_b   9_r    14_b 
                  /   \
                8_b    11_b
                      /
                    10_b
        """
        for i in cases_keys:
            a.insert(i)
        node_root = a.get_root()
        node_5 = node_root.left
        node_4 = node_5.left
        node_6 = node_5.right
        node_12 = node_root.right
        node_9 = node_12.left
        node_8 = node_9.left
        node_11 = node_9.right
        node_10 = node_11.left
        node_14 = node_12.right
        self.assertEqual(a.find(7), node_root)
        self.assertEqual(a.find(5), node_5)
        self.assertEqual(a.find(4), node_4)
        self.assertEqual(a.find(6), node_6)
        self.assertEqual(a.find(12), node_12)
        self.assertEqual(a.find(14), node_14)
        self.assertEqual(a.find(9), node_9)
        self.assertEqual(a.find(8), node_8)
        self.assertEqual(a.find(11), node_11)
        self.assertEqual(a.find(10), node_10)


 
    def test_delete(self):
        a = RB()
        cases_keys = [5, 4, 12, 7, 14, 6, 9, 8, 11, 10, 15]
        for i in cases_keys:
            a.insert(i)

        """
        7_b: key_color
        (key_kolor): delete node

            7_b_______                        7_b_______                          7_b_______                       7_b_______                    7_b_______                                              
           /          \               1      /          \                 2      /          \             3       /          \            4     /          \              5 
          5_b         _12_b_          ->    5_b         _(12_b)_          ->    5_b         _11_b_        ->     5_b         _11_b_       ->   5_b         _(11_b)_       -> 
         /   \       /      \              /   \       /        \              /   \       /      \             /   \       /      \          /   \       /        \
        4_b   6_b   9_r      14_b         4_b   6_b   9_r        14_b         4_b   6_b  (9_r)     14_b        4_b   6_b   (8_b)    14_b     4_b   6_b   10_b       14_b     
                   /   \       \                     /   \                               /   \                               \
                  8_b   11_b    (15_r)              8_b   11_b                          8_b   10_b                            10_r    
                       /                                 /                                  
                      10_r                              10_r
                      


        5             7_b_______               6        (7_b)_______           7            6_b___           8        _6_b_
        ->           /          \              ->      /            \          ->          /      \          ->      /     \  
                    5_r         (10_b)                5_r            14_b                 5_b     (14_b)            5_b     4_b
                   /   \              \              /   \                               /   
                  4_b   6_b            14_r         4_b   6_b                           4_r
                   
        
        
        
        """
        # 0
        self.assertIsNotNone(a.find(15))

        # 1 del red_node, no childs
        a.delete(15)
        self.assertIsNone(a.find(15))
        test_keys = [4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_12 = root.right
        node_14 = node_12.right
        node_9 = node_12.left
        self.assertIs(a[3], root)
        self.assertIs(a.find(12), node_12)
        self.assertIs(a.find(14), node_14)
        self.assertIs(a.find(9), node_9)

        self.assertIsNotNone(a.find(12))

        # 2 del black_node, this node has a left red baby and black right,
        #replacement with a black right child in the left
        a.delete(12)
        self.assertIsNone(a.find(12))
        test_keys = [4, 5, 6, 7, 8, 9, 10, 11, 14]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_11 = root.right
        node_14 = node_11.right
        node_9 = node_11.left
        self.assertIs(a[3], root)
        self.assertIs(a.find(11), node_11)
        self.assertIs(a.find(14), node_14)
        self.assertIs(a.find(9), node_9)
        self.assertIs(a[7], node_11)
        self.assertEqual(a[7].key, 11)

        self.assertIsNotNone(a.find(9))

        # 3 del red_node, this node has two black children
        a.delete(9)
        self.assertIsNone(a.find(9))
        test_keys = [4, 5, 6, 7, 8, 10, 11, 14]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_11 = root.right
        node_14 = node_11.right
        node_8 = node_11.left
        self.assertIs(a[3], root)
        self.assertIs(a.find(11), node_11)
        self.assertIs(a.find(14), node_14)
        self.assertIs(a.find(8), node_8)
        self.assertIs(a[4], node_8)
        self.assertIsNone(a[4].left.key)
        self.assertEqual(a.find(10), a[4].right)
        
        self.assertIsNotNone(a.find(8))

        # 4 del black_node, this node has right red child
        a.delete(8)
        self.assertIsNone(a.find(8))
        test_keys = [4, 5, 6, 7, 10, 11, 14]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_11 = root.right
        node_14 = node_11.right
        node_10 = node_11.left
        self.assertIs(a[3], root)
        self.assertIs(a.find(11), node_11)
        self.assertIs(a.find(14), node_14)
        self.assertIs(a.find(10), node_10)
        self.assertIs(a[4], node_10)
        self.assertIsNone(a[4].left.key)
        self.assertIsNone(a[4].right.key)

        self.assertIsNotNone(a.find(11))

        # 5 del black_node, this node has two black children
        a.delete(11)
        self.assertIsNone(a.find(11))
        test_keys = [4, 5, 6, 7, 10, 14]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_10 = root.right
        node_14 = node_10.right
        self.assertIs(a[3], root)
        self.assertIs(a.find(10), node_10)
        self.assertIs(a.find(14), node_14)
        self.assertIs(a[4], node_10)
        self.assertIsNone(a[4].left.key)


        self.assertIsNotNone(a.find(10))

        #6
        a.delete(10)
        self.assertIsNone(a.find(10))
        test_keys = [4, 5, 6, 7, 14]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_14 = root.right
        node_5 = root.left
        node_4 = node_5.left
        node_6 = node_5.right
        self.assertIs(a[3], root)
        self.assertIs(a.find(14), node_14)
        self.assertIs(a[4], node_14)
        self.assertIsNone(a[4].left.key)
        self.assertIsNone(a[4].right.key)
        self.assertIs(a.find(4), node_4)
        self.assertIs(a.find(6), node_6)
        
        self.assertIsNotNone(a.find(7))
        self.assertEqual(a.get_root().key, 7)

        # 7 del root
        a.delete(7)
        self.assertIsNone(a.find(7))
        test_keys = [4, 5, 6, 14]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_14 = root.right
        node_5 = root.left
        node_4 = node_5.left
        self.assertIs(a[2], root)
        self.assertIs(a.find(14), node_14)
        self.assertIs(a[3], node_14)
        self.assertIsNone(a[3].left.key)
        self.assertIsNone(a[3].right.key)
        self.assertIs(a.find(5), node_5)
        self.assertIs(a[1], node_5)
        self.assertIsNone(a[1].right.key)
        self.assertIs(a.find(4), node_4)
        self.assertIs(a[0], node_4)
        self.assertIsNone(a[0].left.key)
        self.assertIsNone(a[0].right.key)

        # 8 del black_node, node has not children
        a.delete(14)
        self.assertIsNone(a.find(14))
        test_keys = [4, 5, 6]
        self.assertEqual(a.get_keys_list(), test_keys)
        root = a.get_root()
        node_6 = root.right
        node_4 = root.left
        self.assertIs(a[1], root)
        self.assertIs(a.find(4), node_4)
        self.assertIs(a[0], node_4)
        self.assertIsNone(a[0].left.key)
        self.assertIsNone(a[0].right.key)
        self.assertIs(a.find(6), node_6)
        self.assertIs(a[2], node_6)
        self.assertIsNone(a[2].left.key)
        self.assertIsNone(a[2].right.key)


    def test_color(self):
        """
        test_cases from test_insert(), test_delete()

        True - red
        False - black
        """

        #test_insert_color
        a = RB()
        #0
        a.insert(5)
        self.assertFalse(a.find(5).red)

        #1
        a.insert(4)
        self.assertFalse(a.find(5).red)
        self.assertTrue(a.find(4).red)

        #2
        a.insert(12)
        self.assertFalse(a.find(5).red)
        self.assertTrue(a.find(4).red)
        self.assertTrue(a.find(12).red)

        #3
        a.insert(7)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(12).red)
        self.assertTrue(a.find(7).red)

        #4
        a.insert(14)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(12).red)
        self.assertTrue(a.find(7).red)
        self.assertTrue(a.find(14).red)

        #5
        a.insert(6)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertTrue(a.find(12).red)
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(14).red)
        self.assertTrue(a.find(6).red)

        #6
        a.insert(9)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertTrue(a.find(12).red)
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(14).red)
        self.assertTrue(a.find(6).red)
        self.assertTrue(a.find(9).red)

        #7
        a.insert(8)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertTrue(a.find(5).red)
        self.assertFalse(a.find(7).red)
        self.assertTrue(a.find(12).red)
        self.assertFalse(a.find(9).red)
        self.assertFalse(a.find(14).red)
        self.assertTrue(a.find(8).red)

        #8
        a.insert(11)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertTrue(a.find(5).red)
        self.assertFalse(a.find(7).red)
        self.assertTrue(a.find(12).red)
        self.assertFalse(a.find(9).red)
        self.assertFalse(a.find(14).red)
        self.assertTrue(a.find(8).red)
        self.assertTrue(a.find(11).red)

        #9
        a.insert(10)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(12).red)
        self.assertTrue(a.find(9).red)
        self.assertFalse(a.find(14).red)
        self.assertFalse(a.find(8).red)
        self.assertFalse(a.find(11).red)
        self.assertTrue(a.find(10).red)

        #test_delete_color
        a = RB()
        cases_keys = [5, 4, 12, 7, 14, 6, 9, 8, 11, 10, 15]
        for i in cases_keys:
            a.insert(i)

        #0
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(12).red)
        self.assertFalse(a.find(14).red)
        self.assertTrue(a.find(15).red)
        self.assertTrue(a.find(9).red)
        self.assertFalse(a.find(8).red)
        self.assertFalse(a.find(11).red)
        self.assertTrue(a.find(10).red)

        #1
        a.delete(15)
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(12).red)
        self.assertFalse(a.find(14).red)
        self.assertTrue(a.find(9).red)
        self.assertFalse(a.find(8).red)
        self.assertFalse(a.find(11).red)
        self.assertTrue(a.find(10).red)

        #2
        a.delete(12)
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(14).red)
        self.assertTrue(a.find(9).red)
        self.assertFalse(a.find(8).red)
        self.assertFalse(a.find(11).red)
        self.assertFalse(a.find(10).red)

        #3
        a.delete(9)
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(14).red)
        self.assertFalse(a.find(8).red)
        self.assertFalse(a.find(11).red)
        self.assertTrue(a.find(10).red)

        #4
        a.delete(8)
        self.assertFalse(a.find(7).red)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(14).red)
        self.assertFalse(a.find(11).red)
        self.assertFalse(a.find(10).red)

        #5
        a.delete(11)
        self.assertFalse(a.find(7).red)
        self.assertTrue(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertTrue(a.find(14).red)
        self.assertFalse(a.find(10).red)

        #6
        a.delete(10)
        self.assertFalse(a.find(7).red)
        self.assertTrue(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(14).red)

        #6
        a.delete(7)
        self.assertFalse(a.find(5).red)
        self.assertTrue(a.find(4).red)
        self.assertFalse(a.find(6).red)
        self.assertFalse(a.find(14).red)

        #7
        a.delete(14)
        self.assertFalse(a.find(5).red)
        self.assertFalse(a.find(4).red)
        self.assertFalse(a.find(6).red)


    def test_set_value(self):
        a = RB()
        a.insert(5)
        self.assertEqual(a.find(5).val, None)
        a.insert(6, 8)
        self.assertEqual(a.find(6).val, 8)
        a.set_value(5, 4)
        a.set_value(6, 9)
        self.assertEqual(a.find(5).val, 4)
        self.assertEqual(a.find(6).val, 9)



if __name__ == "__main__":
    unittest.main()