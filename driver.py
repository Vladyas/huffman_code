import sys
from huffman_codec import HuffmanCodec


def main():
    BUFFER_SIZE = 1024
    if len(sys.argv) == 3 and sys.argv[1] in ('-e', '-d'):

        name_in_file = sys.argv[2]
        name_start = name_in_file.partition('.')[0]
        name_extension = name_in_file.partition('.')[2]
        name_encoded_file = name_start + '_e' + '.' + name_extension
        name_decoded_file = name_start + '_d' + '.' + name_extension

    else:
        print("2 parameters should be passed: mode (-e  or -d) and 'file name'")
        sys.exit()

    hc = HuffmanCodec(BUFFER_SIZE)

    if sys.argv[1] == '-e':
        with open(name_in_file, 'r', encoding='utf-8') as f_input:
        # with open(name_in_file, 'r', encoding='iso-8859-1') as f_input:
            with open(name_encoded_file, 'wb') as f_encoded:
                hc.encode(f_input, f_encoded)

    elif sys.argv[1] == '-d':
        with open(name_in_file, 'rb') as f_encoded:
            with open(name_decoded_file, 'w', encoding='utf-8') as f_decoded:
            # with open(name_decoded_file, 'w', encoding='iso-8859-1') as f_decoded:
                hc.decode(f_encoded, f_decoded)


if __name__ == '__main__':
    main()
