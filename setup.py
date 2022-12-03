import setuptools


with open("README.md", "r") as file:
    long_description = file.read()


setuptools.setup(
    name='aoc-library',
    version='0.1.3',
    description='Advent of Code Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Area110011/AdventOfCodeLibrary/',
    author='Liborsaf, Thr0nSK',
    author_email='liborsaf@wetian.eu',
    license='GPL-v3',
    classifiers=[],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    python_requires='>=3.11'
)
