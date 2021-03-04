import phunspell
import inspect
import unittest


class TestGuIN(unittest.TestCase):
    pspell = phunspell.Phunspell('gu_IN')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("હરિવક્ત્રી"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "હરિવક્ત્રી દોહેલું તલિયું લહેરથી કાલનિરૂપણ borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
