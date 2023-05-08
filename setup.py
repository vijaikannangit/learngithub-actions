from setuptools import setup, find_packages
try:
   import pypandoc
   long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
   long_description = open('README.md').read()

VERSION = '0.0.5' 
DESCRIPTION = 'My Sample Python package'
LONG_DESCRIPTION = 'My Sample Python package for Calculation and Display'

# Setting up
setup(
       # the name must match the folder name 'vijsamplepackage'
        name="vijsamplepackage", 
        version=VERSION,
        author="Vijai Kannan",
        author_email="vijaik.nd@gmail.com",
        description="Setting up a sample python package",
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'sample package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)