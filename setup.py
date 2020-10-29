from setuptools.config import read_configuration
from pathlib import Path

conf_path = Path("./setup.cfg")
abs_path = conf_path.resolve()
#should restructure str base object
read_configuration(abs_path)