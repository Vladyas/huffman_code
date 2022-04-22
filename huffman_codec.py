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
        while True:
            buff = f_input.read(self.buf_size)
            if buff == '':
                break
            else:
                self.ha.update_freq(buff)

        f_input.seek(0, 0)

        self.ha.prepare_alg()
        buff = f_input.read()
        encoded_buff_and_lenght = self.ha.encode_buff(buff)

        pickle.dump((self.ha.huffman_tree, encoded_buff_and_lenght[1]), f_encoded)
        f_encoded.write(encoded_buff_and_lenght[0])
        # while True:
        #     buff = f_input.read(self.buf_size)
        #     if buff == '':
        #         break
        #     else:
        #         tmp = self.ha.encode_buff(buff)
        #         f_encoded.write(tmp)

        f_encoded.flush()

    def decode(self, f_encoded, f_decoded):
        tree_and_lenght = pickle.load(f_encoded)
        self.ha.huffman_tree = tree_and_lenght[0]

        buff = f_encoded.read()
        decoded_buff = self.ha.decode_buff(buff, tree_and_lenght[1])
        f_decoded.write(decoded_buff)
        # while True:
        #     buff = f_encoded.read(self.buf_size)
        #     if buff == b'':
        #         break
        #     else:
        #         f_decoded.write(self.ha.decode_buff(buff))

