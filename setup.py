import sys

if sys.version_info[0]<3:
	sys.exit('Sorry ,Python < 3 is not supported')

from setuptools import setup

packages=["gui"]

setup(name='udrive-encrypt',
      packages=packages,
      version='1.0',
      description="PyQt5 GUI to encrypt USB drive",
      long_description=open("README.md").read(),
      author='Gajanan akshata Amruta Anuja ',
      author_email='akshatajadhav17@gmail.com',
      #url='',
      zip_safe=False,
      install_requires=["pyqt5"],
      classifiers=['Programming Language :: Python'],
#      entry_points={
#	'console-scripts':[
#		'gui=gui.final:main'
#		]


#	}

      scripts=[
	'script/pyqt',

	],

)
