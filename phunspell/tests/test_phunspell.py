import phunspell
import inspect
import unittest


class TestPhunspell(unittest.TestCase):
    pspell = phunspell.Phunspell('en_US')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_package(self):
        self.assertTrue(inspect.ismodule(phunspell))

    def test_exception_if_not_dictionary(self):
        with self.assertRaises(phunspell.phunspell.PhunspellError):
            phunspell.Phunspell('no-lang')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("about"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_sentance_to_list_cleaned(self):
        self.assertListEqual(
            self.pspell.to_list(
                "This !\"#$%&'()*+, -./:;<=>?@[]^_`{|}~ IS, A lISt? OF words!?, $%^( right here*"
            ),
            ['this', 'is', 'a', 'list', 'of', 'words', 'right', 'here'],
        )

    def test_lookup_list_return_not_found(self):
        self.assertListEqual(
            self.pspell.lookup_list("Bill's TV is borken".split(" ")),
            ["borken"],
        )

    def test_suggest(self):
        suggestions = [x for x in self.pspell.suggest('phunspell')]
        self.assertListEqual(
            suggestions,
            ["Hunspell"],
        )


if __name__ == "__main__":
    unittest.main()
