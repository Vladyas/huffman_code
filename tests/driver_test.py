import filecmp


def test_source_decode_compare(file_names):
    assert filecmp.cmp(file_names[0], file_names[1], shallow=False)
