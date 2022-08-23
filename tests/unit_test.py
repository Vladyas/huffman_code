# @pytest.mark.skip('My dictionary does not match to online calculator ones')
def test_huffman_dict(get_encode_freqs_dicts):
    # correct dict is build basing on https://www.studytonight.com/data-structures/huffman-coding
    assert get_encode_freqs_dicts['test_encode'] == get_encode_freqs_dicts['correct_encode']

   # {'i': '00', 's': '01', 'e': '10', 'u': '1100', 't': '11010', 'o': '11011',
   #                               'a': '111'}


def test_sym_freqs(get_encode_freqs_dicts):
    # correct frequencies dict is build basing on https://www.studytonight.com/data-structures/huffman-coding
    assert get_encode_freqs_dicts['test_freq'] == get_encode_freqs_dicts['correct_freq']

#     {'a': 10, 'e': 15, 'i': 12, 'o': 3, 'u': 4, 's': 13, 't': 1}
