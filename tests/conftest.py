import pytest, sys
from src import driver
from src import huffman_codec
from huffman_codec import HuffmanCodec, HuffmanAlgorithm

# driver_test  fixtures consts
PARAM_ENCODE = 'e'
PARAM_DECODE = 'd'

books = [('War_and_Peace.txt', 'War_and_Peace_e.txt', 'War_and_Peace_e_d.txt'),
         ('chinese.txt', 'chinese_e.txt', 'chinese_e_d.txt')]



def _prepare_huffman_algorithm():
    # https: // www.csfieldguide.org.nz / en / interactives / huffman - tree /
    hc = HuffmanCodec()
    hc.ha = HuffmanAlgorithm()
    f_input_lenght = 0
    with open('1.txt', 'r', encoding='utf-8') as f_input:
        while True:
            buff = f_input.read(hc.buf_size)
            f_input_lenght += len(buff)
            if buff:
                hc.ha.update_freq(buff)
            else:
                break

    hc.ha.prepare_encoding_alg()
    return hc.ha.encode, hc.ha.freq


@pytest.fixture()
def get_encode_freqs_dicts():
    yield _prepare_huffman_algorithm()


@pytest.fixture(params=books)
def file_names(request):
    file_source, file_encoded, file_decoded = request.param
    ### workaround to avoid argparse conflict when pytest is run with parameters
    test_path = sys.argv[0]
    sys.argv.clear()
    sys.argv.extend([test_path, PARAM_ENCODE, file_source])
    ###
    # encode test file
    driver.main()
    sys.argv[1] = PARAM_DECODE
    sys.argv[2] = file_encoded
    # decode test file
    driver.main()

    yield (file_source, file_decoded)
