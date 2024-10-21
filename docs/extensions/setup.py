from setuptools import setup, find_packages

setup(
    name='migrid-sphinx-ext',
    version='0.1.0',
    package_dir={'': 'docs'},
    packages=find_packages(where='docs'),
    install_requires=[
        'Sphinx>=2.0',
        'docutils',
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
)
