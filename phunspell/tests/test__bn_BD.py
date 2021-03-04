import phunspell
import inspect
import unittest


class TestBnBD(unittest.TestCase):
    pspell = phunspell.Phunspell('bn_BD')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("জিয়ান"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "জিয়ান কপ্‌চাইয়াছিলেন ফাঁপছি হাসাইতে সাপ্‌টাইয়াছি borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
