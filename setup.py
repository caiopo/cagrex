from setuptools import setup, find_packages


setup(
    name='cagrex',
    version='0.3.1',
    packages=find_packages(),
    install_requires=['requests', 'bs4', 'mechanicalsoup'],
)
