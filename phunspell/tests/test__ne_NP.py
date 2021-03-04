import phunspell
import inspect
import unittest


class TestNeNP(unittest.TestCase):
    pspell = phunspell.Phunspell('ne_NP')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("डम्फु"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "डम्फु दोस्त मगज शिक्षाविद दिशानिर्देश borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
