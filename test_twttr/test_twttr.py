from twttr import shorten

def test_shorten():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("albondiga") == "lbndg"
    assert shorten("albo45ndiga25") == "lb45ndg25"
    assert shorten("albondiga,") == "lbndg,"
