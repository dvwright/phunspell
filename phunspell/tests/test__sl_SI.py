import phunspell
import inspect
import unittest

# TODO


class TestSlSL(unittest.TestCase):
    pspell = phunspell.Phunspell('sl_SI')

    def test_true(self):
        self.assertTrue(True)

    # def test_word_found(self):
    #     self.assertTrue(self.pspell.lookup("Podvr¹ièe"))

    # def test_word_not_found(self):
    #     self.assertFalse(self.pspell.lookup("phunspell"))

    # def test_lookup_list_return_not_found(self):
    #     words = "Bala¾ice Podvr¹ièe Mlaèevkah omikanosti napakicam borken"
    #     self.assertListEqual(
    #         self.pspell.lookup_list(words.split(" ")), ["borken"]
    #     )


if __name__ == "__main__":
    unittest.main()
