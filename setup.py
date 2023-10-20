import io
import re
import ast
from setuptools import find_packages,setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent Django are
# still present in site-packages. See #18115.


EXCLUDE_FROM_PACKAGES = []
with io.open("src/castanett/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

EXCLUDE_FROM_PACKAGES = [];


setup(
    name='castanett',
    version=version,
    url='https://codehyouka.xyz/',
    author='Codehyouka',
    author_email='plants.coordinators@gmail.com',
    description=('A Python Web microframework that encourages rapid development and clean, pragmatic design.'),
    license='MIT',
    packages=find_packages( "src"),
    package_dir={"": "src"},
    include_package_data=True,
    
    entry_points={'console_scripts': [
        'castanett = castanett.command:autoload',
    ]},
    install_requires=[],
    platforms='any',
    extras_require={
            "pytest": ["pytest"],
            "pytz": ["pytz"],
            "pylint": ["pylint"],
    },
    zip_safe=False,
    classifiers=[
       
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
