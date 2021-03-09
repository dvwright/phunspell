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

    pspell = phunspell.Phunspell("en_US")

    print(pspell.lookup("phunspell")) # False
    print(pspell.lookup("about")) # True

    mispelled = pspell.lookup_list("Bill's TV is borken".split(" "))
    print(mispelled) # ["bill", "tv", "borken"]

    pspell = phunspell.Phunspell("cs_CZ")

"""

import os
import string
import pickle
import tempfile
import logging
import functools
from spylls.hunspell import Dictionary

TEMPDIR = tempfile.gettempdir()

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

class PhunspellError(Exception):
    def __init__(self, message):
        Exception.__init__(self, "%s" % (message))


class Phunspell:
    """pure Python spell checker, utilizing Spylls a port of Hunspell"""

    def __init__(self, loc_lang="en_US", loc_list=[], load_all=False):
        """Load passed dictionary (loc_lang) on init
        dictionary must be of the form Locale_Langage
        e.g. "en_US"

        params:
            loc_list : ["en_US", "de_AT", "de_DE", "el_GR", etc]
            load_all : Load all supported dictionaries on load True/False

        See README for all supported languages
        """
        try:
            if load_all:
                self.dictionary_loader(self.dictionaries_all())
            elif len(loc_list) > 0:
                # if locales passed, load specified dictionaries on init
                self.dictionary_loader(loc_list)
            else:
                # just load single loc dictionary on init
                self.dict_dirpath(loc_lang)

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
            raise PhunspellError(
                "phunspell, dictionary not found {}".format(error)
            )

    def dictionaries_all(self):
        """Load 'all' dictionaries"""
        return [n for n in DICTIONARIES.keys() if n.find('_') != -1]

    @functools.lru_cache  # memoize
    def dictionary_load(self, loc):
        """load stored dictionary object for locale"""
        try:
            datadir = os.getenv("PICKLED_DATADIR")
            if datadir:
                filepath = os.path.join(datadir, loc)
            else:
                filepath = os.path.join(TEMPDIR, loc)

            logging.debug(f'Load dictionary from directory {filepath}')

            pfile = open(filepath, 'rb')
            stored_dic = pickle.load(pfile)
            # self.dictionary = Dictionary.from_files(stored_dic)
            self.dictionary = stored_dic
            pfile.close()

            logging.debug(f'Loaded dictionary from directory {filepath}')
        except (TypeError, OSError) as error:
            raise PhunspellError(f'Cannot load dictionary: {filepath} {error}')

    def dictionary_store(self, loc):
        """iterate locale dump dictionary to object
        pickle the dictionary

        Can specify an Environement varible to
        local dir to save/load pickled data to

        linux/mac osx:
        $ export PICKLED_DATADIR="/home/dwright/python/phunspell/pickled_data/"
        """
        try:
            datadir = os.getenv("PICKLED_DATADIR")
            if datadir:
                filepath = os.path.join(datadir, loc)
            else:
                filepath = os.path.join(TEMPDIR, loc)

            logging.debug(f'Store dictionary to directory {filepath}')
            # if os.path.exists(filepath):
            self.dict_dirpath(loc)
            pfile = open(filepath, 'wb')
            data = Dictionary.from_files(self.dict_path)
            pickle.dump(data, pfile)
            pfile.close()
            # else:
            #   raise PhunspellError(f'Cant create dictionay path {filepath}')
        except (TypeError, OSError) as error:
            raise PhunspellError(f'Cannot write file: {filepath} {error}')

    def dictionary_loader(self, loc_list):
        """iterate locale list load dictionary for locale

        meant to load dictionaries on init, not return them
        from this call
        """
        for loc in loc_list:
            # XXX skip for now
            # re.error: bad character range ű-ø at position 12
            if loc in ["hu_HU"]:
                continue

            self.dictionary_store(loc)
            # self.dictionary_load(loc)

    def find_dict_dirpath(self, dictdir, loc_lang):
        """find directory for dictionary `loc_lang`

        if found sets:
            self.dict_path = dictionary directory
            self.loc_lang = language locale
        """
        # expecting "underscore" format. e.g. "en_US"
        if os.path.isdir(dictdir):
            aff_file = os.path.join(dictdir, "{}.aff".format(loc_lang))
            # expecting "underscore" format. e.g. "en_US.aff"
            if os.path.exists(aff_file):
                self.dict_path = os.path.join(dictdir, loc_lang)
                self.loc_lang = loc_lang
                return True
            else:
                # underscore format ("en_US") not found
                # fallback try lang dir "en"
                loc_lang = loc_lang[0:2]
                dictdir = os.path.join(dictdir, loc_lang)
                aff_file = os.path.join(dictdir, "{}.aff".format(loc_lang))
                if os.path.exists(aff_file):
                    self.dict_path = dictdir
                    self.loc_lang = loc_lang
                    return True
        raise PhunspellError("phunspell, dictionary path not found")

    def dict_dirpath(self, loc_lang):
        """find directory to dictionary for locale"""
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
            raise PhunspellError("phunspell, to list failed {}".format(error))

    def to_list(self, sentance, lcase=True, filter_all=False):
        """takes string of words and
        splits it into list removing punctuation
        returns list of words

        args: lcase : convert all chars to lower case (the default)
              filter_all : strip all punctuation (set True)
                           strips all punctuation except hyphen and dash ['-]
                           (set False) [the default]

        string.punctuation => !"#$%&'()*+, -./:;<=>?@[]^_`{|}~

        En based languages only!

        TODO: punctuation in other languages
        """
        try:
            if lcase:
                sentance = sentance.lower()

            # allow hyphen and dash ['-]
            punctuation = r"""!"#$%&()*+,./:;<=>?@[\]^_`{|}~"""

            if filter_all:
                punctuation = string.punctuation

            words = sentance.translate(
                str.maketrans('', '', punctuation)
            ).split(" ")
            return [x.strip() for x in words if len(x) and x not in ["'", '-']]
        except (FileNotFoundError, TypeError, ValueError) as error:
            raise PhunspellError("phunspell, to list failed {}".format(error))

    def lookup(self, word, locs=[]):
        """takes word (string)
        removes beginning and trailing whitespace
        returns true if found in dictionary, false otherwise
        """
        try:
            if len(locs) > 0:
                self.dictionary_load(locs)

            return self.dictionary.lookup(word.strip())
        except ValueError as error:
            raise PhunspellError(
                "phunspell, dictionary lookup failed {}".format(error)
            )

    def lookup_list(self, wordlist, locs=[]):
        """takes list of words, returns list words not found
        in dictionary

        In: ["word", "another", "more", "programming"]
        Out: ["programing"]
        """
        try:
            if len(locs) > 0:
                self.dictionary_load(locs)

            flagged = []
            for word in wordlist:
                if not self.dictionary.lookup(word.strip()):
                    flagged.append(word)
            return flagged
        except ValueError as error:
            raise PhunspellError(
                "phunspell, dictionary lookup_list failed {}".format(error)
            )

    def suggest(self, word, locs=[]):
        """takes word (string)
        removes beginning and trailing whitespace
        returns suggested spelling if not found in dictionary
        returns nothing if found in dictionary
        """
        try:
            if len(locs) > 0:
                self.dictionary_load(locs)

            return self.dictionary.suggest(word.strip())
        except ValueError as error:
            raise PhunspellError(
                "phunspell, dictionary suggest failed {}".format(error)
            )

    def languages(self):
        # ["Afrikaans", "Aragonese"...
        return [x[1] for x in DICTIONARIES.values()]

    def dictionaries(self):
        # ["af_ZA", "an_ES", "ar"...
        return [x for x in DICTIONARIES.keys()]


if __name__ == "__main__":
    # create pickled dictionaries for all dictionaries
    # pspell = Phunspell(loc_lang="en_US", load_all=True)
    # import sys
    # sys.exit()

    pspell = Phunspell(loc_lang="en_US")
    print(pspell.lookup_list("Wonder Woman 1984"))
    print(pspell.lookup_list(pspell.to_list("Wonder Woman 1984")))

    pspell = Phunspell() # default "en_US"
    # pspell = Phunspell("af_ZA")

    print(pspell.lookup("phunspell"))  # False
    print(pspell.lookup("about"))  # True

    mispelled = pspell.lookup_list("Bill's TV is borken".split(" "))
    print(mispelled)  # ["borken"]

    for suggestion in pspell.suggest("phunspell"):
        print(suggestion)
        # Hunspell
        # spellbound
        # unshapely
        # speller
        # principle
        # principal

    # exception
    # pspell = Phunspell("cs_CZ")

    # ["this", "is", "a", "list", "of", "words", "right", "here"]
    print(
        pspell.to_list(
            "This !\"#$%&'()*+, -./:;<=>?@[]^_`{|}~ IS, A lISt? OF words!?, $%^( right here*"
        )
    )

    print(pspell.languages())
    print(pspell.dictionaries())
