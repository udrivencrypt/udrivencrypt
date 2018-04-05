Getting Started
===============

**1. \ Introduction**
         USB drives have become inseparable part of our lives. Providing security to the data in them has become a topic of concern. 
         LUKS is the specification that allows encryption of USB drives but the process is not easily understood by people less connected to shellcommands and LUKS.
        udrivencrypt provides a GUI for performing encryption of USB drives where users will just have to click buttons and enter data as guided. This the main objective of udrivencrypt is to make encryption easy for not so technical people and prohibiting access to unauthorized people.

**2. \ Features**

        **a. \ Encrypt USB drive**

                i.   udrivencrypt provides list of connected USB drives

                ii.  udrivencrypt formats the selected USB drive

                iii. udrivencrypt creates LUKS partition

                iv.  udrivencrypt custom passphrase

        **b. \ Add new key for encrypted USB drive**

                i.   udrivencrypt asks for existing passphrase

                ii.  udrivencrypt authenticates user

                iii. udrivencrypt adds custom passphrase

                iv.  udrivencrypt displays warning if 8 passphrases already exist.

        **c. \ Delete key from encrypted USB drive**

                i.   udrivencrypt asks for existing passphrase

                ii.  udrivencrypt authenticates user

                iii. udrivencrypt asks for passphrase to be deleted

                iv.  udrivencrypt deletes the desired passphrase

                v.   udrivencrypt displays warning if last passphrase is being deleted. (If last passphrase gets deleted, user will lose the 
                     access to data and will have to format the drive unwantedly.)

**3. \ Installation**

        a. Create virtual environment:
                
                $ python3 -m venv v1  
           (Here v1 is virtual environment name)
                
                $ source v1/bin/activate
           (To activate your virtual environment)


        b. Clone project from github:

                $ git clone `*https://github.com/udrivencrypt/udrivencrypt.git* <https://github.com/udrivencrypt/udrivencrypt.git>`__


        c. Install the prerequisites to run the application:

                $ pip install -r requirement.txt


        d. Build the application:

                $ python setup.py install

                $ python setup.py build


        e. Open Terminal and enter the command ‘udrivencrypt’.


        f. Encrypt your USB and make your data safe.

