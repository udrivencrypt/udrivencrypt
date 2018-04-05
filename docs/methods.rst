Methods and Modules
===================

An easy to use GUI that allows users to encrypt their USB drives in a simple way. Users can also add and delete keys to their already 
encrypted drives through this application.
Get this project here: `*https://github.com/udrivencrypt/udrivencrypt* <https://github.com/udrivencrypt/udrivencrypt>`__
The methods and modules written to develop this GUI are as follows.

**1. \ Methods:**

        **1. \ \_\_init\_\_.py:**
                This method is used to call the main method and sets layout for main application window.

**2. \ Modules:**

        **1. \ Main.py:**
                The execution starts from this method and the application is built.
                This module has following methods:
                -  \ **list\_device:** Lists all the connected USB drives (both encrypted and non-encrypted). It uses 'df -h' command to filter 
                  connected USB drives by checking mount point and gets labels of each USB drive. The 3 checkboxes ‘Encrypt USB drive’, ‘Add keys
                  and ‘Delete keys’ are handled using methods Entoggle, Atoggle and Dtoggle respectively. When the user checks one of the checkbox
                  , the groupbox associated with that checkbox gets set visible and other two groupboxes remain disabled.

                -  \ **check:** Checks which checkbox is checked andwhether any drive from corresponding drop-down menu is selected or  not.

                -  \ **password\_popup:** Creates a popup window, where user is asked to enter superuser password. This is called when the user 
                  clicks continue button.

                -  \ **format:** Unmounts the selected device and erases all signatures.

                -  \ **Finish:** Creates a popup window, where user is asked to enter a label for selected device.

                -  \ **create\_luks\_partition:** Encrypts the device using cryptsetup commands.

                -  \ **listEncryptedDevices:** Lists all encrypted devices. It uses 'lsblk' command to filter only encrypted devices by checking
                  FSTYPE.

                -  \ **addKey:** Adds new backup key for already    encrypted device.

                -  \ **delKey:** Deletes entered key.

        **2. encrypt.py:**

                - \ **Encrypt:** Enables groupbox for encryption of drives.

        **3. add.py:**

                - \  **Add:** Enables groupbox for adding new key.

        **4. delete.py:**

                - \  **Delete:** Enables groupbox for deleting an existing key.
