# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in whatsapp_integration/__init__.py
from whatsapp_integration import __version__ as version

setup(
	name='whatsapp_integration',
	version=version,
	description='Integrations for Whatsapp for Business',
	author='Diamo',
	author_email='contacto@diamo.com.ar',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
