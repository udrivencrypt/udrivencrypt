from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,QComboBox,QLabel,QLineEdit,QMessageBox,QProgressBar,
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget,QBoxLayout)
import os
from encrypt import Encrypt
from add import Add
from delete import Delete

filesystem=[]
devicename=[]

class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		
		self.layout = QBoxLayout(QBoxLayout.TopToBottom)
		self.setLayout(self.layout)
		self.setWindowTitle("GUI")
		self.setFixedSize(500,500)

		Encrypt(self)
		Add(self)
		Delete(self)
		self.Dcheck.toggle()		
		self.Acheck.toggle()		
		self.Echeck.toggle()


	
	def list_device(self):
		os.system("df -h > device")
	
		with open("device","r") as f:
			device=[]
			
			device1=[]
			
			for line in f.readlines()[1:]:
				device.append(line.split()[5])
				#device2.append(line.split()[6:])
				device1.append(line.split()[0])
				#if "/run/media" in line.split()[5]:
				#	print(device[5])

			#print(device)
			#print(device1)
			#print(device2)
		
			
			for s in device:
						
				if "/run/media" in s:
					filesystem.append(device1[device.index(s)])
					devicename.append(os.path.basename(s))
		return devicename

	
			

		


	def format(self):
		if self.EcomboBox.currentIndex()==0:
			QMessageBox.information(self,'Alert',"Please Select Drive",QMessageBox.Close)
		else:

			choices=QMessageBox.question(self,'Message',"To format disk you need to enter user password.Do you want to continue?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
			self.complete=0
		
			if choices==QMessageBox.Yes:
				self.password=QLineEdit()
			
				self.password.setEchoMode(QLineEdit.Password)

				labelpass=QLabel()
				labelpass.setText("Enter your password")
				
				btncontinue=QPushButton("Continue")
			
			
				self.hboxpass=QHBoxLayout()
				self.hboxpass.addWidget(labelpass)
				self.hboxpass.addWidget(self.password)
				self.hboxpass.addWidget(btncontinue)


				self.widget1=QWidget()
				self.widget1.setLayout(self.hboxpass)
				self.widget1.setWindowTitle('Password window')
				#self.widget1.setGeometry(50,50,500,100)
				self.widget1.show()

				btncontinue.clicked.connect(self.passwordfun)





	def passwordfun(self):
			
			
			#self.widget1.close()
			self.progressLabel = QLabel('Progress Bar:', self)
		
			# Creating a progress bar and setting the value limits
			self.progressBar = QProgressBar(self)
			self.progressBar.setMaximum(100)
			self.progressBar.setMinimum(0)
			self.btn=QPushButton("Cancel",self)
			
			
			# Creating a Horizontal Layout to add all the widgets
			self.hboxLayout = QHBoxLayout(self)

			# Adding the widgets
			self.hboxLayout.addWidget(self.progressLabel)
			self.hboxLayout.addWidget(self.progressBar)
			self.hboxLayout.addWidget(self.btn)
			
			command='umount %s'%filesystem[devicename.index(self.EcomboBox.currentText())]
			command1='wipefs -a %s'%filesystem[devicename.index(self.EcomboBox.currentText())]
			
			x=os.system("echo %s |sudo -S %s"%(self.password.text(),command))
			
			if x==0:
				y=os.system("echo %s |sudo -S %s"%(self.password.text(),command1))			
				if y==0:
					# Setting the hBoxLayout as the main layout
					self.widget=QWidget()
					self.widget.setLayout(self.hboxLayout)
					self.widget.setWindowTitle('Dialog with Progressbar')
					self.widget.setGeometry(50,50,500,100)
					self.widget1.close()
					self.widget.show()

			
		
					connect=0
					while connect<100:
						connect+=0.001				
						self.progressBar.setValue(connect)
			
					self.widget.close()
					QMessageBox.information(self,'Message',"Drive is formatted.Now you can set password",QMessageBox.Ok) 
					self.Etextbox.setEnabled(True)
					self.Etextbox1.setEnabled(True)
				else:
					choice=QMessageBox.information(self,'Error',"Cannot format drive.Please verify that password is correct ",QMessageBox.Retry|QMessageBox.Close ,QMessageBox.Retry)

					if choice==QMessageBox.Retry:
						self.widget1.show()
				
			
			
				


	def Finish(self):

		#if self.textbox.text()==self.textbox1.text():
		#	os.system()


		choice=QMessageBox.information(self,'Message',"Drive is encrypted.Click 'No' to end .Click 'Yes'to add new key",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
		if choice==QMessageBox.Yes:
			self.AgroupBox.setChecked(True)
		else:	
			sys.exit()	
		
			





	

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()

sys.exit(app.exec_())
