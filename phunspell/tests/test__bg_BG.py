import phunspell
import inspect
import unittest


class TestBgBG(unittest.TestCase):
    pspell = phunspell.Phunspell('bg_BG')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("удържехме"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "удържехме премляхме непретрупан пладнуване ралица borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
