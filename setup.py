from distutils.core import setup

setup(
    name='mxit',
    version='0.3',
    author='Philip Perold',
    author_email='prperold@gmail.com',
    packages=['mxit'],
    url='https://github.com/Mxit/python-mxit',
    license='LICENSE',
    description="Python utility library for accessing Mxit's public APIs.",
    long_description=open('README.md').read(),
    install_requires=[
        "requests == 2.0.1",
    ],
)

