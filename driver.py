# extract input file name from received arguments
# call HuffmanCodec to build encoded and decoded files
# compare input and decoded files byte-to-byte and print final message are the files identical
import sys
from huffman_codec import HuffmanCodec

def check_res(name_in_file, name_decoded_file):
    with open(name_in_file, 'rb') as f_input:
        with open(name_decoded_file, 'rb') as f_decoded:
            while True:
                c1 = f_input.read(1)
                c2 = f_decoded.read(1)
                if c1 != c2:
                    print('ERROR:Input and decoded files are not identical!')
                    sys.exit()
                if c1 == b'':
                    print(f'{f_input.name} and {f_decoded.name} are identical!')
                    break

if __name__ == '__main__':

    if len(sys.argv) > 1:
        name_in_file = sys.argv[1]
        name_start = name_in_file.partition('.')[0]
        name_extension = name_in_file.partition('.')[2]
        name_encoded_file = name_start + '_encoded' + '.' + name_extension
        name_decoded_file = name_start + '_decoded' + '.' + name_extension
        name_deb_file = name_start + '_debug' + '.' + name_extension
    else:
        print("No input file name passed in parameters")
        sys.exit()

    hc = HuffmanCodec()

    with open(name_in_file, 'rb') as f_input:
        with open(name_encoded_file, 'w') as f_encoded:
            hc.encode(f_input, f_encoded)

    with open(name_encoded_file, 'rb') as f_encoded:
        with open(name_decoded_file, 'wb') as f_decoded:
            hc.decode(f_encoded, f_decoded)

    check_res(name_in_file, name_decoded_file)