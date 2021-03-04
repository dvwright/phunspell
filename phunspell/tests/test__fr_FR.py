import phunspell
import inspect
import unittest


class TestFrFR(unittest.TestCase):
    pspell = phunspell.Phunspell('fr_FR')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("zoomorphe"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "charnel zoomorphe iguane frumentaire borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
