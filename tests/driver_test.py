"""
The test checks that source file is identical with the encoded_decoded result file
The input files are in the project directory: War_and_Peace.txt in Russian
and chinese.txt in Cinese with short English prephase
"""
import filecmp


def test_source_decode_compare(file_names):
    """
    The test checks that source file is identical with the encoded_decoded result file
    """
    assert filecmp.cmp(file_names[0], file_names[1], shallow=False)
