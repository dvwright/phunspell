import phunspell
import inspect
import unittest


class TestNO(unittest.TestCase):
    pspell = phunspell.Phunspell('nb_NO')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("sjøfarende"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "kompetansebegrep kvalitetskontroller lovreguler datamaterial sjøfarende notword"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["notword"]
        )


if __name__ == "__main__":
    unittest.main()
