import os
import phunspell
import inspect
import unittest
import tempfile

TEMPDIR = tempfile.gettempdir()


class TestPhunspellObjectStoreExpected(unittest.TestCase):
    loc = "ru_RU"
    # use object path
    pspell = phunspell.Phunspell(object_storage=TEMPDIR)
    pspell.dictionary_loader([loc])

    def tearDown(self):
        try:
            os.remove(os.path.join(TEMPDIR, self.loc))
        except FileNotFoundError as error:
            print(error)

    def test_dict_obj_expected(self):
        """local object expected and used"""

        # exists
        filepath = os.path.join(TEMPDIR, self.loc)
        self.assertTrue(os.path.exists(filepath))

        self.assertTrue(self.pspell.lookup("наденутся", loc=self.loc))
        self.assertFalse(self.pspell.lookup("phunspell", loc=self.loc))

        # still exist
        self.assertTrue(os.path.exists(filepath))


if __name__ == "__main__":
    unittest.main()
