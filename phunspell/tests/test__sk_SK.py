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

    def test_to_list(self):
        words = "!\"#$%&'()*+, -./:;<=>?@[]^_`{|}~ Alma-ata bielo-červený bielo-čierny cyrilo-metodovský červeno-biely Česko-slovensko, $%^(*"  # noqa E501
        self.assertListEqual(
            self.pspell.to_list(words),
            [
                "alma-ata",
                "bielo-červený",
                "bielo-čierny",
                "cyrilo-metodovský",
                "červeno-biely",
                "česko-slovensko",
            ],
        )

        self.assertListEqual(
            self.pspell.to_list(words, lcase=False),
            [
                "Alma-ata",
                "bielo-červený",
                "bielo-čierny",
                "cyrilo-metodovský",
                "červeno-biely",
                "Česko-slovensko",
            ],
        )

        self.assertListEqual(
            self.pspell.to_list(words, lcase=False, filter_all=True),
            [
                "Almaata",
                "bieločervený",
                "bieločierny",
                "cyrilometodovský",
                "červenobiely",
                "Československo",
            ],
        )


if __name__ == "__main__":
    unittest.main()
