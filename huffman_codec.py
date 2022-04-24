import pickle
from huffman_algorithm import HuffmanAlgorithm


class HuffmanCodec:
    ''' 1 Encode() :
            - add huffman_tree at the beginning of output file
            - write encoded buffer to output file
        2 Decode() :
            -  read huffmun tree from the beginning of encoded input file and init algorithm
            -  decode the rest of input file and write to out file
        '''

    def __init__(self, buffer_size=1024):
        self.buf_size = buffer_size

    def encode(self, f_input, f_encoded):
        self.ha = HuffmanAlgorithm()

        f_input_lenght = 0
        while True:
            buff = f_input.read(self.buf_size)
            f_input_lenght += len(buff)
            if buff == '':
                break
            else:
                self.ha.update_freq(buff)
        self.ha.prepare_encoding_alg()
        pickle.dump((self.ha.huffman_tree, f_input_lenght), f_encoded)

        f_input.seek(0, 0)
        while True:
            buff = f_input.read(self.buf_size)
            if buff == '':
                break
            else:
                f_encoded.write(self.ha.encode_buff(buff))
        if self.ha.last_bits:
            f_encoded.write(self.ha.last_byte())

        f_encoded.flush()

    def decode(self, f_encoded, f_decoded):
        self.ha = HuffmanAlgorithm()

        tree_and_lenght = pickle.load(f_encoded)
        self.ha.huffman_tree = tree_and_lenght[0]

        while True:
            buff = f_encoded.read(self.buf_size)
            if buff == b'':
                break
            else:
                f_decoded.write(self.ha.decode_buff(buff, tree_and_lenght[1]))
        f_decoded.flush()
