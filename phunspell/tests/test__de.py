import phunspell
import inspect
import unittest


class TestDe(unittest.TestCase):
    pspell = phunspell.Phunspell('de_CH')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("schilffrei"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "adventnacht schilffrei borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")),
            ["adventnacht", "borken"],
        )


if __name__ == "__main__":
    unittest.main()
