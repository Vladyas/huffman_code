import heapq


class Node:
    freq = 0
    symbol = None
    left = None
    right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanAlgorithm:
    def __init__(self):

        self.node = None
        self.freq = {}
        self.encode = {}
        self.last_bits = ''
        self.temp_node = None
        self.decoded_lenght = 0

    def _build_tree(self, freqs):
        node_list = []
        for i in freqs:
            n = Node()
            n.freq = freqs[i]
            n.symbol = i
            heapq.heappush(node_list, n)

        while len(node_list) > 1:
            parent_node = Node()
            parent_node.left = heapq.heappop(node_list)
            parent_node.right = heapq.heappop(node_list)
            parent_node.freq = parent_node.left.freq + parent_node.right.freq
            heapq.heappush(node_list, parent_node)

        self.node = node_list[0]

    def _build_encode_list(self, node=None, char_code=''):

        if node.left is None:
            self.encode[node.symbol] = char_code
            return
        else:
            self._build_encode_list(node.left, char_code + '0')
            self._build_encode_list(node.right, char_code + '1')

    def update_freq(self, buff_in):
        for i in buff_in:
            if i in self.freq.keys():
                self.freq[i] += 1
            else:
                self.freq[i] = 1

    def prepare_encoding_alg(self):
        self._build_tree(self.freq)
        self._build_encode_list(self.node)
        self.last_bits = ''

    def last_byte(self):
        # prepare the last byte of the encoded file
        return int((self.last_bits + '0' * 8)[:8], 2).to_bytes(1, 'big')

    def encode_buff(self, buff_in):
        encoded_buff, bytes_buff = self.last_bits, b''
        for i in buff_in:
            encoded_buff += self.encode[i]

        tmp = len(encoded_buff)
        if tmp % 8:
            self.last_bits = encoded_buff[tmp - tmp % 8:]
            encoded_buff = encoded_buff[:tmp - tmp % 8]
        else:
            self.last_bits = ''

        for i in range(0, len(encoded_buff), 8):
            bytes_buff += int((encoded_buff[i:i + 8] + '0' * 8)[:8], 2).to_bytes(1, 'big')

        return bytes_buff

    def decode_buff(self, buff_encoded, result_lenght):
        def add_decoded_sym():
            nonlocal buff_decoded
            buff_decoded += self.temp_node.symbol
            self.decoded_lenght += 1
            self.temp_node = self.node

        buff_decoded, buff_in = '', ''

        for i in buff_encoded:
            buff_in += format(i, '0>8b')

        if self.temp_node is None:
            self.temp_node = self.node

        for i in buff_in:
            if self.temp_node.left is None:
                add_decoded_sym()
                if self.decoded_lenght == result_lenght:
                    return buff_decoded
            if i == '0':
                self.temp_node = self.temp_node.left
            elif i == '1':
                self.temp_node = self.temp_node.right
        else:
            if self.temp_node.left is None:
                add_decoded_sym()

        return buff_decoded
