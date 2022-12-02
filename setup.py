import setuptools


setuptools.setup(
    name='aoc-library',
    version='0.1.1',
    description='Advent of Code Library',
    author='Liborsaf, Thr0nSK',
    author_email='liborsaf@wetian.eu',
    license='GPL-v3',
    url='https://github.com/Area110011/AdventOfCodeLibrary/',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    python_requires='>=3.11'
)
