import phunspell
import inspect
import unittest


class TestGug(unittest.TestCase):
    pspell = phunspell.Phunspell('gug_PY')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("mba'erepy"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "formula hetyma ytororõ apysa mba'erepy borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
