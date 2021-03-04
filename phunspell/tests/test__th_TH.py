import phunspell
import inspect
import unittest


class TestThTH(unittest.TestCase):
    pspell = phunspell.Phunspell('th_TH')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("พริ้มเพรา"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "ประเทศชาติ พริ้มเพรา เปิดช่อง จำราญ อาร์เอสเอส borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
