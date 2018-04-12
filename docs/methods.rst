Methods and Modules
===================

An easy to use GUI that allows users to encrypt their USB drives in a simple way. Users can also add and delete keys to their already encrypted drives through this application.
Get this project `here <https://github.com/udrivencrypt/udrivencrypt>`_.
The methods and modules written to develop this GUI are as follows.


Methods
-------

       **1 \ __init__.py:**
          This method is used to call the main method and sets layout for application window.


Modules
-------

        **2 \ main.py:**
          The execution starts from this method and the application is built. This module has following methods:

                - \ **list_device:** 
                  List all the connected USB drives (both encrypted and nonencrypted). It uses 'df -h' command to filter connected USB drives by checking mount point and gets labels of each USB drive. 
                  The 3 checkboxes 'Encrypt USB drive', 'Add Keys', 'Delete Keys' are handled using methods Entoggle, Atoggle and Dtoggle respectively. When the user checks one of the checkbox, the gorupbox associated with that checkbox gets set visible and other two groupboxes remain disabled.
                
                - \ **check:** 
                Checks which checkbox is checked and whether any drive from corresponding drop-down menu is selected or not.

                - \ **password_popup:** 
                Creates a popup window, where user is asked to enter superuser password. This is called when the user clicks continue button.

                - \ **format:** 
                Unmounts the selected device and erases all signatures.

                - \ **finish:** 
                Creates a popup window, where user is asked to enter a label for selected device.

                - \ **create_luks_partition:** 
                Encrypts the device using cryptsetup commands.

                - \ **listEncryptedDevices:** 
                Lists all encrypted devices. It uses 'lsblk' command to filter only encrypted devices by checking FSTYPE.

                - \ **addKey:** 
                Adds new backup key for already encrypted device.

                - \ **delKey:** 
                Deletes entered key.


        **2 \ encrypt.py:**

                - \ **Encrypt:** 
                Enables groupbox for encryption of devices.


        **3 \ add.py:**

                - \ **Add:** 
                Enables groupbox for adding new key.


        **4 \ delete.py:**
                
                - \ **Delete:** 
                Enables groupbox for deleting an existing key.


