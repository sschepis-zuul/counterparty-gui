import sys
from setuptools import setup, find_packages
import zuulgui

APP_VERSION = "1.0.0"

required_packages = [
    'appdirs',
    'zuul-cli'
]

setup_options = {
    'name': zuulgui.APP_NAME,
    'version': zuulgui.APP_VERSION,
    'author': 'Zuul Foundation',
    'author_email': 'support@zuul.io',
    'maintainer': 'Ouziel Slama',
    'maintainer_email': 'ouziel@zuul.io',
    'url': 'http://zuul.io',
    'license': 'MIT',
    'description': 'Zuul Wallet',
    'long_description': '',
    'keywords': 'zuul,gozer',
    'classifiers': [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Office/Business :: Financial",
        "Topic :: System :: Distributed Computing"
    ],
    'download_url': 'https://github.com/sschepis-zuul/zuul-gui/releases/tag/v' + zuulgui.APP_VERSION,
    'provides': ['zuulgui'],
    'packages': find_packages(),
    'zip_safe': False,
    'install_requires': required_packages
}

setup(**setup_options)
