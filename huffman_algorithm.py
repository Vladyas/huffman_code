from huffman_tree import HuffmanTree


class HuffmanAlgorithm:

    def __init__(self):
        self.freq = {}
        self.encode = {}
        self.huffman_tree = HuffmanTree()
        self.ready = False
        self.temp_node = None

    def update_freq(self, buff_in):
        for i in buff_in:
            if i in self.freq.keys():
                self.freq[i] += 1
            else: self.freq[i] = 1

    def build_encode_list(self):

        def create_encode_list(node=None, char_code=''):
            if node.left is None:
                self.encode[node.symbol] = char_code
                return True
            else:
                create_encode_list(node.left, char_code + '0')
                create_encode_list(node.right, char_code + '1')

        create_encode_list(self.huffman_tree.node_list[0])

    def prepare_alg(self):
        if not self.ready:
            self.huffman_tree.build_tree(self.freq)
            self.build_encode_list()
            self.ready = True


    def encode_buff(self, buff_in):
        self.prepare_alg()
        encoded_buff, bytes_buff = '', b''
        for i in buff_in:
            encoded_buff += self.encode[i]

        self.huffman_tree.lengh = len(encoded_buff)

        for i in range(0, len(encoded_buff), 8):
            bytes_buff +=int((encoded_buff[i:i+8]+'0'*8)[:8], 2).to_bytes(1, 'big')

        return bytes_buff

    def decode_buff(self, buff_in_comp):
        buff_decoded = ''
        buff_in = ''
        for i in buff_in_comp:
            buff_in +=format(i, '0>8b')
        buff_in = buff_in[:self.huffman_tree.lengh]

        if self.temp_node is None:
            self.temp_node = self.huffman_tree.node_list[0]
        for i in buff_in:
            if self.temp_node.left is None:
                buff_decoded += self.temp_node.symbol
                self.temp_node = self.huffman_tree.node_list[0]
            if i == '0':
                self.temp_node = self.temp_node.left
            elif i == '1':
                self.temp_node = self.temp_node.right
        buff_decoded += self.temp_node.symbol
        return buff_decoded



