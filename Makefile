.PHONY: all clean cython python install

export CC="/usr/local/opt/llvm/bin/clang"
export CPPFLAGS="-I/usr/local/opt/llvm/include"

PIPOPTS=--user

all: python cython install

python:
	pip install $(PIPOPTS) numpy==1.16.2 ase==3.16.2
	pip install $(PIPOPTS) scipy cython sympy

cython:
	cd soapfast/utils;python setup_cython.py build_ext --inplace
install:
	python setup.py install	 

clean:
	cd soapfast/utils;rm -rf *.so build
