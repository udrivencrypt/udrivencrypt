# GUI to encrypt USB drive
An easy-to-use gui for encryption of USB drives using Python (PyQt5) for GUI and LUKS for encryption. Users will be provided a list of connected USB drives and will have to select the one to be encrypted. Further they will have to add password. In case, the drive is already encrypted, users will be able to add new passwords (max 8) or delete passwords.

**Prerequisites** <hr/>
  Any system having Linux based operating system can use this application.

**Installing**<hr/>
  Installing PyQt5
	 <ol> <li>pip3 install PyQt5
	      <li>If the above command does not run successfully, you can make a directory and create virtual environment.
			<ul>	<li>mkdir demo
		       		<li> cd demo	
				<li> python -m venv v1
       				<li> source v1/bin/activate
       				<li>pip3 install PyQt5	
			</ul>
		<li>Or you can clone the repo and run following command.
	<ul><li>pip install -r requirement.txt<ul></ol>

**Built With** <hr/>
  PyQt5 - Python binding of the cross-platform GUI toolkit Qt. It is implemented as a Python plug-in. <br>
  PyCharm - Integrated Development Environment, specially used for Python.

**Authors** <hr/>
<ul><li>  Akshata Jadhav
<li>  Gajanan More
  <li>Anuja Kulkarni
  <li>Amruta Salunkhe</ul>
  
**License**<hr/>
  This project is licensed under the GNU General Public License - see the <a href="https://github.com/udrivencrypt/udrivencrypt/blob/master/LICENSE"> License </a> file for details.
