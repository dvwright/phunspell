import phunspell
import inspect
import unittest

dicts_words = {
    "af_ZA": "voortgewoed",
    "an_ES": "vengar",
    "be_BY": "ідалапаклонніцкі",
    "bg_BG": "удържехме",
    "br_FR": "c'huñvderioù",
    "de_DE": "schilffrei",
    "en_GB": "indict",
    "es_MX": "pianista",
    "fr_FR": "zoomorphe",
}

dicts_words_cached = {
    "an_ES": "vengar",
    "be_BY": "ідалапаклонніцкі",
    "bg_BG": "удържехме",
}

# TODO:
# fix this upstream
# re: reloading dictionaries is not handled upstream
# ResourceWarning: Enable tracemalloc to get the object allocation traceback
# /Users/dwright/Dev/python/misc/dw/lib/python3.8/site-packages/spylls/hunspell/dictionary.py:141: ResourceWarning: unclosed file <_io.TextIOWrapper name='/Users/dwright/Dev/python/Phunspell/phunspell/data/dictionary/de/de_DE.aff' mode='r' encoding='ISO8859-1'>
#   aff, context = readers.read_aff(FileReader(path + '.aff'))
# ResourceWarning: Enable tracemalloc to get the object allocation traceback


class TestMultiLoadNoCache(unittest.TestCase):
    def test_multi_load_no_cache(self):
        for loc in dicts_words.keys():
            # slower performance
            pspell = phunspell.Phunspell(loc)
            self.assertTrue(pspell.lookup(dicts_words[loc], locs=loc))

        for loc in dicts_words_cached.keys():
            # slower performance
            pspell = phunspell.Phunspell(loc)
            self.assertTrue(pspell.lookup(dicts_words[loc], locs=loc))


if __name__ == "__main__":
    unittest.main()
