from setuptools import setup, find_packages

setup(
    name='savable',
    version='1.0.0',
    description='A Python utility for making child classes savable, '
                'providing methods to save and load objects using various formats '
                'such as pickle, zip, dict, and json.',
    author='Giacomo Tanzi',
    author_email='giacomo.tanzi14@gmail.com',
    python_requires=">=3.9",  # Minimum Python version required
    packages=find_packages(),
    install_requires=[
        'pathlib',
        'json',
        'pickle',
        'inspect'],
)
