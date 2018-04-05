import sys

if sys.version_info[0]<3:
	sys.exit('Sorry ,Python < 3 is not supported')

from setuptools import setup,find_packages



setup(name='udrivencrypt',
      packages=find_packages(),
      version='1.0.0',
      description="GUI to encrypt USB drive using PyQt5",
      long_description=open("README.md").read(),
      author='Gajanan More, '
             'Akshata Jadhav, '
             'Anuja Kulkarni, '
             'Amruta Salunkhe',
      author_email='anujakulkarni111@gmail.com',
      license='GNU General Public License V3.0',
      url='https://github.com/udrivencrypt/udrivencrypt',
      zip_safe=False,
      install_requires=["pyqt5","pexpect"],
      classifiers=['Programming Language :: Python'],
      entry_points={
          'console_scripts':[
              'udrivencrypt=udrivencrypt.__init__:main'
          ]
      },

)
