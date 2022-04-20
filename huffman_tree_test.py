import pytest
from huffman_tree import HuffmanTree

if __name__ == '__main__':
    t = HuffmanTree()
    t_freq = [3, 3, 2, 2, 1]
    t_freq += [0]*(256-len(t_freq))
    t.build_tree(t_freq)

    def test_tree(root):
        if root.left is not None:
            if root.left.freq < root.right.freq:
                print('wrong list orders')
            else:
                test_tree(root.left)
                test_tree(root.right)
        else:
            return
    print('Check frequency in the tree...')
    test_tree(t.node_list[0])
    print("Check frequency in the tree is finished. It is OKAY if you haven't see '<wrong list orders>' message")