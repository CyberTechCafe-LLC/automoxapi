from distutils.core import setup
from automoxapi import __version__

try:
    with open('README.rst') as f:
        long_description = f.read()
except:
    long_description = 'Thin python wrapper for the Automox API'


setup(
    name='automoxapi_old',
    version=__version__,
    packages=['automoxapi_old'],
    url='https://github.com/CyberTechCafe-LLC/automoxapi_old',
    license='GNU General Public License v3.0',
    author='Rob Adkerson',
    author_email='r.j.adkerson@gmail.com',
    description='Thin python wrapper for the Automox API',
    long_description=long_description,
    keywords=['automox', 'api']
)
