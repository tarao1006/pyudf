from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyudf',
    version='0.0.0',
    description='Udf file handler',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tarao1006/pyudf',
    author='Taiga Katarao',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Chemistry'
    ],
    packages=find_packages(exclude=('tests',)),
    install_requires=['numpy'],
    python_requires='>=3.7'
)
