from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='seaborn-games',
    version='0.0.1',
    description='SeabornGames installs all of the SeabornGames repositories',
    long_description='',
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/File',
    download_url='https://github.com/SeabornGames/Games/tarball/download',
    keywords=[],
    install_requires=[
        # todo uncomment when all packages are pushed to pypy
        # 'seaborn-logger',
        # 'seaborn-meta',
        # 'seaborn-recorder',
        # 'seaborn-request-client',
        # 'seaborn-table',
        # 'seaborn-timestamp',
    ],
    extras_require={
    },
    packages=['seaborn_games'],
    license='MIT License',
    classifiers=[
        'Intended Audience :: Seaborn Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    entry_points='''
        [console_scripts]
        seaborn_status=seaborn_games.git_commands:seaborn_status
        seaborn_commit=seaborn_games.git_commands:seaborn_commit
        seaborn_push=seaborn_games.git_commands:seaborn_push
        seaborn_pull=seaborn_games.git_commands:seaborn_pull
        seaborn_debug=seaborn_games.git_commands:seaborn_debug
        seaborn_install=seaborn_games.git_commands:seaborn_install
    '''
)
