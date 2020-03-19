from distutils.core import setup, Extension
import numpy
from Cython.Build import cythonize

ext = [Extension("im2col_lasagne_cython",sources=["im2col_lasagne_cython.pyx"],include_dirs=[numpy.get_include()]),Extension("acc8_func",sources = ["acc8.c","acc8_func.pyx"]) ]
setup(
    ext_modules=cythonize(ext)
)