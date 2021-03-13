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

# use cache if already seen
dicts_words_cached = {
    "an_ES": "vengar",
    "be_BY": "ідалапаклонніцкі",
    "bg_BG": "удържехме",
}


class TestMultiLoadCache(unittest.TestCase):
    pspell = phunspell.Phunspell()

    def test_multi_load_cache(self):
        for loc in dicts_words.keys():
            self.assertTrue(self.pspell.lookup(dicts_words[loc], loc=loc))

        for loc in dicts_words_cached.keys():
            self.assertTrue(self.pspell.lookup(dicts_words[loc], loc=loc))


if __name__ == "__main__":
    unittest.main()
