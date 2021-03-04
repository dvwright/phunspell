import phunspell
import inspect
import unittest


class TestSkSK(unittest.TestCase):
    pspell = phunspell.Phunspell('sk_SK')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("nezbožštite"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = (
            "neodňateľne nezbožštite najtorzovitejších éra zaváňajúci borken"
        )
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
