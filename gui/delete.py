from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,QComboBox,QLabel,QLineEdit,QMessageBox,QProgressBar,
        QMenu, QPushButton, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget,QBoxLayout)


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





