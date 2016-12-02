from distutils.core import setup
setup(
    name = 'pyperiods',
    packages = [
        'pyperiods',
        'pyperiods.django',
        'pyperiods.restframework',
    ],
    version = '0.9',
    description = 'Tools for representing and manipulating periods of time (i.e. months and years)',
    author = 'David Marquis',
    author_email = 'david@radiant3.ca',
    url = 'https://github.com/davidmarquis/pyperiods',
    download_url = 'https://github.com/davidmarquis/pyperiods/tarball/0.9',
    keywords = ['period', 'year', 'years', 'month', 'months'],
    classifiers = [],
)