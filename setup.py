from setuptools import setup, find_packages

from pimpmyplot._version import __version__

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pimpmyplot',
    version='0.0.3',
    author='andrea maioli',
    author_email='maioliandrea0@gmail.com',
    description='Small collection of functions to make better looking matplotlib plots',
    #long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/clarkmaio/pimpmyplot',
    packages=find_packages(), 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    python_requires='>=3.7',
    install_requires=[
            "matplotlib",
            "numpy"
    ],
)