import phunspell
import inspect
import unittest


class TestAnES(unittest.TestCase):
    pspell = phunspell.Phunspell('an_ES')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("vengar"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "vengar miseriosament Salvador achustar subversivo borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
