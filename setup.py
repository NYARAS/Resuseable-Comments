# import os
# from setuptools import find_packages, setup

# with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#     README = readme.read()

# # allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# setup(
#     name='django-calvo-comments',
#     version='0.0.7',
#     packages=find_packages(),
#     include_package_data=True,
#     license='MIT License',  # example license
#     description='A simple Django app to handle comments with javascript.',
#     long_description=README,
#     url='https://github.com/NYARAS/django-calvo-comments',
#     author='Otieno Calvine',
#     author_email='hello@calvine.com',
#     classifiers=[
#         'Environment :: Web Environment',
#         'Framework :: Django',
#         'Framework :: Django :: 1.10',  # replace "X.Y" as appropriate
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: MIT License',  # example license
#         'Operating System :: OS Independent',
#         'Programming Language :: Python',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#         'Topic :: Internet :: WWW/HTTP',
#         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
#     ],
# )



#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2017 by Otieno Calvine
:license: MIT, see LICENSE for more details.
"""
import os
import sys

from setuptools import setup
from setuptools.command.install import install

# circleci.py version
VERSION = "1.1.1"

def readme():
    """print long description"""
    with open('README.rst') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
    name="circleci",
    version=VERSION,
    description="Python wrapper for the CircleCI API",
    long_description=readme(),
    url="https://github.com/NYARAS/Reusable-Comments-CI",
    author="Otieno Calvine",
    author_email="nyarangacalvine@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords='circleci ci cd api sdk',
    packages=['circleci'],
    install_requires=[
        'requests==2.18.4',
    ],
    python_requires='>=3',
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
