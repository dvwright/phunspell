import phunspell
import inspect
import unittest

# TODO


class TestKoKR(unittest.TestCase):
    pspell = phunspell.Phunspell('ko_KR')

    def test_true(self):
        self.assertTrue(True)

    # def test_word_found(self):
    #     self.assertTrue(self.pspell.lookup("불같다"))

    # def test_word_not_found(self):
    #     self.assertFalse(self.pspell.lookup("asdfphunspell"))

    # def test_lookup_list_return_not_found(self):
    #     words = "불같다 협찬한 활강해 서걱거릴 출자해 borken"
    #     self.assertListEqual(
    #         self.pspell.lookup_list(words.split(" ")), ["borken"]
    #     )


if __name__ == "__main__":
    unittest.main()
