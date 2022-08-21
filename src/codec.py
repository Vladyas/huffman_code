from huffman_codec import HuffmanCodec


class Codec():
    def __init__(self):
        self.buffer_size = 1024

    def encode(self, name_in_file, name_encoded_file):
        with open(name_in_file, 'r', encoding='utf-8') as f_input:
            with open(name_encoded_file, 'wb') as f_encoded:
                HuffmanCodec(self.buffer_size).encode(f_input, f_encoded)
                return True

    def decode(self, name_encoded_file, name_decoded_file):
        with open(name_encoded_file, 'rb') as f_encoded:
            with open(name_decoded_file, 'w', encoding='utf-8') as f_decoded:
                HuffmanCodec(self.buffer_size).decode(f_encoded, f_decoded)
                return True
