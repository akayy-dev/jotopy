from setuptools import setup, find_packages
from pathlib import Path

current_dir = Path(__file__).parent

VERSION = '0.0.1' 
DESCRIPTION = 'Python library for interacting with the jotoba.de API.'
LONG_DESCRIPTION = (current_dir / "README.md").read_text()

# Setting up
setup(
        name="jotopy", 
        version=VERSION,
        author="Ahadu Kebede",
		author_email="ahadukebede@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
		long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)