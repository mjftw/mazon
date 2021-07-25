from setuptools import setup, find_packages


setup(
    name='mazon',
    version='0.0.1',
    author='Merlin Webster',
    author_email='mjftwebster@gmail.com',
    description=('Sudoku solver'),
    python_requires='>=3.7',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    license='GPLv3',
    install_requires=[
        'pytest',
        'numpy'
    ]
)