"""Installer for the singer-getting-started package."""

from setuptools import find_packages
from setuptools import setup


setup(
    name='singer-getting-started',
    version='0.1.0',
    description='The purpose of this project is to make simple examples '
                'of how singer.io works in practice.',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'License :: MIT License',
    ],
    author='Gasper Vozel',
    author_email='gasper.vozel@niteoweb.com',
    url='https://github.com/karantan/singer-getting-started',
    keywords='singer',
    license='MIT License',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'singer-python',
        'target-csv',
        'tap-fixerio',
    ],
    entry_points='''
        [console_scripts]
        my-ip=main:my_ip
    ''',
)
