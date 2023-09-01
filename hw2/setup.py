from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Sorts folder by extensions',
    url='https://github.com/senioree97/goit_2023/tree/e64de783dba3cb7cb71e8445c4667d913c14da27/hw2',
    author='senioree97',
    author_email='chebotarenko.yegor@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=[''],
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:sort']}
)