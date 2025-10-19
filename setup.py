from setuptools import setup, find_packages

setup(
    name='tail-cli',
    version='1.0',
    author='Anastasia Pelyno',
    description='CLI утиліта tail на Python',
    packages=find_packages(),
    install_requires=['click', 'colorama'],
    entry_points={
        'console_scripts': [
            'tail-cli=tail_cli.tail:tail',
        ],
    },
)
