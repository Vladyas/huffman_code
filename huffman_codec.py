from huffman_algorithm import HuffmanAlgorithm
import pickle

class HuffmanCodec:
    ''' Encode or decode buffer and write to destination file'''

    def __init__(self):
        self.ha = HuffmanAlgorithm()
        self.buf_size = 1024

    def encode(self, f_input, f_encoded):
        f_input.seek(0, 0)
        while True:
            buff = f_input.read(self.buf_size)
            if buff == b'':
                break
            else:
                self.ha.update_freq(buff)

        f_input.seek(0, 0)

        with open('treedump', 'wb') as f:
            self.ha.prepare_alg()
            pickle.dump(self.ha.huffman_tree, f)

        while True:
            buff = f_input.read(self.buf_size)
            if buff == b'':
                break
            else:
                f_encoded.write(self.ha.encode_buff(buff))

        f_encoded.flush()

    def decode(self, f_encoded, f_decoded):

        with open('treedump', 'rb') as f:
            self.ha.huffman_tree = pickle.load(f)

        while True:
            buff = f_encoded.read(self.buf_size)
            if buff == b'':
                break
            else:
                f_decoded.write(self.ha.decode_buff(buff))


if __name__ == '__main__':

    hc = HuffmanCodec()
