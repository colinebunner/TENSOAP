import setuptools
from Cython.Build import cythonize
from distutils.extension import Extension

ext_modules = [
    Extension(
    "initsoap",
    ["soapfast/utils/initsoap.pyx"],
    libraries=["m"],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
),
    Extension(
    "build_kernel",
    ["soapfast/utils/build_kernel.pyx"],
    libraries=["m"],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
)
]

setuptools.setup(
    name="tensoap",
    version="0.0.1",
    author="David Wilkins",
    author_email="",
    description='',
    packages=['soapfast', 'soapfast/utils', 'soapfast/scripts'],
    ext_modules=cythonize(ext_modules),
    install_requires = [
      'numpy',
    ],
    zip_safe=False
)
