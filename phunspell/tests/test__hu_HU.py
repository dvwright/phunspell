import phunspell
import inspect
import unittest

# TODO


class TestHuHU(unittest.TestCase):
    pass
    # pspell = phunspell.Phunspell('hu_HU')

    # def test_word_found(self):
    #     self.assertTrue(self.pspell.lookup("türkméncentrikusság"))

    # def test_word_not_found(self):
    #     self.assertFalse(self.pspell.lookup("phunspell"))

    # def test_lookup_list_return_not_found(self):
    #     words = "gondatlan türkméncentrikusság Walz ágynemű borken"
    #     self.assertListEqual(
    #         self.pspell.lookup_list(words.split(" ")), ["borken"]
    #     )


if __name__ == "__main__":
    unittest.main()
