import phunspell
import inspect
import unittest


class TestLoLA(unittest.TestCase):
    pspell = phunspell.Phunspell('lo_LA')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("ເຈັບປວດ"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "ເຈັບປວດ ອົດສາ ເສກາກາ ຮອດ ແມ່ນວ່າ borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
