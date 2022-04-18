import heapq


class HuffmanTree:

    def __init__(self):
        self.freq_list = []
        self.node_list = []

    class Node:
        freq = 0
        code = 256
        left = None
        right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def build_tree(self, freq_list):
        self.freq_list = freq_list
        for i in range(0, 256):
            if self.freq_list[i] != 0:
                n = self.Node()
                n.freq = self.freq_list[i]
                n.code = i
                heapq.heappush(self.node_list, n)

        while len(self.node_list) > 1:
            tmp_heap = []
            while len(self.node_list) > 1:
                right_node = heapq.heappop(self.node_list)
                left_node = heapq.heappop(self.node_list)
                parent_node = self.Node()
                parent_node.freq = left_node.freq + right_node.freq
                parent_node.left = left_node
                parent_node.right = right_node
                tmp_heap.append(parent_node)

            for i in range(0, len(tmp_heap)):
                heapq.heappush(self.node_list, tmp_heap[i])


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
    pass
