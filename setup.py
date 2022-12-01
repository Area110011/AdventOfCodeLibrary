from setuptools import find_packages, setup

setup(
    name='aoc-library',
    packages=find_packages(include=['aoc']),
    version='0.1.0',
    description='',
    author='Liborsaf',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
