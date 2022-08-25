import argparse
import os
from codec import Codec
from hc_exceptions import HCEncodeTreeReadError


def parse_args(PARAM_ENCODE, PARAM_DECODE):
    parser = argparse.ArgumentParser(description='Encode and Decode files with Huffman codding.')
    parser.add_argument('command', choices=[PARAM_ENCODE, PARAM_DECODE], help='e for encoding, d for decoding. ')
    parser.add_argument('sourcefile', type=str, help='File for encoding or decoding.')

    return parser.parse_args()


def main():
    PARAM_ENCODE = 'e'
    PARAM_DECODE = 'd'
    MSG_FILEIOERROR = "The source file does not exist or empty."

    args = parse_args(PARAM_ENCODE, PARAM_DECODE)

    name_start, file_extension = os.path.splitext(args.sourcefile)

    if args.command == PARAM_ENCODE:
        if os.path.isfile(args.sourcefile) and os.path.getsize(args.sourcefile) > 0:
            output_file = '{}_{}{}'.format(name_start, PARAM_ENCODE, file_extension)
            Codec().encode(args.sourcefile, output_file)
        else:
            print(MSG_FILEIOERROR)
    elif args.command == PARAM_DECODE:
        if os.path.isfile(args.sourcefile) and os.path.getsize(args.sourcefile) > 0:
            output_file = '{}_{}{}'.format(name_start, PARAM_DECODE, file_extension)
            try:
                Codec().decode(args.sourcefile, output_file)
            except HCEncodeTreeReadError:
                print('The source file {} could not be decoded as it was not encoded by this codec.'.format(args.sourcefile))
        else:
            print(MSG_FILEIOERROR)


if __name__ == '__main__':
    main()
