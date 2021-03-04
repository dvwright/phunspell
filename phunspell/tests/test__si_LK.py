import phunspell
import inspect
import unittest


class TestSiLK(unittest.TestCase):
    pspell = phunspell.Phunspell('si_LK')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("සන්දියෙ"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "ප්‍රශස්ත සන්දියෙ සර්කාවිගේ හපන් මන්දගාමී borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
