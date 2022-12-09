from setuptools import setup, find_packages

setup(
    name='Password Generator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    genpsswd=genpsswd:generate
    '''
)
