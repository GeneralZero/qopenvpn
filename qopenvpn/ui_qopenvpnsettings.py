# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qopenvpn/qopenvpnsettings.ui'
#
# Created: Tue Feb 12 17:28:25 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QOpenVPNSettings(object):
    def setupUi(self, QOpenVPNSettings):
        QOpenVPNSettings.setObjectName(_fromUtf8("QOpenVPNSettings"))
        QOpenVPNSettings.resize(300, 120)
        self.gridLayout = QtGui.QGridLayout(QOpenVPNSettings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(QOpenVPNSettings)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.vpnNameEdit = QtGui.QLineEdit(QOpenVPNSettings)
        self.vpnNameEdit.setObjectName(_fromUtf8("vpnNameEdit"))
        self.gridLayout.addWidget(self.vpnNameEdit, 0, 1, 1, 2)
        self.line = QtGui.QFrame(QOpenVPNSettings)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.sudoCheckBox = QtGui.QCheckBox(QOpenVPNSettings)
        self.sudoCheckBox.setObjectName(_fromUtf8("sudoCheckBox"))
        self.gridLayout.addWidget(self.sudoCheckBox, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(QOpenVPNSettings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.sudoCommandEdit = QtGui.QLineEdit(QOpenVPNSettings)
        self.sudoCommandEdit.setObjectName(_fromUtf8("sudoCommandEdit"))
        self.gridLayout.addWidget(self.sudoCommandEdit, 3, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QOpenVPNSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        self.retranslateUi(QOpenVPNSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QOpenVPNSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QOpenVPNSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QOpenVPNSettings)

    def retranslateUi(self, QOpenVPNSettings):
        QOpenVPNSettings.setWindowTitle(_translate("QOpenVPNSettings", "QOpenVPN Settings", None))
        self.label.setText(_translate("QOpenVPNSettings", "VPN name:", None))
        self.sudoCheckBox.setText(_translate("QOpenVPNSettings", "Use sudo", None))
        self.label_2.setText(_translate("QOpenVPNSettings", "Sudo command:", None))

