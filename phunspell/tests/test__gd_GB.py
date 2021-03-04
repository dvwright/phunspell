import phunspell
import inspect
import unittest


class TestGdGB(unittest.TestCase):
    pspell = phunspell.Phunspell('gd_GB')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("MhacIlleRuaidh"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "mheur-lorgan bìgeil MhacIlleRuaidh speachas thaigh-consalachd borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
