import phunspell
import inspect
import unittest


class TestLvLV(unittest.TestCase):
    pspell = phunspell.Phunspell('lv_LV')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("kvēpinātājs"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "piežulgt kvēpinātājs pārpeldēt pamatieguldījums Veremi borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
