import os
import re

from setuptools import setup, find_packages


def get_version():
    path = os.path.join(os.path.dirname(__file__), 'lead_sentences', '__init__.py')
    with open(path, 'r') as f:
        content = f.read()
    m = re.search(r'__version__\s*=\s*"(.+)"', content)
    assert m is not None
    return m.group(1)


def long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


version = get_version()

setup(
    name="lead_sentences",
    version=version,
    description="Generate lead-n from texts",
    url="http://github.com/pltrdy/lead_sentences_summarization",
    download_url="https://github.com/pltrdy/lead_sentences_summarization/archive/%s.tar.gz" % version,
    author="pltrdy",
    author_email="pltrdy@gmail.com",
    keywords=["NL", "CL", "natural language processing",
              "computational linguistics", "summarization"],
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Linguistic"
    ],
    license="LICENCE.txt",
    long_description=long_description(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'lead_sentences=lead_sentences.bin.cmd:main'
        ]
    }
)
