from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Sorts folder by extensions',
    url='none',
    author='senioree97',
    author_email='chebotarenko.yegor@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=[''],
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:sort']}
)