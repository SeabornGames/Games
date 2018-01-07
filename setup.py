from setuptools import setup, find_packages

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
        'seaborn-file',
        'seaborn-flask-server',
        'seaborn-logger',
        'seaborn-meta',
        'seaborn-request_client',
        'seaborn-table',
        'seaborn-timestamp'
    ],
    extras_require={
    },
    packages=[],
    license='MIT License',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
)
