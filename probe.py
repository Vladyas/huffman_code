import argparse


def main():
    parser = argparse.ArgumentParser(description='Encode and Decode files with Huffman codding.')
    parser.add_argument('command', choices=['e', 'd'], help='e for encoding, d for decoding. ')
    parser.add_argument('sourcefile', type = str, help='File for encoding or decoding.')
    try:
        args = parser.parse_args()
        print(args)
    except :
        print('ПОЙМАЛ!')

if __name__ == '__main__':
    main()
