"""
The test checks that source file is identical with the encoded_decoded result file
The input files are in the project directory: War_and_Peace.txt in Russian
and chinese.txt in Cinese with short English prephase
"""
import pytest
import filecmp
from contextlib import redirect_stdout
import io, sys
from src import driver

MSG_FILEIOERROR = "The source file does not exist or empty."


def test_source_decode_compare(file_names):
    """
    The test checks that source file is identical with the encoded_decoded result file
    """
    assert filecmp.cmp(file_names[0], file_names[1], shallow=False)


@pytest.mark.parametrize('command, sourcefile', [('e', 'empty.txt'),
                                                 ('e', 'doesnotexist.txt'),
                                                 ('d', 'empty.txt'),
                                                 ('d', 'doesnotexist.txt')
                                                 ])
def test_empty_source(command, sourcefile, prepare_sys_argv):
    """
    Checks the correct error message from driver.py if source file is empty or does not exist
    :param command: 'e' or 'd' as driver.py accepts
    :param sourcefile: source file name
    :param prepare_sys_argv:
    :return:
    """
    sys.argv.extend([command, sourcefile])
    f = io.StringIO()
    with redirect_stdout(f):
        driver.main()

    assert MSG_FILEIOERROR in f.getvalue()
