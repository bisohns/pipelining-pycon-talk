import re
import setuptools

REQUIRED_PYTHON = (3, 6)

# Load requirements
REQUIREMENTS = 'requirements.txt'
REQUIREMENTS = [line.strip('\n') for line in open(REQUIREMENTS).readlines()]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name="pycon-2019",
    version='1.0.2',
    author='Domnan Diretnan, Mmadu Manasseh',
    author_email="diretnandomnan@gmail.com",
    description="Welcome to Pycon Nigeria 2019",
    url="https://github.com/bisoncorps/pipelining-pycon-talk",
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords='\
        pycon nigeria',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
)
