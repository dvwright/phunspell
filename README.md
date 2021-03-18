# Phunspell

A pure Python spell checker utilizing [spylls](https://github.com/zverok/spylls) a port of [Hunspell](https://hunspell.github.io/).

*NOTE: If you are only supporting languages: English, Russian or Swedish then use [spylls](https://github.com/zverok/spylls) directly: (`pip install spylls`)*

This library includes [dictionaries](https://github.com/LibreOffice/dictionaries) for all languages supported by [LibreOffice](https://wiki.documentfoundation.org/Development/Dictionaries).

Just a note giving credit where it's due, [spylls](https://github.com/zverok/spylls) is a fantastic project which deserves all the credit. There is a [corresponding blog](https://zverok.github.io/blog/2021-01-05-spellchecker-1.html) entry which is a good read. (and of course [Hunspell](https://hunspell.github.io/) itself)

### Usage

    import phunspell

    pspell = phunspell.Phunspell('en_US')
    print(pspell.lookup("phunspell")) # False
    print(pspell.lookup("about")) # True

    mispelled = pspell.lookup_list("Bill's TV is borken".split(" "))
    print(mispelled) # ["borken"]

    for suggestion in pspell.suggest('phunspell'):
        print(suggestion) # Hunspell

### Installation

```shell
pip install phunspell
```

#### Supported Languages
Language                     | Language Code
---------------------------- | -------------
Afrikaans                    | af_ZA
Aragonese                    | an_ES
Arabic                       | ar
Belarusian                   | be_BY
Bulgarian                    | bg_BG
Breton                       | br_FR
Catalan	                     | ca_ES
Czech                        | cs_CZ
Danish                       | da_DK
German                       | de_AT
German                       | de_CH
German                       | de_DE
Greek                        | el_GR
English (Australian)         | en_AU
English (Canada)             | en_CA
English (Great Britain)	     | en_GB
English (US)                 | en_US
English (South African)	     | en_ZA
Spanish	(all variants)       | es
Spanish                      | es_AR
Spanish                      | es_BO
Spanish                      | es_CL
Spanish                      | es_CO
Spanish                      | es_CR
Spanish                      | es_CU
Spanish                      | es_DO
Spanish                      | es_EC
Spanish                      | es_ES
Spanish                      | es_GQ
Spanish                      | es_GT
Spanish                      | es_HN
Spanish                      | es_MX
Spanish                      | es_NI
Spanish                      | es_PA
Spanish                      | es_PE
Spanish                      | es_PH
Spanish                      | es_PR
Spanish                      | es_PY
Spanish                      | es_SV
Spanish                      | es_US
Spanish                      | es_UY
Spanish                      | es_VE
Estonian                     | et_EE
French                       | fr_FR
Scottish Gaelic              | gd_GB
Gujarati                     | gu_IN
Guarani	                     | gug_PY
Hebrew	                     | he_IL
Hindi	                     | hi_IN
Croatian	                 | hr_HR
Hungarian	                 | hu_HU (*TODO*)
Icelandic	                 | is
Indonesian	                 | id_ID
Italian	                     | it_IT
Kurdish (Turkey)	         | ku_TR
Lithuanian	                 | lt_LT
Latvian	                     | lv_LV
Mapudüngun	                 | md (arn) (*TODO*)
Netherlands	                 | nl_NL
Norwegian	                 | nb_NO
Norwegian	                 | nn_NO
Occitan	                     | oc_FR
Polish	                     | pl_PL
Brazilian Portuguese	     | pt_BR
Portuguese	                 | pt_PT
Romanian	                 | ro_RO
Sinhala	                     | si_LK
Slovak	                     | sk_SK
Slovenian	                 | sl_SI
Serbian (Cyrillic)           | sr
Serbian (Latin)              | sr-Latn
Swedish	                     | sv_SE
Swahili	                     | sw_TZ
Tamil	                     | Ta (*TODO*)
Thai	                     | th_TH
Turkish	                     | tr_TR
Ukrainian	                 | uk_UA
Vietnamese	                 | vi_VN

#### Tests
```shell
python -m unittest discover -s phunspell/tests -p "test_*.py"
```

#### Experimental

```python

    # Extended Optional:

    # First time usage:
    # create a directory of dictionaries stored as object
    # makes loading/access much faster

    storage_path = "/home/dvwright/data/phunspell/dictionary_objects"
    # run once only:
    pspell_object_create = PhunspellObjectStore(path=storage_path)


    # Then, typical usage:
    pspell = Phunspell(object_storage=storage_path)

    dicts_words = {
        "an_ES": "vengar",
        "be_BY": "ідалапаклонніцкі",
        "bg_BG": "удържехме",
    }

    for loc in dicts_words.keys():
        print(pspell.lookup(dicts_words[loc], loc=loc))
```

There is an option to build/store all the dictionaries as pickled data. Since there are security risks associated with pickled data we will not include that data in the distrubution.

To create your own local pickled dictionaries:

enter a python shell:
```python
$ python
storage_path = "/home/dvwright/data/phunspell/dictionary_objects"
pspell = PhunspellObjectStore(path=storage_path)
```

*NOTE: You only have to do this once before using the library and it's optional (this will consume a lot of resources!)*

Once completed you should have a picked object for every dictionary supported by this lib.

```shell
$ ls /home/dwright/python/phunspell/pickled_data/
af_ZA
an_ES
be_BY
bg_BG
bn_BD
br_FR
bs_BA
cs_CZ
da_DK
de_AT
de_CH
...
...
...
```

*NOTE: will take up almost 2 GB of space*

```shell
$ du -sh .
1.4G
```

For all future uses of the library just pass the directory as an argument.

```python
storage_path = "/home/dvwright/data/phunspell/dictionary_objects"
pspell = Phunspell(object_storage=storage_path)

# load the specific locale on lookups
pspell.lookup_list(['us-word1', 'us-word2'], loc='en_US')
pspell.lookup('german-word', loc='de_DE')

```

*NOTE: If you ever update dictionary data, you will need to create a new pickle store for it.*

and it should find the dictionaries and load them quickly


#### Misc
`python`, `python3`, `hunspell`, `libreoffice`, `spell`, `spell checking`
