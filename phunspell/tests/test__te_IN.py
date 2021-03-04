import phunspell
import inspect
import unittest


class TestTeIN(unittest.TestCase):
    pspell = phunspell.Phunspell('te_IN')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("గుర్రుమని"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "గుర్రుమని స్యాట్ ప్రాజాపత్యము ప్రస్తుతి నూ borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
