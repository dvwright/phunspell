import phunspell
import inspect
import unittest


class TestBrFR(unittest.TestCase):
    pspell = phunspell.Phunspell('br_FR')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("c'huñvderioù"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "biziataior c'huñvderioù fikerien farlotetoc'h simud borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
