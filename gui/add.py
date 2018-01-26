from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,QComboBox,QLabel,QLineEdit,QMessageBox,QProgressBar,
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget,QBoxLayout)




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
	



