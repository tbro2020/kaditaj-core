from setuptools import setup

with open('requirements.txt') as f:
    reqs = [line.rstrip() for line in f]
setup(install_requires=reqs)