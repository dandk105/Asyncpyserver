"""test conf class object

Returns
-------
[type]
    [description]
"""

import unittest
from pathlib import Path

from src.config import ConfManage as cm

pathes = {
    "py": "./test/test_dserver.py",
    "json": "./test/test_json.json"
    }


class TestConfig(unittest.TestCase):
    """this class test ../src/config.py file.
    """

    def setUp(self):
        self.target = cm()
        self.str_relational_path = pathes["py"]
        self.path_abs_path = Path(self.str_relational_path).resolve()
        self.path_abs_json = Path(pathes["json"]).resolve()

    def test_convert_path(self):
        str_abs_path = str(self.path_abs_path)
        str_resul_path = self.target.convert_path(self.str_relational_path)
        self.assertEqual(str_abs_path, str_resul_path)

    @unittest.skip("I havent understand strcture of logging yet.")
    def test_logger_setup(self):
        self.target.setup_logging()

    def test_jsonload(self):
        pyobj = self.target.load_jsonfile(str(self.path_abs_json))
        self.assertIs(type(pyobj), dict)

    def test_return_fileobj(self):
        self.target.output_fileobj(self.path_abs_json)
