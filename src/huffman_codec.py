import pickle
from hc_exceptions import HCEncodeTreeReadError
from huffman_algorithm import HuffmanAlgorithm


class HuffmanCodec:
    """ 1 Encode() :
            - add huffman_tree at the beginning of output file
            - write encoded buffer to output file
        2 Decode() :
            -  read huffman tree from the beginning of encoded input file and init algorithm
            -  decode the rest of input file and write to out file
    """

    def __init__(self, buffer_size=1024):
        self.buf_size = buffer_size

    def encode(self, f_input, f_encoded):
        self.ha = HuffmanAlgorithm()
        f_input_lenght = 0
        # build char frequencies list by update_freq()
        while True:
            buff = f_input.read(self.buf_size)
            f_input_lenght += len(buff)
            if buff:
                self.ha.update_freq(buff)
            else:
                break
        # make all neccessary preparations by prepare_encoding_alg() as soon as frequency list is build
        self.ha.prepare_encoding_alg()
        # store encoding dictionary at the beginning of output file for future decoding
        f_encoded.write(pickle.dumps((self.ha.node, f_input_lenght)))

        # encode and store to output file the input file by BUF_SIZE lenght parts
        f_input.seek(0, 0)
        while True:
            buff = f_input.read(self.buf_size)
            if buff:
                f_encoded.write(self.ha.encode_buff(buff))
            else:
                break
        if self.ha.last_bits:
            f_encoded.write(self.ha.last_byte())

        f_encoded.flush()

    def decode(self, f_encoded, f_decoded):
        self.ha = HuffmanAlgorithm()
        try:
            tree_and_lenght = pickle.load(f_encoded)
        except Exception as e:
            raise HCEncodeTreeReadError() from e

        self.ha.node = tree_and_lenght[0]

        while True:
            buff = f_encoded.read(self.buf_size)
            if buff:
                f_decoded.write(self.ha.decode_buff(buff, tree_and_lenght[1]))
            else:
                break

        f_decoded.flush()
