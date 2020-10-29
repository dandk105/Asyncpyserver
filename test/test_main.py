
import unittest
import main


class TestMain(unittest.TestCase):
    @unittest.skip("main moudule is not complete.")
    def test_seup_logging(self):
        main.setup_logging()

