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

# fmt: off ### doesn't work!!! black still formatted this - bad...
DICTIONARIES = {
    # lang-loc # dir   # language
    "af_ZA": ["af_ZA", "Afrikaans"],
    "an_ES": ["an_ES", "Aragonese"],
    "ar": ["ar", "Arabic"],
    "be_BY": ["be_BY", "Belarusian"],
    "bg_BG": ["bg_BG", "Bulgarian"],
    "bn_BD": ["bn_BD", "?"],
    "bo": ["bo", "?"],
    "br_FR": ["br_FR", "Breton"],
    "bs_BA": ["bs_BA", "?"],
    # ca_ES ? Catalan
    "ca": ["ca", "?"],
    "ca-valencia": ["ca", "?"],
    "cs_CZ": ["cs_CZ", "Czech"],
    "da_DK": ["da_DK", "Danish"],
    "de_AT": ["de", "German"],
    "de_CH": ["de", "German"],
    "de_DE": ["de", "German"],
    "el_GR": ["el_GR", "Greek"],
    "en_AU": ["en", "English (Australian)"],
    "en_CA": ["en", "English (Canada)"],
    "en_GB": ["en", "English (Great Britain)"],
    "en_US": ["en", "English (US)"],
    "en_ZA": ["en", "English (South African)"],
    "es": ["es", "Spanish"],
    "es_AR": ["es", "Spanish"],
    "es_BO": ["es", "Spanish"],
    "es_CL": ["es", "Spanish"],
    "es_CO": ["es", "Spanish"],
    "es_CR": ["es", "Spanish"],
    "es_CU": ["es", "Spanish"],
    "es_DO": ["es", "Spanish"],
    "es_EC": ["es", "Spanish"],
    "es_ES": ["es", "Spanish"],
    "es_GQ": ["es", "Spanish"],
    "es_GT": ["es", "Spanish"],
    "es_HN": ["es", "Spanish"],
    "es_MX": ["es", "Spanish"],
    "es_NI": ["es", "Spanish"],
    "es_PA": ["es", "Spanish"],
    "es_PE": ["es", "Spanish"],
    "es_PH": ["es", "Spanish"],
    "es_PR": ["es", "Spanish"],
    "es_PY": ["es", "Spanish"],
    "es_SV": ["es", "Spanish"],
    "es_US": ["es", "Spanish"],
    "es_UY": ["es", "Spanish"],
    "es_VE": ["es", "Spanish"],
    "et_EE": ["et_EE", "Estonian"],
    "fr_FR": ["fr_FR", "French"],
    "gd_GB": ["gd_GB", "Scottish Gaelic"],
    "gl_ES": ["gl", "?"],
    "gu_IN": ["gu_IN", "Gujarati"],
    "gug_PY": ["gug", "Guarani"],
    "he_IL": ["he_IL", "Hebrew"],
    "hi_IN": ["hi_IN", "Hindi"],
    "hr_HR": ["hr_HR", "Croatian"],
    "hu_HU": ["hu_HU", "Hungarian"],
    "id_ID": ["id", "Indonesian"],
    "is": ["is", "Icelandic"],
    "it_IT": ["it_IT", "Italian"],
    # Kurdish (Turkey)	ku_TR   ?
    "kmr_Latn": ["kmr_Latn", "?"],
    "ko_KR": ["ko_KR", "?"],
    "lo_LA": ["lo_LA", "?"],
    "lt_LT": ["lt_LT", "Lithuanian"],
    "lv_LV": ["lv_LV", "Latvian"],
    # Mapudüngun 	md (arn)   ?
    "ne_NP": ["ne_NP", "?"],
    "nl_NL": ["nl_NL", "Netherlands"],
    "nb_NO": ["no", "Norwegian"],
    "nn_NO": ["no", "Norwegian"],
    "oc_FR": ["oc_FR", "Occitan"],
    "pl_PL": ["pl_PL", "Polish"],
    "pt_BR": ["pt_BR", "Brazilian Portuguese"],
    "pt_PT": ["pt_PT", "Portuguese"],
    "ro_RO": ["ro", "Romanian"],
    "ru_RU": ["ru_RU", "Russian"],
    "si_LK": ["si_LK", "Sinhala"],
    "sk_SK": ["sk_SK", "Slovak"],
    "sl_SI": ["sl_SI", "Slovenian"],
    "sq_AL": ["sq_AL", "?"],
    "sr-Latn": ["sr", "?"],
    "sr": ["sr", "Serbian (Cyrillic and Latin)"],
    "sv_FI": ["sv_SE", "Swedish"],
    "sv_SE": ["sv_SE", "Swedish"],
    "sw_TZ": ["sw_TZ", "Swahili"],
    "te_IN": ["te_IN", "?"],
    "th_TH": ["th_TH", "Thai"],
    "tr_TR": ["tr_TR", "Turkish"],
    "uk_UA": ["uk_UA", "Ukrainian"],
    "vi_VN": ["vi", "Vietnamese"],
    # "hyph_zu_ZA" : ["zu_ZA",    "LANG"],
}
# fmt: on


class PhunspellError(Exception):
    def __init__(self, message):
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
            self.dict_dirpath(loc_lang)
            # print(self.dict_path)

            # use local dictionaries only
            self.dictionary = Dictionary.from_files(self.dict_path)
            # pass directly to spylls (could do for en_US)
            # self.dictionary = Dictionary.from_files(loc_lang)
        except (
            FileNotFoundError,
            KeyError,
            TypeError,
            ValueError,
            PhunspellError,
        ) as error:
            raise PhunspellError("Dictionary not found {}".format(error))

    def find_dict_dirpath(self, dictdir, loc_lang):
        # expected 'underscore' format 'en_US'
        if os.path.isdir(dictdir):
            aff_file = os.path.join(dictdir, "{}.aff".format(loc_lang))
            # expected 'underscore' format 'en_US.aff'
            if os.path.exists(aff_file):
                self.dict_path = os.path.join(dictdir, loc_lang)
                self.loc_lang = loc_lang
                return True
            else:
                # underscore format ('en_US') not found
                # fallback try lang dir 'en'
                loc_lang = loc_lang[0:2]
                dictdir = os.path.join(dictdir, loc_lang)
                aff_file = os.path.join(dictdir, "{}.aff".format(loc_lang))
                if os.path.exists(aff_file):
                    self.dict_path = dictdir
                    self.loc_lang = loc_lang
                    return True
        raise PhunspellError("Dictionary path not found")

    def dict_dirpath(self, loc_lang):
        try:
            dirpath = os.path.dirname(os.path.realpath(__file__))
            dictdir = os.path.join(
                dirpath,
                "data",
                "dictionary",
                DICTIONARIES[loc_lang.strip()][0],
            )
            self.find_dict_dirpath(dictdir, loc_lang)
        except ValueError as error:
            raise PhunspellError("to list failed {}".format(error))

    def to_list(self, sentance):
        """takes string of words and
        splits it into list removing punctuation
        returns list of words

        string.punctuation => !"#$%&'()*+, -./:;<=>?@[]^_`{|}~

        En based languages only!

        TODO: punctuation in other languages
        """
        try:
            words = (
                sentance.lower()
                .translate(str.maketrans('', '', string.punctuation))
                .split(" ")
            )
            return [x.strip() for x in words if len(x)]
        except (FileNotFoundError, TypeError, ValueError) as error:
            raise PhunspellError("to list failed {}".format(error))

    def lookup(self, word):
        """takes word (string)
        removes beginning and trailing whitespace
        returns true if found in dictionary, false otherwise
        """
        try:
            return self.dictionary.lookup(word.strip())
        except ValueError as error:
            raise PhunspellError("Dictionary lookup failed {}".format(error))

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
            raise PhunspellError("Dictionary suggest failed {}".format(error))

    def languages(self):
        # ['Afrikaans', 'Aragonese'...
        return [x[1] for x in DICTIONARIES.values()]

    def dictionaries(self):
        # ['af_ZA', 'an_ES', 'ar'...
        return [x for x in DICTIONARIES.keys()]


if __name__ == "__main__":
    pspell = Phunspell('en_US')
    # pspell = Phunspell('af_ZA')

    print(pspell.lookup("phunspell"))  # False
    print(pspell.lookup("about"))  # True

    mispelled = pspell.lookup_list("Bill's TV is borken".split(" "))
    print(mispelled)  # ["borken"]

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
    print(
        pspell.to_list(
            "This !\"#$%&'()*+, -./:;<=>?@[]^_`{|}~ IS, A lISt? OF words!?, $%^( right here*"
        )
    )

    print(pspell.languages())
    print(pspell.dictionaries())
