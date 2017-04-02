from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))


setup(
    name='cbrf_receiver',
    version='0.1',
    description='Module for obtaining data from CBRF.',
    author='Kirill Shirolapov',
    author_email='kirill.shirolapov@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='CBRF currency ruble',

    packages=find_packages(exclude=['datetime', 'urllib', 'xml']),
)
