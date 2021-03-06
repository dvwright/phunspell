import phunspell
import inspect
import unittest


class TestUkUA(unittest.TestCase):
    pspell = phunspell.Phunspell('uk_UA')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("фосфоричність"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = (
            "фосфоричність провіщати практикуючи піретрум застібування borken"
        )
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )

    def test_to_list(self):
        words = "!\"#$%&'()*+, -./:;<=>?@[]^_`{|}~ бас-гітара бас-кларнет безособово-предикативний безумовно-рефлекторний $%^(*"  # noqa E501
        self.assertListEqual(
            self.pspell.to_list(words),
            [
                "бас-гітара",
                "бас-кларнет",
                "безособово-предикативний",
                "безумовно-рефлекторний",
            ],
        )


if __name__ == "__main__":
    unittest.main()
