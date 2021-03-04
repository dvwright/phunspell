import phunspell
import inspect
import unittest


class TestHrHR(unittest.TestCase):
    pspell = phunspell.Phunspell('hr_HR')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("prigušivač"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "umjesto ukipiti išle prigušivač usprotivljen borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
