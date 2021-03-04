import phunspell
import inspect
import unittest

# TODO


class TestTrTR(unittest.TestCase):
    pspell = phunspell.Phunspell('tr_TR')

    def test_true(self):
        self.assertTrue(True)

    # def test_word_found(self):
    #     self.assertTrue(self.pspell.lookup("türeyip"))

    # def test_word_not_found(self):
    #     self.assertFalse(self.pspell.lookup("phunspell"))

    # def test_lookup_list_return_not_found(self):
    #     words = "toplayamayan turşuculuk türeyip envanterlemek acemiliğimde borken"
    #     self.assertListEqual(
    #         self.pspell.lookup_list(words.split(" ")), ["borken"]
    #     )


if __name__ == "__main__":
    unittest.main()
