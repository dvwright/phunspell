import phunspell
import inspect
import unittest


class TestEtEE(unittest.TestCase):
    pspell = phunspell.Phunspell('et_EE')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("sünoptilise"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = (
            "sünoptilise vohasidki teisendustega lombateski toekustega borken"
        )
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
