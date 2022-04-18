import heapq
import sys

if len(sys.argv) > 1:
    name_In_File = sys.argv[1]
    name_start = name_In_File.partition('_in.')[0]
    name_extension = name_In_File.partition('_in.')[2]
    name_encoded_file = name_start + '_encoded' + '.' + name_extension
    name_decoded_file = name_start + '_decoded' + '.' + name_extension
    name_deb_file = name_start + '_debug' + '.' + name_extension

else:
    print("No input file name passed in parameters")
    sys.exit()


class Node:
    freq = 0
    code = 256
    left = None
    right = None

    def __lt__(self, other):
        return self.freq < other.freq


# initializing freq, encode lists
freq = [0 for _ in range(0, 256)]
encode = ['' for _ in range(0, 256)]

# read test input file for encoding
with open(name_In_File, 'rb') as f_input:
    byte = f_input.read(1)

    if byte == b'':
        print('Input file is empty. The program is terminated.')
        sys.exit(False)
    #  make frequency list
    while byte != b'':
        freq[byte[0]] += 1
        byte = f_input.read(1)

# huffman tree
h = []
#  prepare nodes list for heapq
for i in range(0, 256):
    if freq[i] != 0:
        n = Node()
        n.freq = freq[i]
        n.code = i
        heapq.heappush(h, n)
#  build hyffman tree
while len(h) > 1:
    tmp_heap = []
    while len(h) > 1:
        right_node = heapq.heappop(h)
        left_node = heapq.heappop(h)
        parent_node = Node()
        parent_node.freq = left_node.freq + right_node.freq
        parent_node.left = left_node
        parent_node.right = right_node
        tmp_heap.append(parent_node)

    for i in range(0, len(tmp_heap)):
        heapq.heappush(h, tmp_heap[i])


# create encode list
def create_encode_list(node=None, char_code=''):
    # if node.left is None:

    if node.code != 256:
        # char_code += '0'
        # encode[node.code] = int(charcode, 2)
        encode[node.code] = char_code
        return True
    else:
        create_encode_list(node.left, char_code + '0')
        create_encode_list(node.right, char_code + '1')


create_encode_list(h[0])

# create encoded file
with open(name_In_File, 'rb') as f_input:
    with open(name_encoded_file, 'w') as f_encoded:
        byte = f_input.read(1)
        while byte != b'':
            f_encoded.write(encode[byte[0]])
            byte = f_input.read(1)

# create decoded file
with open(name_encoded_file, 'rb') as f_encoded:
    with open(name_decoded_file, 'wb') as f_decoded:
        tmp_node = h[0]
        while True:
            if tmp_node.left is not None:
                byte = f_encoded.read(1)
                if byte == b'':
                    break
                if byte == b'0':
                    tmp_node = tmp_node.left
                elif byte == b'1':
                    tmp_node = tmp_node.right
            else:
                f_decoded.write(tmp_node.code.to_bytes(1, byteorder='big'))
                tmp_node = h[0]

# create debug file with encode list
with open(name_deb_file, 'wb') as f_debug:
    for i in range(0, len(encode)):
        if encode[i] != "":
            if i < 32 or i > 127:
                # sym = hex(i)
                sym = chr(i)
            else:
                sym = chr(i)

            sym += ':' + encode[i] + '\n'
            f_debug.write(bytes(sym, encoding='utf-8'))
