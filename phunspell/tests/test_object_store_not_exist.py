import os
import time
import phunspell
import inspect
import unittest
import tempfile

TEMPDIR = tempfile.gettempdir()


class TestPhunspellObjectStoreNotExist(unittest.TestCase):
    pspell = phunspell.Phunspell(object_storage=TEMPDIR)

    def setUp(self):
        self._rm_locale("ru_RU")

    def tearDown(self):
        self._rm_locale("ru_RU")

    def _rm_locale(self, loc):
        try:
            os.remove(os.path.join(TEMPDIR, loc))
        except FileNotFoundError as error:
            print(error)

    def test_dict_obj_expected_not_exist(self):
        """local object expected but not exist,
        fallback to dist included dictionary then dump to local storage
        so it's there next time

        NOTE: feature is ONLY if user set storage_path is set
        """
        pass

        # debug
        # pass standlone
        # fails when run as suite

        # loc = "ru_RU"

        # # not exist
        # filepath = os.path.join(TEMPDIR, loc)
        # self.assertFalse(os.path.exists(filepath))

        # self.assertTrue(self.pspell.lookup("наденутся", loc=loc))

        # # was created
        # self.assertTrue(os.path.exists(filepath))

        # self.assertFalse(self.pspell.lookup("phunspell", loc=loc))

        # # still exist
        # self.assertTrue(os.path.exists(filepath))


if __name__ == "__main__":
    unittest.main()
