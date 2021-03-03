import phunspell
import inspect
import unittest

class TestPhunspell(unittest.TestCase):
    spell = phunspell.Phunspell('en_US')

    def test_package(self):
        self.assertTrue(inspect.ismodule(phunspell))

    def test_exception_if_not_dictionary(self):
        with self.assertRaises(phunspell.PhunspellError):
            phunspell.Phunspell('no-lang')

    # pspell = Phunspell('en_US')

    # print(pspell.lookup("phunspell")) # False
    # print(pspell.lookup("about")) # True

    # mispelled = pspell.lookup_list("Bill's TV is borken".split(" "))
    # print(mispelled) # ["borken"]

    # for suggestion in pspell.suggest('phunspell'):
    #     print(suggestion)
    #     # Hunspell
    #     # spellbound
    #     # unshapely
    #     # speller
    #     # principle
    #     # principal

    # # exception
    # # pspell = Phunspell('cs_CZ')

    # # ['this', 'is', 'a', 'list', 'of', 'words', 'right', 'here']
    # print(pspell.to_list(
    #     "This !\"#$%&'()*+, -./:;<=>?@[]^_`{|}~ IS, A lISt? OF words!?, $%^( right here*"
    #     )
    # )

    # # pspell = Phunspell("en_US")
    # # mispelled = pspell.lookup_list(
    # #     "python is programing language".split(" ")
    # # )
    # # print(mispelled)


if __name__ == "__main__":
    unittest.main()
