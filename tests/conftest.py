import os
import pytest, sys
from src import driver
# from src import huffman_codec
from huffman_codec import HuffmanCodec, HuffmanAlgorithm

# unnit_test  fixtures params
# codding to test is got from https://www.csfieldguide.org.nz/en/interactives/huffman-tree/
inputs_encodes_freqs = [
    ('aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst',
     {'i': '00', 's': '01', 'e': '10', 'u': '1100', 't': '11010', 'o': '11011', 'a': '111'},
     {'a': 10, 'e': 15, 'i': 12, 'o': 3, 'u': 4, 's': 13, 't': 1}),
    ('Привет кодировщик Хаффмана!!',
     {'и': '001', 'м': '0000', 'н': '0001', 'а': '010', 'р': '0110', 'в': '0111', ' ': '1000', 'к': '1001', 'о': '1010',
      'ф': '1011', '!': '1100', 'П': '11010', 'е': '11011', 'т': '11100', 'д': '11101', 'щ': '11110', 'Х': '11111'},
     {'и': 3, 'м': 1, 'н': 1, 'а': 3, 'р': 2, 'в': 2, ' ': 2, 'к': 2, 'о': 2,
      'ф': 2, '!': 2, 'П': 1, 'е': 1, 'т': 1, 'д': 1, 'щ': 1, 'Х': 1}
     )
]


@pytest.fixture(params=inputs_encodes_freqs)
def get_encode_freqs_dicts(request):
    """
    Fixture for test_unit_huffman_codec.py tests
    :param request: tuple as (string to encode, correct encode dict, correct frequency dict)
    :return: tuple as (calculated encode dict, calculated frequency dict, correct encode dict, correct frequency dict)
    """
    TMP_FILE = 'tmp.txt'
    with open(TMP_FILE, 'w') as f:
        f.write(request.param[0])

    # https: // www.csfieldguide.org.nz / en / interactives / huffman - tree /
    hc = HuffmanCodec()
    hc.ha = HuffmanAlgorithm()
    f_input_lenght = 0
    with open(TMP_FILE, 'r', encoding='utf-8') as f_input:
        while True:
            buff = f_input.read(hc.buf_size)
            f_input_lenght += len(buff)
            if buff:
                hc.ha.update_freq(buff)
            else:
                break

    hc.ha.prepare_encoding_alg()
    yield {'test_encode': hc.ha.encode, 'test_freq': hc.ha.freq,
           'correct_encode': request.param[1], 'correct_freq': request.param[2]}

    os.remove(TMP_FILE)


# driver_test  fixtures consts
PARAM_ENCODE = 'e'
PARAM_DECODE = 'd'

books = [('War_and_Peace.txt', 'War_and_Peace_e.txt', 'War_and_Peace_e_d.txt'),
         ('chinese.txt', 'chinese_e.txt', 'chinese_e_d.txt')
         ]

@pytest.fixture()
def prepare_sys_argv():
    """ workaround to avoid argparse conflict when pytest is run with parameters """
    test_path = sys.argv[0]
    sys.argv.clear()
    sys.argv.extend([test_path])


@pytest.fixture(params=books)
def file_names(request, prepare_sys_argv):
    """
    The fixture for test_driver.py calls tested driver.py for encoding and decoding
    :param request: tuple as (source file name, encoded file name, decoded file name)
    :param prepare_sys_argv is used for command line arguments processing
    :return: tuple as (source file name, decoded file name)
    """
    file_source, file_encoded, file_decoded = request.param
    sys.argv.extend([PARAM_ENCODE, file_source])
    # encode test file
    driver.main()
    sys.argv[1] = PARAM_DECODE
    sys.argv[2] = file_encoded
    # decode test file
    driver.main()

    yield (file_source, file_decoded)
