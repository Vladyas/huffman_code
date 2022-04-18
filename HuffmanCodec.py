from HuffmanAlgorithm import HuffmanAlgorithm


class HuffmanCodec:

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

        while True:
            buff = f_input.read(self.buf_size)
            if buff == b'':
                break
            else:
                f_encoded.write(self.ha.encode_buff(buff))

        f_encoded.flush()

    def decode(self, f_encoded, f_decoded):
        while True:
            buff = f_encoded.read(self.buf_size)
            if buff == b'':
                break
            else:
                f_decoded.write(self.ha.decode_buff(buff))


if __name__ == '__main__':

    hc = HuffmanCodec()
