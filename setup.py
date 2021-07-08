from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in shuttle_cock/__init__.py
from shuttle_cock import __version__ as version

setup(
	name='shuttle_cock',
	version=version,
	description='Shuttle_cock App',
	author='Aerele',
	author_email='surajitmetya82@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
