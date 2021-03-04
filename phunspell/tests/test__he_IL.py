import phunspell
import inspect
import unittest


class TestHeIL(unittest.TestCase):
    pspell = phunspell.Phunspell('he_IL')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("המחישון"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "אונותיהם המחישון דילמתנו בנאמתי החלפותייך borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
