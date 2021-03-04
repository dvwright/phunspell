import phunspell
import inspect
import unittest


class TestBeBy(unittest.TestCase):
    pspell = phunspell.Phunspell('be_BY')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("ідалапаклонніцкі"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "ідалапаклонніцкі гавею звышгукавы Флемінг падпаўзу borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
