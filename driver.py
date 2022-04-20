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

    if len(sys.argv) == 3:
        if sys.argv[1] not in ('-e', '-d'):
            print("wrong mode value(-e or -d are allowed)")
            sys.exit()

        name_in_file = sys.argv[2]
        name_start = name_in_file.partition('.')[0]
        name_extension = name_in_file.partition('.')[2]
        name_encoded_file = name_start + '_e' + '.' + name_extension
        name_decoded_file = name_start + '_d' + '.' + name_extension
        name_deb_file = name_start + '_debug' + '.' + name_extension
    else:
        print("It must be 2 parameters passed: mode value(-e or -d) and file name")
        sys.exit()

    hc = HuffmanCodec()

    if sys.argv[1] == '-e':
        with open(name_in_file, 'rb') as f_input:
            with open(name_encoded_file, 'wb') as f_encoded:
                hc.encode(f_input, f_encoded)

    elif sys.argv[1] == '-d':
        with open(name_in_file, 'rb') as f_encoded:
            with open(name_decoded_file, 'wb') as f_decoded:
                hc.decode(f_encoded, f_decoded)

    # check_res(name_in_file, name_decoded_file)
