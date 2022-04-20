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
        self.ha = HuffmanAlgorithm()
        self.buf_size = buffer_size

    def encode(self, f_input, f_encoded):
        f_input.seek(0, 0)
        while True:
            buff = f_input.read(self.buf_size)
            if buff == b'':
                break
            else:
                self.ha.update_freq(buff)

        f_input.seek(0, 0)

        self.ha.prepare_alg()
        pickle.dump(self.ha.huffman_tree, f_encoded)

        while True:
            buff = f_input.read(self.buf_size)
            if buff == b'':
                break
            else:
                f_encoded.write(self.ha.encode_buff(buff).encode())

        f_encoded.flush()

    def decode(self, f_encoded, f_decoded):

        self.ha.huffman_tree = pickle.load(f_encoded)

        while True:
            buff = f_encoded.read(self.buf_size)
            if buff == b'':
                break
            else:
                f_decoded.write(self.ha.decode_buff(buff))

