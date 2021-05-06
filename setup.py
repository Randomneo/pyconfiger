from setuptools import setup

setup(
    name='pyconfiger',
    version='0.1.0',
    packages=['pyconfiger'],
    author='Rostyslav Misiura',
    author_email='rostislav9999@gmail.com',
    maintainer='Rostyslav Misiura',
    maintainer_email='rostislav9999@gmail.com',
    url='https://github.com/Randomneo/pyconfiger',
    description='A simple python module to handle your project settings',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    license=u"GNU Affero General Public License, version 3",
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
