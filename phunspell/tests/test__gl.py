import phunspell
import inspect
import unittest


class TestGL(unittest.TestCase):
    pspell = phunspell.Phunspell("gl_ES")

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("Hèctor"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "Rincón Hèctor Ab'Sáber borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
