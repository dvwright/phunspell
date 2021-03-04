import phunspell
import inspect
import unittest


class TestPtPT(unittest.TestCase):
    pspell = phunspell.Phunspell('pt_PT')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("caulícola"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "licitamente caulícola cintilador mesquinhar granada borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
