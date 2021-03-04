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

```
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
German                       | de (de_AT,de_CH,de_DE)
Greek                        | el_GR
English (Australian)         | en_AU
English (Canada)             | en_CA
English (Great Britain)	     | en_GB
English (US)                 | en_US
English (South African)	     | en_ZA
Spanish	(all variants)       | es
Estonian                     | et_EE
French                       | fr_FR
Scottish Gaelic              | gd_GB
Gujarati                     | gu_IN
Guarani	                     | gug_PY
Hebrew	                     | he_IL
Hindi	                     | hi_IN
Croatian	                 | hr_HR
Hungarian	                 | hu_HU
Icelandic	                 | is
Indonesian	                 | id_ID
Italian	                     | it_IT
Kurdish (Turkey)	         | ku_TR
Lithuanian	                 | lt_LT
Latvian	                     | lv_LV
Mapudüngun	                 | md (arn)
Netherlands	                 | nl_NL
Norwegian	                 | no
Occitan	                     | oc_FR
Polish	                     | pl_PL
Brazilian Portuguese	     | pt_BR
Portuguese	                 | pt_PT
Romanian	                 | ro
Sinhala	                     | si_LK
Slovak	                     | sk_SK
Slovenian	                 | sl_SI
Serbian (Cyrillic and Latin) | sr
Swedish	                     | sv_SE
Swahili	                     | sw_TZ
Tamil	                     | Ta
Thai	                     | th_TH
Turkish	                     | tr_TR
Ukrainian	                 | uk_UA
Vietnamese	                 | vi

#### Tests
```
python -m unittest discover -s phunspell/tests -p "test_*.py"
```

#### Misc
`python`, `python3`, `hunspell`, `libreoffice`, `spell`, `spell checking`
