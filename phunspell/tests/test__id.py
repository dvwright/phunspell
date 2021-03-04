import phunspell
import inspect
import unittest


class TestID(unittest.TestCase):
    pspell = phunspell.Phunspell('id_ID')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("garah-garah"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "seng ubit sehingga garah-garah tendo borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
