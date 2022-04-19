from huffman_tree import HuffmanTree


class HuffmanAlgorithm:

    def __init__(self):
        self.freq = [0] * 256
        self.encode = [''] * 256
        self.huffman_tree = HuffmanTree()
        self.ready = False
        self.temp_node = None

    def update_freq(self, buff_in):
        for i in buff_in:
            self.freq[i] += 1

    def build_encode_list(self):

        def create_encode_list(node=None, char_code=''):
            if node.left is None:
                self.encode[node.code] = char_code
                return True
            else:
                create_encode_list(node.left, char_code + '0')
                create_encode_list(node.right, char_code + '1')

        create_encode_list(self.huffman_tree.node_list[0])

    def encode_buff(self, buff_in):
        if not self.ready:
            self.huffman_tree.build_tree(self.freq)
            self.build_encode_list()
            self.ready = True
        encoded_buff = ''
        for i in buff_in:
            encoded_buff += self.encode[i]

        return encoded_buff

    def decode_buff(self, buff_in):
        buff_decoded = b''
        if self.temp_node is None:
            self.temp_node = self.huffman_tree.node_list[0]
        for i in buff_in:
            if self.temp_node.left is None:
                buff_decoded += self.temp_node.code.to_bytes(1, byteorder='big')
                self.temp_node = self.huffman_tree.node_list[0]
            if i == ord(b'0'):
                self.temp_node = self.temp_node.left
            elif i == ord(b'1'):
                self.temp_node = self.temp_node.right
        if self.temp_node.left is None:
            buff_decoded += self.temp_node.code.to_bytes(1, byteorder='big')
            self.temp_node = self.huffman_tree.node_list[0]
        return buff_decoded


if __name__ == "__main__":
    buff = b'aaaabbcdefg'
    ha = HuffmanAlgorithm()
    ha.update_freq(buff)
    buff_enc = ha.encode_buff(buff)
    print('Encoded buff:', buff_enc)
    buff_dec = ha.decode_buff(buff_enc.encode('utf-8'))
    print('String to encode/decode:', buff)
    print('Decoded buff:', buff_dec)
