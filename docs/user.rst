Getting Started
===============

Introduction
------------
Providing security to the data in USB drives has become a topic of concern. udrivencrypt provides a GUI for performing encryption of USB drives where users will just have to click buttons and enter data as guided. 
udrivencrypt allows users to encrypt USB drives, add passwords to already encrypted USB drives and delete passwords from already encrypted USB drives. It uses `LUKS <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/installation_guide/ch29s02>`_ commands at background and the GUI is built using PyQt5.


Features
--------

**Encrypt USB Drive**


  * udrivencrypt provides list of only unencrypted USB drives.

  * udrivencrypt formats the selected USB drive.

  * udrivencrypt creates LUKS partition.

  * udrivencrypt allows user to add custom passphrase.



**Add new key for encrypted USB drive**


  * udrivencrypt provides list of only encrypted USB drives.

  * udrivencrypt asks for existing passphrase.

  * udrivencrypt authenticates user.

  * udrivencrypt allows user to add new backup keys.

  * udrivencrypt displays warning if all eight key slots are full.



**Delete key from encrypted USB drive**


  * udrivencrypt provides list of only encrypted USB drives.

  * udrivencrypt asks for existing passphrase.

  * udrivencrypt authenticates user.

  * udrivencrypt asks for passphrase to be deleted.

  * udrivencrypt deletes the desired passphrase.

  * udrivencrypt displays warning if past is being deleted. (If last passphrase gets deleted, user will lose the access to data and will have to format the drive unwantedly.)


Installation
------------

  * Create virtual environment:

                $ python3 -m venv *virtual_environment_name*

                $ source *virtual_environment_name*/bin/activate
  
  * Clone project from github:

                $ git clone https://github.com/udrivencrypt/udrivencrypt.git


  * Install the prerequistics to run the application:
        
                $ pip install -r requirement.txt


  * Build the application:

                $ python setup.py install

                $ python setup.py build

  * Open terminal and enter the command 'udrivencrypt'.


  * Encrypt your USB and make your data safe.

