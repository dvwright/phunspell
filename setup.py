from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='phunspell',
    version='0.1.6',
    url='https://github.com/dvwright/phunspell',
    download_url='https://github.com/dvwright/phunspell/archive/v0.1.6.tar.gz',
    license='MIT',
    description='Pure Python spell checker, utilizing Spylls a port of Hunspell',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='David Wright',
    author_email='dvwright@cpan.org',
    include_package_data=True,
    packages=find_packages(
        exclude=[
            'tests',
            'pyproject.toml',
            'create_test_data.sh',
            'obtain_dicts.rb',
            'obtain_dicts.sh',
            'test_data.txt',
        ]
    ),
    install_requires=['spylls'],
    keywords=['Spelling', 'Hunspell', 'Spylls', 'Python'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
