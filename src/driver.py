import sys, argparse, os
from codec import Codec


def parse_args(PARAM_ENCODE, PARAM_DECODE):
    parser = argparse.ArgumentParser(description='Encode and Decode files with Huffman codding.')
    parser.add_argument('command', choices=[PARAM_ENCODE, PARAM_DECODE], help='e for encoding, d for decoding. ')
    parser.add_argument('sourcefile', type=str, help='File for encoding or decoding.')

    return parser.parse_args()


def main():
    PARAM_ENCODE = 'e'
    PARAM_DECODE = 'd'

    args = parse_args(PARAM_ENCODE, PARAM_DECODE)

    name_start, file_extension = os.path.splitext(args.sourcefile)

    if args.command == PARAM_ENCODE:
        output_file = '{}_{}{}'.format(name_start, PARAM_ENCODE, file_extension)
        Codec().encode(args.sourcefile, output_file)
    elif args.command == PARAM_DECODE:
        output_file = '{}_{}{}'.format(name_start, PARAM_DECODE, file_extension)
        Codec().decode(args.sourcefile, output_file)


if __name__ == '__main__':
    main()
