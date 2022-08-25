import pytest
from huffman_codec import HuffmanCodec
from hc_exceptions import HCEncodeTreeReadError

"""
Unit tests for huffman_codec.py and huffman_algorithm.py.
The tests check huffman encoding dictionary and symbols frequency dictionary, which are used by the algorithm
"""


def test_huffman_dict(get_encode_freqs_dicts):
    """
    Tests encoding dictionary.
    # correct dict is build basing on https://www.studytonight.com/data-structures/huffman-coding
    # it seems incorrect dict is build basing on https://www.csfieldguide.org.nz/en/interactives/huffman-tree/
    """
    assert get_encode_freqs_dicts['test_encode'] == get_encode_freqs_dicts['correct_encode']


def test_sym_freqs(get_encode_freqs_dicts):
    """
    Tests symbols frequency dictionary.
    # correct frequencies dict is build basing on https://www.studytonight.com/data-structures/huffman-coding
    """
    assert get_encode_freqs_dicts['test_freq'] == get_encode_freqs_dicts['correct_freq']


def test_pickle_load_error():
    """Checks HCEncodeTreeReadError() exception is raised if source file for decoding
    has no encoded tree and pickle.load exception occurs"""

    with open('War_and_Peace.txt', 'r') as f_source:
        with open('War_and_Peace_e_d.txt', 'wb') as f_destination:
            with pytest.raises(HCEncodeTreeReadError):
                HuffmanCodec().decode(f_source, f_destination)
