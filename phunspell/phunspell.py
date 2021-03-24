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
from spylls.hunspell import Dictionary

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
    # "ca-valencia": ["ca", "?"], # a dialect? used?
    "ca": ["ca", "Catalan ?"],
    "ca_ES": ["ca", "Catalan"],  # guessing that ca should be ca_ES
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

# memoize - only if using object_storage feature
DICTIONARIES_LOADED = {}


class PhunspellError(Exception):
    def __init__(self, message):
        Exception.__init__(self, "%s" % (message))


class PhunspellObjectStore:
    """Create local object stores of all dictionaries
    meant to only be run once.

    NOTE: Will need to be rerun anytime a dictionary is updated
    """

    def __init__(self, path):
        """NOTE: meant to be run once to
        create/store local pickled dictionary objects
        """
        try:
            pspell = Phunspell(object_storage=path)
            pspell.dictionary_loader(pspell.dictionaries_all())
            # pspell.dictionary_loader(['ca', 'ru_RU'])
        except (
            FileNotFoundError,
            KeyError,
            TypeError,
            ValueError,
            PhunspellError,
        ) as error:
            raise PhunspellError(
                "phunspell object store, dictionary not found {}".format(error)
            )


class Phunspell:
    """pure Python spell checker, utilizing Spylls a port of Hunspell"""

    def __init__(self, loc_lang="en_US", loc_list=[], object_storage=None):
        """Load passed dictionary (loc_lang) on init
        dictionary must be of the form Locale_Langage
        e.g. "en_US"

        Can specify a local directory path to dictionary objects

        params:
            loc_list : ["en_US", "de_AT", "de_DE", "el_GR", etc]
            object_storage : "/home/dwright/python/phunspell/pickled_data/"

        See README for all supported languages
        """
        try:
            self.object_storage = object_storage

            if len(loc_list) > 0:
                # if locales passed, load specified dictionaries on init
                self.dictionary_loader(loc_list)
            else:
                # load single loc dictionary on init
                self.dict_dirpath(loc_lang)

                # use local dictionaries
                self.dictionary = Dictionary.from_files(self.dict_path)
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
        """Return included dictionary locales names"""
        return [n for n in DICTIONARIES.keys() if n.find('_') != -1]

    def dictionary_load(self, loc):
        """load stored dictionary object for locale"""
        try:
            if loc in DICTIONARIES_LOADED:
                self.dictionary = DICTIONARIES_LOADED[loc]
                return

            if self.object_storage:
                filepath = os.path.join(self.object_storage, loc)

                if os.path.exists(filepath):
                    pfile = open(filepath, 'rb')
                    stored_dic = pickle.load(pfile)
                    self.dictionary = stored_dic
                    pfile.close()
                    # memoize
                    DICTIONARIES_LOADED[loc] = stored_dic
                else:
                    # not found it object_storage, create it
                    self.dictionary_store(loc)
            else:
                # not using object store
                # open dist included dictionary directly
                self.dict_dirpath(loc)
                self.dictionary = Dictionary.from_files(self.dict_path)
        except (TypeError, OSError) as error:
            raise PhunspellError("Cannot load dictionary {}".format(error))

    def dictionary_store(self, loc):
        """iterate locale dump dictionary to object
        pickle the dictionary
        """
        try:
            if self.object_storage:
                filepath = os.path.join(self.object_storage, loc)

                self.dict_dirpath(loc)
                # read dictionaries from distrubtion path
                data = Dictionary.from_files(self.dict_path)

                # open object_storage local path to dump object to
                pfile = open(filepath, 'wb')
                pickle.dump(data, pfile)
                pfile.close()

                self.dictionary = data

                # memoize it
                DICTIONARIES_LOADED[loc] = data
        except (KeyError, TypeError, OSError) as error:
            raise PhunspellError("Cannot write file {}".format(error))

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

        en_* based languages only?

        TODO: punctuation for other languages?

        TODO:
            remove non-breaking unicode char from string: \xa0
        "The New\xa0Movie" => ['The', 'New\xa0Movie']

        i.e. update to: "NFKD"?
        return [unicodedata.normalize("NFKC", x.strip()) for x in words if len(x) and x not in ["'", '-']] # noqa E501
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

    def lookup(self, word, loc=None):
        """takes word (string)
        removes beginning and trailing whitespace
        returns true if found in dictionary, false otherwise
        """
        try:
            if loc:
                self.dictionary_load(loc)

            return self.dictionary.lookup(word.strip())
        except ValueError as error:
            raise PhunspellError(
                "phunspell, dictionary lookup failed {}".format(error)
            )

    def lookup_list(self, wordlist, loc=None):
        """takes list of words, returns list words not found
        in dictionary

        In: ["word", "another", "more", "programming"]
        Out: ["programing"]
        """
        try:
            if loc:
                self.dictionary_load(loc)

            flagged = []
            for word in wordlist:
                if not self.dictionary.lookup(word.strip()):
                    flagged.append(word)
            return flagged
        except ValueError as error:
            raise PhunspellError(
                "phunspell, dictionary lookup_list failed {}".format(error)
            )

    def suggest(self, word, loc=None):
        """takes word (string)
        removes beginning and trailing whitespace
        returns suggested spelling if not found in dictionary
        returns nothing if found in dictionary
        """
        try:
            if loc:
                self.dictionary_load(loc)

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
    import sys

    # TEST - local object expected but not exist,
    # will be read from dictionary and dumped to local storage
    # so it's there next time
    # NOTE: feature is ONLY if user set storage_path is set
    # pspell = Phunspell(object_storage="/tmp/d")
    # # should load default en_US dictionary
    # print(pspell.lookup("phunspell"))  # False
    # print(pspell.lookup("about"))  # True

    # # load russian dictionary - should create a dump file in /tmp/d
    # print(pspell.lookup("phunspell", loc='ru_RU'))  # False
    # print(pspell.lookup("about", loc='ru_RU'))  # False

    # sys.exit()

    pspell = Phunspell()
    # should load default en_US dictionary
    print(pspell.lookup("phunspell"))  # False
    print(pspell.lookup("about"))  # True

    # load russian dictionary - should NOTE create a dump file in /tmp/d
    print(pspell.lookup("phunspell", loc='ru_RU'))  # False
    print(pspell.lookup("about", loc='ru_RU'))  # False

    sys.exit()

    # create pickled dictionaries for all dictionaries
    # import tempfile
    # TEMPDIR = tempfile.gettempdir()
    # storage_path = "/var/folders/vd/n_l9hxb57msdcc_33myhkqmw0000gn/T"
    storage_path = "/tmp/foo"

    # run once:
    # pspell = PhunspellObjectStore(path=storage_path)
    # import sys
    # sys.exit()

    dicts_words = {
        "af_ZA": "voortgewoed",
        "an_ES": "vengar",
        "be_BY": "ідалапаклонніцкі",
        "bg_BG": "удържехме",
        "br_FR": "c'huñvderioù",
        "de_DE": "schilffrei",
        "en_GB": "indict",
        "es_MX": "pianista",
        "fr_FR": "zoomorphe",
    }
    # use cache if already seen
    dicts_words_cached = {
        "an_ES": "vengar",
        "be_BY": "ідалапаклонніцкі",
        "bg_BG": "удържехме",
    }

    # 16.41s user 0.48s system 99% cpu 16.986 total
    pspell = Phunspell(object_storage=storage_path)

    for loc in dicts_words.keys():
        # 36.08s user 0.65s system 99% cpu 36.788 total
        # pspell = Phunspell(loc)
        print(pspell.lookup(dicts_words[loc], loc=loc))

    for loc in dicts_words_cached.keys():
        # 36.08s user 0.65s system 99% cpu 36.788 total
        # pspell = Phunspell(loc)
        print(pspell.lookup(dicts_words[loc], loc=loc))

    # import sys
    # sys.exit()

    pspell = Phunspell(loc_lang="en_US")
    print(pspell.lookup_list("Wonder Woman 1984"))
    print(pspell.lookup_list(pspell.to_list("Wonder Woman 1984")))

    pspell = Phunspell()  # default "en_US"
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
