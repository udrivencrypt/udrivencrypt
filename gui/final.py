from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,QComboBox,QLabel,QLineEdit,QMessageBox,QProgressBar,
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget)


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
		
		self.layout = QBoxLayout(QBoxLayout.TopToBottom)
		self.setLayout(self.layout)
		self.setWindowTitle("GUI")
		self.setFixedSize(500,500)

		self.Encrypt()
		self.Add()
		self.Delete()
		self.Dcheck.toggle()		
		self.Acheck.toggle()		
		self.Echeck.toggle()


	
	def list_device(self):
		os.system("df -h > device")
	
		with open("device","r") as f:
			device=[]
			
			device1=[]
			devicename=[]
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

		


		
	def Encrypt(self):
		self.Echeck=QCheckBox('Encrypt USB Drive',self)
		
		self.Echeck.stateChanged.connect(self.Entoggle)
		
		self.layout.addWidget(self.Echeck)

				
		self.EgroupBox = QGroupBox("")
		self.EcomboBox = QComboBox()
		self.EcomboBox.addItem(' Select your drive')
		device=self.list_device()

		for i in device:
			self.comboBox.addItem(i)
		
		self.EcomboBox.setMinimumWidth(300)
		   
		
		self.EcomboBox.move(150, 50)
		
		self.Ebtn=QPushButton("Format",self)
		self.Ebtn.clicked.connect(self.format)
	
		
		label=QLabel()
		label.setText("Enter your Password")

		self.Etextbox=QLineEdit()
		self.Etextbox.setEnabled(False)
		self.Etextbox.setEchoMode(QLineEdit.Password)
		self.Etextbox.setMaxLength(10)
		
		label1=QLabel()
		label1.setText("Confirm Your Password")

		self.Etextbox1=QLineEdit()
		self.Etextbox1.setEchoMode(QLineEdit.Password)
		self.Etextbox1.setEnabled(False)
		self.Etextbox1.setMaxLength(10)

		self.Ebtn1=QPushButton("Finish",self)
		self.Ebtn1.clicked.connect(self.Finish)
		

		vbox = QVBoxLayout()
		
		vbox.addWidget(self.EcomboBox)
		vbox.addWidget(self.Ebtn)
		vbox.addWidget(label)
		vbox.addWidget(self.Etextbox)
		vbox.addWidget(label1)
		vbox.addWidget(self.Etextbox1)
		vbox.addWidget(self.Ebtn1)
		vbox.addStretch(1)
		self.EgroupBox.setLayout(vbox)
		
		
		self.layout.addWidget(self.EgroupBox)


	def Add(self):
		self.Acheck=QCheckBox('Add Keys',self)
		self.Acheck.stateChanged.connect(self.Atoggle)
		

		self.layout.addWidget(self.Acheck)
		
		self.AgroupBox = QGroupBox("")
		
		self.AcomboBox = QComboBox()
		self.AcomboBox.addItem(' Select your drive')
		#device=self.list_device()

		#for i in device:
		#	self.comboBox.addItem(i)
		
		self.AcomboBox.setMinimumWidth(300)
		 
		
		label=QLabel()
		label.setText("Enter any existing password")

		self.Atextbox=QLineEdit()
		self.Atextbox.setEnabled(False)
		self.Atextbox.setEchoMode(QLineEdit.Password)
		self.Atextbox.setMaxLength(10)
		
		label1=QLabel()
		label1.setText("Enter your new password")

		self.Atextbox1=QLineEdit()
		self.Atextbox1.setEchoMode(QLineEdit.Password)
		self.Atextbox1.setEnabled(False)
		self.Atextbox1.setMaxLength(10)

		self.Abtn1=QPushButton("Finish",self)
		#self.btn1.clicked.connect(self.Finish)
		

		vbox = QVBoxLayout()
		
		vbox.addWidget(self.AcomboBox)
		vbox.addWidget(label)
		vbox.addWidget(self.Atextbox)
		vbox.addWidget(label1)
		vbox.addWidget(self.Atextbox1)
		vbox.addWidget(self.Abtn1)
		vbox.addStretch(1)
		self.AgroupBox.setLayout(vbox)
		

		self.layout.addWidget(self.AgroupBox)
	


	def Delete(self):
		self.Dcheck=QCheckBox(' Delete Keys',self)
		self.Dcheck.stateChanged.connect(self.Dtoggle)
		

		self.layout.addWidget(self.Dcheck)
		
		self.DgroupBox = QGroupBox("")
		
		self.DcomboBox = QComboBox()
		self.DcomboBox.addItem(' Select your drive')
		#device=self.list_device()

		#for i in device:
		#	self.comboBox.addItem(i)
		
		self.DcomboBox.setMinimumWidth(300)
		 
		
		label=QLabel()
		label.setText("Enter any existing password")

		self.Dtextbox=QLineEdit()
		self.Dtextbox.setEnabled(False)
		self.Dtextbox.setEchoMode(QLineEdit.Password)
		self.Dtextbox.setMaxLength(10)
		
		label1=QLabel()
		label1.setText("Enter your new password")

		self.Dtextbox1=QLineEdit()
		self.Dtextbox1.setEchoMode(QLineEdit.Password)
		self.Dtextbox1.setEnabled(False)
		self.Dtextbox1.setMaxLength(10)

		self.Dbtn1=QPushButton("Finish",self)
		#self.btn1.clicked.connect(self.Finish)
		

		vbox = QVBoxLayout()
		
		vbox.addWidget(self.DcomboBox)
		vbox.addWidget(label)
		vbox.addWidget(self.Dtextbox)
		vbox.addWidget(label1)
		vbox.addWidget(self.Dtextbox1)
		vbox.addWidget(self.Dbtn1)
		vbox.addStretch(1)
		self.DgroupBox.setLayout(vbox)
		

		self.layout.addWidget(self.DgroupBox)
	




	def Entoggle(self):
		
		
		if self.Echeck.isChecked()==True:
			self.EgroupBox.setVisible(True)
			self.Acheck.setChecked(False)
			self.Dcheck.setChecked(False) 			
			
			

		else:
			self.EgroupBox.setVisible(False)
			#self.check1.setChecked(True)
		
	def Atoggle(self):
		
		
		
		if self.Acheck.isChecked()==True:
			self.AgroupBox.setVisible(True)
			self.Echeck.setChecked(False)
			self.Dcheck.setChecked(False)
		else:
			
			
			self.AgroupBox.setVisible(False)
			

	def Dtoggle(self):
		
		
		
		if self.Dcheck.isChecked()==True:
			self.DgroupBox.setVisible(True)
			self.Echeck.setChecked(False)
			self.Acheck.setChecked(False)
		else:
			
			
			self.DgroupBox.setVisible(False)
			

		


	def format(self):
		if self.EcomboBox.currentIndex()==0:
			QMessageBox.information(self,'Alert',"Please Select Drive",QMessageBox.Close)
		else:

			choices=QMessageBox.question(self,'Message',"To format disk you need to enter password.Do you want to continue?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
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
				self.widget1.setGeometry(50,50,500,100)
				self.widget1.show()

				btncontinue.clicked.connect(self.passwordfun)





	def passwordfun(self):
			
			
			self.widget1.close()
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
			
			command='wipefs -a --force %s'%filesystem[devicename.index(self.EcomboBox.currentText())]
			
			x=os.system("echo %s |sudo -S %s"%(self.password.text(),command))			
			if x==0:
				# Setting the hBoxLayout as the main layout
				self.widget=QWidget()
				self.widget.setLayout(self.hboxLayout)
				self.widget.setWindowTitle('Dialog with Progressbar')
				self.widget.setGeometry(50,50,500,100)
				self.widget.show()

			
		
				connect=0
				while connect<100:
					connect+=0.001				
					self.progressBar.setValue(connect)
			
				self.widget.close()
				QMessageBox.information(self,'Message',"Drive is formatted.Now you can set password",QMessageBox.Ok) 
				self.Etextbox.setEnabled(True)
				self.Etextbox1.setEnabled(True)

			
			
				


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
