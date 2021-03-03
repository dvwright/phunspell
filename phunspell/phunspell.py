# Copyright (c) 2021 David Wright
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Phunspell - A pure Python spell checker, utilizing Spylls a port of Hunspell

    Typical usage:

    import phunspell

    pspell = phunspell.Phunspell('en_US')

    print(pspell.lookup("phunspell")) # False
    print(pspell.lookup("about")) # True

    mispelled = pspell.lookup_list("Bill's TV is borken".split(" "))
    print(mispelled) # ["bill", "tv", "borken"]

    pspell = phunspell.Phunspell('cs_CZ')

"""

import os
import string
from spylls.hunspell import Dictionary

class PhunspellError(Exception):
    def __init__(self,  message):
        Exception.__init__(self, "%s" % (message))

class Phunspell:
    """pure Python spell checker, utilizing Spylls a port of Hunspell"""

    def __init__(self, loc_lang):
        """Load passed dictionary (loc_lang) on init
        dictionary must be of the form Locale_Langage
        e.g. 'en_US'

        See README for all supported languages
        """
        try:
            self.dictionary = Dictionary.from_files(loc_lang)
        except (FileNotFoundError, TypeError) as error:
            raise PhunspellError(
                 "Dictionary not found {}".format(error)
            )

    def to_list(self, sentance):
        """takes string of words and
        splits it into list removing punctuation
        returns list of words

        string.punctuation => !"#$%&'()*+, -./:;<=>?@[]^_`{|}~
        """
        try:
            words = (
                sentance.lower()
                .translate(str.maketrans('', '', string.punctuation))
                .split(" ")
            )
            return [x.strip() for x in words if len(x)]
        except (FileNotFoundError, TypeError, ValueError) as error:
            raise PhunspellError(
                 "to list failed {}".format(error)
            )

    def lookup(self, word):
        """takes word (string)
        removes beginning and trailing whitespace
        returns true if found in dictionary, false otherwise
        """
        try:
            return self.dictionary.lookup(word.strip())
        except ValueError as error:
            raise PhunspellError(
                 "Dictionary lookup failed {}".format(error)
            )

    def lookup_list(self, wordlist):
        """takes list of words, returns list words not found
        in dictionary

        In: ['word', 'another', 'more', 'programming']
        Out: ['programing']
        """
        try:
            flagged = []
            for word in wordlist:
                if not self.dictionary.lookup(word):
                    flagged.append(word)
            return flagged
        except ValueError as error:
            raise PhunspellError(
                 "Dictionary lookup_list failed {}".format(error)
            )

    def suggest(self, word):
        """takes word (string)
        removes beginning and trailing whitespace
        returns suggested spelling if not found in dictionary
        returns nothing if found in dictionary
        """
        try:
            return self.dictionary.suggest(word.strip())
        except ValueError as error:
            raise PhunspellError(
                 "Dictionary suggest failed {}".format(error)
            )

if __name__ == "__main__":
    pspell = Phunspell('en_US')

    print(pspell.lookup("phunspell")) # False
    print(pspell.lookup("about")) # True

    mispelled = pspell.lookup_list("Bill's TV is borken".split(" "))
    print(mispelled) # ["borken"]

    for suggestion in pspell.suggest('phunspell'):
        print(suggestion)
        # Hunspell
        # spellbound
        # unshapely
        # speller
        # principle
        # principal

    # exception
    # pspell = Phunspell('cs_CZ')

    # ['this', 'is', 'a', 'list', 'of', 'words', 'right', 'here']
    print(pspell.to_list(
        "This !\"#$%&'()*+, -./:;<=>?@[]^_`{|}~ IS, A lISt? OF words!?, $%^( right here*"
        )
    )

    # pspell = Phunspell("en_US")
    # mispelled = pspell.lookup_list(
    #     "python is programing language".split(" ")
    # )
    # print(mispelled)

