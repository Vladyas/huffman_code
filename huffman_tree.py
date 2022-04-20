import heapq


class HuffmanTree:

    def __init__(self):
        self.node_list = []

    class Node:
        freq = 0
        symbol = None
        left = None
        right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def build_tree(self, freqs):
        for i in freqs:
            n = self.Node()
            n.freq = freqs[i]
            n.symbol = i
            heapq.heappush(self.node_list, n)

        while len(self.node_list) > 1:
            parent_node = self.Node()
            parent_node.right = heapq.heappop(self.node_list)
            parent_node.left = heapq.heappop(self.node_list)
            parent_node.freq = parent_node.left.freq + parent_node.right.freq
            heapq.heappush(self.node_list, parent_node)


