"""
Building the GridCut wrapper

>>> python setup.py build_ext --inplace
>>> python setup.py install
"""

import os
import requests
import zipfile

try:
    from setuptools import setup, Extension # , Command, find_packages
    from setuptools.command.build_ext import build_ext
except ImportError:
    from distutils.core import setup, Extension # , Command, find_packages
    from distutils.command.build_ext import build_ext

PACKAGE = 'GridCut-1.3.zip'
HERE = os.path.abspath(os.path.dirname(__file__))
URL_ZIP = 'http://gridcut.com/dl/%s' % PACKAGE
PATH_CODE = os.path.join(HERE, 'code')
PATH_GRIDCUT = os.path.join(PATH_CODE, 'include', 'GridCut')
PATH_ALPHAEXP = os.path.join(PATH_CODE, 'examples', 'include', 'AlphaExpansion')
VERSION = os.path.splitext(PACKAGE)[0].split('-')[-1]  # parse version

# DOWNLOAD code
try:  # Python2
    import StringIO
    req = requests.get(URL_ZIP, stream=True)
    with zipfile.ZipFile(StringIO.StringIO(req.content)) as zip_ref:
        zip_ref.extractall(PATH_CODE)
except Exception:  # Python3
    import io
    req = requests.get(URL_ZIP)
    with zipfile.ZipFile(io.BytesIO(req.content)) as zip_ref:
        zip_ref.extractall(PATH_CODE)


assert os.path.exists(PATH_GRIDCUT), 'missing GridCut source code'
assert os.path.exists(PATH_GRIDCUT), 'missing AplhaExpansion source code'


class BuildExt(build_ext):
    """ build_ext command for use when numpy headers are needed.
    SEE: https://stackoverflow.com/questions/2379898
    SEE: https://stackoverflow.com/questions/19919905/how-to-bootstrap-numpy-installation-in-setup-py
    """

    def finalize_options(self):
        build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        # __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

setup(
    name='gridcut',
    version=VERSION,
    author='Willem Olding',
    author_email='willemolding@gmail.com',
    description='pyGridCut: a python wrapper for the grid-cuts package',
    url='https://github.com/Borda/GridCut-python',
    download_url='http://www.gridcut.com/',
    cmdclass={'build_ext': BuildExt},
    ext_modules=[Extension(
        'gridcut',
        ['gridcut.cpp'],
        language='c++',
        include_dirs=[PATH_GRIDCUT, PATH_ALPHAEXP],
        extra_compile_args=["-fpermissive"]
        )
    ],
    setup_requires=['requests', 'numpy'],
    install_requires=['requests', 'numpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
