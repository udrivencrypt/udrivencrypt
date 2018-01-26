from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,QComboBox,QLabel,QLineEdit,QMessageBox,QProgressBar,
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget,QBoxLayout)


def Encrypt(self):

	self.Echeck=QCheckBox('Encrypt USB Drive',self)
		
	self.Echeck.stateChanged.connect(self.Entoggle)
		
	self.layout.addWidget(self.Echeck)

				
	self.EgroupBox = QGroupBox("")
	self.EcomboBox = QComboBox()
	self.EcomboBox.addItem(' Select your drive')
	device=self.list_device()

	for i in device:
		self.EcomboBox.addItem(i)
		
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







