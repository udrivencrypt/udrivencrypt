# GUI to encrypt USB drive
An easy-to-use gui for encryption of USB drives using Python (PyQt5) for GUI and LUKS for encryption. Users will be provided a list of connected USB drives and will have to select the one to be encrypted. Further they will have to add password. In case, the drive is already encrypted, users will be able to add new passwords (max 8) or delete passwords.

## Prerequisites

```
Python 2.7+
```

## Installing

* Create virtual environment
```
python3 -m venv v1
```
* Activate virtual environment
```
source v1/bin/activate
```
* Install dependencies using Requirement.txt
```
pip3 install -r Requirement.txt
```
* Install, build and run an application
```
python3 setup.py install
python3 setup.py build
udrivencrypt
```

## Author

* Gajanan More
* Anuja Kulkarni
* Amruta Salunkhe
* Akshata Jadhav

## LICENSE

This project is licensed under the GNU General Public License - see the <a href="https://github.com/udrivencrypt/udrivencrypt/blob/master/LICENSE"> License </a> file for details.

