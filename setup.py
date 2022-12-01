import setuptools


setuptools.setup(
    name='aoc-library',
    version='0.1.0',
    description='Advent of Code Library',
    author='Liborsaf',
    author_email='liborsaf@wetian.eu',
    url='https://github.com/Liborsaf/AdventOfCodeLibrary/',
    packages=setuptools.find_packages(),
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    python_requires='>=3.11'
)
