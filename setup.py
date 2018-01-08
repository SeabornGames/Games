from setuptools import setup, find_packages
from pip.req import parse_requirements

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
    ],
    extras_require={
    },
    packages=['seaborn.games'],
    license='MIT License',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    entry_points='''
        [console_scripts]
        seatest=seaborn.games:seatest
        seaborn_status=seaborn.games:seaborn_status
        seaborn_commit=seaborn.games:seaborn_commit
        seaborn_push=seaborn.games:seaborn_push
    '''
)
