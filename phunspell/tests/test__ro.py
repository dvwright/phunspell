import phunspell
import inspect
import unittest


class TestRO(unittest.TestCase):
    pspell = phunspell.Phunspell('ro_RO')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("nesesizată"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "rezeflemisindu cvasiumanelor nesesizată Democrată borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
