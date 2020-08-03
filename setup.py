from distutils.core import setup
setup(
    name = 'pyperiods',
    packages = [
        'pyperiods',
        'pyperiods.django',
        'pyperiods.restframework',
    ],
    version = '1.1.0',
    description = 'Tools for representing and manipulating periods of time (i.e. months and years)',
    author = 'David Marquis',
    author_email = 'david@radiant3.ca',
    url = 'https://github.com/davidmarquis/pyperiods',
    download_url = 'https://github.com/davidmarquis/pyperiods/tarball/1.0.1',
    keywords = ['period', 'year', 'years', 'month', 'months'],
    classifiers = [],
)