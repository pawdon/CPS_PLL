Steps to build python wrappe based on https://scipy-cookbook.readthedocs.io/items/SWIG_NumPy_examples.html

1. Install SWIG (on Linux sudo apt-get install swig).
2. Create a new directory.
3. Copy numpy.i and pyfragments.swg.
4. Create files XXX.h, XXX.c and XXX.i.
5. Create a file setup.py.
6. Run "python setup.py build".
7. Your module is a file XXX.py and a file in build.lib*
