# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_baseplate.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1097, 705)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(590, 260, 481, 411))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("pages_ui/baseplate_frame_80.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 211, 71))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pbSave = QtGui.QPushButton(self.frame_2)
        self.pbSave.setGeometry(QtCore.QRect(80, 30, 61, 21))
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.lineEdit = QtGui.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(1, 1, 80, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.sbID = QtGui.QSpinBox(self.frame_2)
        self.sbID.setGeometry(QtCore.QRect(80, 1, 130, 21))
        self.sbID.setMaximum(65535)
        self.sbID.setObjectName(_fromUtf8("sbID"))
        self.pbCancel = QtGui.QPushButton(self.frame_2)
        self.pbCancel.setGeometry(QtCore.QRect(150, 30, 61, 21))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.pbNew = QtGui.QPushButton(self.frame_2)
        self.pbNew.setGeometry(QtCore.QRect(0, 30, 71, 21))
        self.pbNew.setObjectName(_fromUtf8("pbNew"))
        self.pbEdit = QtGui.QPushButton(self.frame_2)
        self.pbEdit.setGeometry(QtCore.QRect(0, 50, 71, 21))
        self.pbEdit.setObjectName(_fromUtf8("pbEdit"))
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 100, 211, 571))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.cbChirality = QtGui.QComboBox(self.frame_3)
        self.cbChirality.setGeometry(QtCore.QRect(130, 261, 80, 20))
        self.cbChirality.setObjectName(_fromUtf8("cbChirality"))
        self.cbChirality.addItem(_fromUtf8(""))
        self.cbChirality.addItem(_fromUtf8(""))
        self.cbChirality.addItem(_fromUtf8(""))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(1, 200, 130, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_11 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(1, 1, 90, 20))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.cbShape = QtGui.QComboBox(self.frame_3)
        self.cbShape.setGeometry(QtCore.QRect(130, 241, 80, 20))
        self.cbShape.setObjectName(_fromUtf8("cbShape"))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.cbShape.addItem(_fromUtf8(""))
        self.pbGoShipment = QtGui.QPushButton(self.frame_3)
        self.pbGoShipment.setGeometry(QtCore.QRect(90, 20, 121, 21))
        self.pbGoShipment.setObjectName(_fromUtf8("pbGoShipment"))
        self.leManufacturer = QtGui.QLineEdit(self.frame_3)
        self.leManufacturer.setGeometry(QtCore.QRect(130, 160, 80, 20))
        self.leManufacturer.setReadOnly(True)
        self.leManufacturer.setObjectName(_fromUtf8("leManufacturer"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(1, 140, 130, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_10 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(1, 20, 90, 20))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_7 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(1, 160, 130, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(1, 180, 130, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.leLocation = QtGui.QLineEdit(self.frame_3)
        self.leLocation.setGeometry(QtCore.QRect(90, 1, 120, 20))
        self.leLocation.setText(_fromUtf8(""))
        self.leLocation.setReadOnly(True)
        self.leLocation.setObjectName(_fromUtf8("leLocation"))
        self.listShipments = QtGui.QListWidget(self.frame_3)
        self.listShipments.setGeometry(QtCore.QRect(1, 40, 209, 91))
        self.listShipments.setObjectName(_fromUtf8("listShipments"))
        self.lineEdit_13 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(1, 261, 130, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_16 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(1, 280, 130, 21))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.dsbNomThickness = QtGui.QDoubleSpinBox(self.frame_3)
        self.dsbNomThickness.setGeometry(QtCore.QRect(130, 200, 80, 21))
        self.dsbNomThickness.setReadOnly(True)
        self.dsbNomThickness.setMinimum(-1.0)
        self.dsbNomThickness.setMaximum(2147483647.0)
        self.dsbNomThickness.setSingleStep(0.05)
        self.dsbNomThickness.setObjectName(_fromUtf8("dsbNomThickness"))
        self.leIdentifier = QtGui.QLineEdit(self.frame_3)
        self.leIdentifier.setGeometry(QtCore.QRect(130, 140, 80, 20))
        self.leIdentifier.setReadOnly(True)
        self.leIdentifier.setObjectName(_fromUtf8("leIdentifier"))
        self.lineEdit_15 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(1, 241, 130, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(1, 221, 130, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.sbRotation = QtGui.QSpinBox(self.frame_3)
        self.sbRotation.setGeometry(QtCore.QRect(130, 280, 80, 21))
        self.sbRotation.setReadOnly(True)
        self.sbRotation.setMinimum(-1)
        self.sbRotation.setMaximum(5)
        self.sbRotation.setObjectName(_fromUtf8("sbRotation"))
        self.frame = QtGui.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(0, 330, 211, 241))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pbAddComment = QtGui.QPushButton(self.frame)
        self.pbAddComment.setGeometry(QtCore.QRect(0, 220, 81, 21))
        self.pbAddComment.setObjectName(_fromUtf8("pbAddComment"))
        self.pteWriteComment = QtGui.QPlainTextEdit(self.frame)
        self.pteWriteComment.setGeometry(QtCore.QRect(1, 150, 209, 71))
        self.pteWriteComment.setPlainText(_fromUtf8(""))
        self.pteWriteComment.setObjectName(_fromUtf8("pteWriteComment"))
        self.lineEdit_14 = QtGui.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(1, 0, 100, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.listComments = QtGui.QListWidget(self.frame)
        self.listComments.setGeometry(QtCore.QRect(0, 20, 211, 121))
        self.listComments.setObjectName(_fromUtf8("listComments"))
        self.pbDeleteComment = QtGui.QPushButton(self.frame)
        self.pbDeleteComment.setGeometry(QtCore.QRect(100, 0, 111, 21))
        self.pbDeleteComment.setObjectName(_fromUtf8("pbDeleteComment"))
        self.leNumKaptons = QtGui.QLineEdit(self.frame_3)
        self.leNumKaptons.setGeometry(QtCore.QRect(130, 300, 80, 21))
        self.leNumKaptons.setReadOnly(True)
        self.leNumKaptons.setObjectName(_fromUtf8("leNumKaptons"))
        self.lineEdit_12 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(1, 300, 130, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.cbSize = QtGui.QComboBox(self.frame_3)
        self.cbSize.setGeometry(QtCore.QRect(130, 220, 80, 21))
        self.cbSize.setObjectName(_fromUtf8("cbSize"))
        self.cbSize.addItem(_fromUtf8(""))
        self.cbSize.addItem(_fromUtf8(""))
        self.cbMaterial = QtGui.QComboBox(self.frame_3)
        self.cbMaterial.setGeometry(QtCore.QRect(130, 180, 81, 21))
        self.cbMaterial.setObjectName(_fromUtf8("cbMaterial"))
        self.cbMaterial.addItem(_fromUtf8(""))
        self.cbMaterial.addItem(_fromUtf8(""))
        self.cbMaterial.addItem(_fromUtf8(""))
        self.pbGoProtomodule = QtGui.QPushButton(Form)
        self.pbGoProtomodule.setGeometry(QtCore.QRect(680, 50, 41, 21))
        self.pbGoProtomodule.setObjectName(_fromUtf8("pbGoProtomodule"))
        self.sbProtomodule = QtGui.QSpinBox(Form)
        self.sbProtomodule.setGeometry(QtCore.QRect(600, 50, 81, 21))
        self.sbProtomodule.setReadOnly(True)
        self.sbProtomodule.setMinimum(-1)
        self.sbProtomodule.setMaximum(2147483647)
        self.sbProtomodule.setObjectName(_fromUtf8("sbProtomodule"))
        self.pbGoStepSensor = QtGui.QPushButton(Form)
        self.pbGoStepSensor.setGeometry(QtCore.QRect(680, 30, 41, 21))
        self.pbGoStepSensor.setObjectName(_fromUtf8("pbGoStepSensor"))
        self.lineEdit_17 = QtGui.QLineEdit(Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(510, 50, 91, 21))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.sbModule = QtGui.QSpinBox(Form)
        self.sbModule.setGeometry(QtCore.QRect(600, 120, 81, 21))
        self.sbModule.setReadOnly(True)
        self.sbModule.setMinimum(-1)
        self.sbModule.setMaximum(2147483647)
        self.sbModule.setObjectName(_fromUtf8("sbModule"))
        self.lineEdit_8 = QtGui.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(510, 120, 91, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_19 = QtGui.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(510, 30, 91, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.sbStepSensor = QtGui.QSpinBox(Form)
        self.sbStepSensor.setGeometry(QtCore.QRect(600, 30, 81, 21))
        self.sbStepSensor.setReadOnly(True)
        self.sbStepSensor.setMinimum(-1)
        self.sbStepSensor.setMaximum(2147483647)
        self.sbStepSensor.setObjectName(_fromUtf8("sbStepSensor"))
        self.pbGoModule = QtGui.QPushButton(Form)
        self.pbGoModule.setGeometry(QtCore.QRect(680, 120, 41, 21))
        self.pbGoModule.setObjectName(_fromUtf8("pbGoModule"))
        self.frame_4 = QtGui.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(260, 30, 211, 191))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.dsbThickness = QtGui.QDoubleSpinBox(self.frame_4)
        self.dsbThickness.setGeometry(QtCore.QRect(130, 170, 79, 20))
        self.dsbThickness.setReadOnly(True)
        self.dsbThickness.setMinimum(-1.0)
        self.dsbThickness.setMaximum(2147483647.0)
        self.dsbThickness.setSingleStep(0.05)
        self.dsbThickness.setObjectName(_fromUtf8("dsbThickness"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(1, 121, 130, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_23 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_23.setGeometry(QtCore.QRect(1, 41, 130, 20))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.lineEdit_24 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_24.setGeometry(QtCore.QRect(1, 81, 130, 20))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.lineEdit_25 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_25.setGeometry(QtCore.QRect(1, 101, 130, 20))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.dsbC2 = QtGui.QDoubleSpinBox(self.frame_4)
        self.dsbC2.setEnabled(True)
        self.dsbC2.setGeometry(QtCore.QRect(131, 41, 79, 20))
        self.dsbC2.setDecimals(2)
        self.dsbC2.setMinimum(-8192.0)
        self.dsbC2.setMaximum(8191.0)
        self.dsbC2.setSingleStep(0.05)
        self.dsbC2.setObjectName(_fromUtf8("dsbC2"))
        self.lineEdit_20 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_20.setGeometry(QtCore.QRect(1, 1, 130, 20))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.lineEdit_21 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_21.setGeometry(QtCore.QRect(1, 21, 130, 20))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.dsbC5 = QtGui.QDoubleSpinBox(self.frame_4)
        self.dsbC5.setEnabled(True)
        self.dsbC5.setGeometry(QtCore.QRect(131, 101, 79, 20))
        self.dsbC5.setDecimals(2)
        self.dsbC5.setMinimum(-8192.0)
        self.dsbC5.setMaximum(8191.0)
        self.dsbC5.setSingleStep(0.05)
        self.dsbC5.setObjectName(_fromUtf8("dsbC5"))
        self.lineEdit_22 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_22.setGeometry(QtCore.QRect(1, 61, 130, 20))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.dsbC1 = QtGui.QDoubleSpinBox(self.frame_4)
        self.dsbC1.setEnabled(True)
        self.dsbC1.setGeometry(QtCore.QRect(131, 21, 79, 20))
        self.dsbC1.setDecimals(2)
        self.dsbC1.setMinimum(-8192.0)
        self.dsbC1.setMaximum(8191.0)
        self.dsbC1.setSingleStep(0.05)
        self.dsbC1.setObjectName(_fromUtf8("dsbC1"))
        self.dsbC0 = QtGui.QDoubleSpinBox(self.frame_4)
        self.dsbC0.setEnabled(True)
        self.dsbC0.setGeometry(QtCore.QRect(131, 1, 79, 20))
        self.dsbC0.setDecimals(2)
        self.dsbC0.setMinimum(-8192.0)
        self.dsbC0.setMaximum(8191.0)
        self.dsbC0.setSingleStep(0.05)
        self.dsbC0.setObjectName(_fromUtf8("dsbC0"))
        self.dsbC3 = QtGui.QDoubleSpinBox(self.frame_4)
        self.dsbC3.setEnabled(True)
        self.dsbC3.setGeometry(QtCore.QRect(131, 60, 79, 21))
        self.dsbC3.setDecimals(2)
        self.dsbC3.setMinimum(-8192.0)
        self.dsbC3.setMaximum(8191.0)
        self.dsbC3.setSingleStep(0.05)
        self.dsbC3.setObjectName(_fromUtf8("dsbC3"))
        self.lineEdit_26 = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_26.setGeometry(QtCore.QRect(1, 170, 130, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.dsbC4 = QtGui.QDoubleSpinBox(self.frame_4)
        self.dsbC4.setEnabled(True)
        self.dsbC4.setGeometry(QtCore.QRect(131, 80, 79, 21))
        self.dsbC4.setDecimals(2)
        self.dsbC4.setMinimum(-8192.0)
        self.dsbC4.setMaximum(8191.0)
        self.dsbC4.setSingleStep(0.05)
        self.dsbC4.setObjectName(_fromUtf8("dsbC4"))
        self.ckKaptonTapeApplied = QtGui.QCheckBox(self.frame_4)
        self.ckKaptonTapeApplied.setGeometry(QtCore.QRect(1, 150, 121, 17))
        self.ckKaptonTapeApplied.setObjectName(_fromUtf8("ckKaptonTapeApplied"))
        self.leFlatness = QtGui.QLineEdit(self.frame_4)
        self.leFlatness.setGeometry(QtCore.QRect(130, 121, 80, 20))
        self.leFlatness.setReadOnly(True)
        self.leFlatness.setObjectName(_fromUtf8("leFlatness"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 211, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 240, 211, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 300, 211, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frame_5 = QtGui.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(260, 500, 211, 171))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.lineEdit_37 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_37.setGeometry(QtCore.QRect(1, 70, 120, 21))
        self.lineEdit_37.setReadOnly(True)
        self.lineEdit_37.setObjectName(_fromUtf8("lineEdit_37"))
        self.cbCheckLeakage_2 = QtGui.QComboBox(self.frame_5)
        self.cbCheckLeakage_2.setGeometry(QtCore.QRect(120, 70, 91, 20))
        self.cbCheckLeakage_2.setObjectName(_fromUtf8("cbCheckLeakage_2"))
        self.cbCheckLeakage_2.addItem(_fromUtf8(""))
        self.cbCheckLeakage_2.addItem(_fromUtf8(""))
        self.lineEdit_32 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_32.setGeometry(QtCore.QRect(1, 130, 120, 21))
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.cbCheckEdgesFirm_2 = QtGui.QComboBox(self.frame_5)
        self.cbCheckEdgesFirm_2.setGeometry(QtCore.QRect(120, 110, 91, 20))
        self.cbCheckEdgesFirm_2.setObjectName(_fromUtf8("cbCheckEdgesFirm_2"))
        self.cbCheckEdgesFirm_2.addItem(_fromUtf8(""))
        self.cbCheckEdgesFirm_2.addItem(_fromUtf8(""))
        self.cbCheckGlueSpill_2 = QtGui.QComboBox(self.frame_5)
        self.cbCheckGlueSpill_2.setGeometry(QtCore.QRect(120, 130, 91, 20))
        self.cbCheckGlueSpill_2.setObjectName(_fromUtf8("cbCheckGlueSpill_2"))
        self.cbCheckGlueSpill_2.addItem(_fromUtf8(""))
        self.cbCheckGlueSpill_2.addItem(_fromUtf8(""))
        self.sbStepKapton_2 = QtGui.QSpinBox(self.frame_5)
        self.sbStepKapton_2.setGeometry(QtCore.QRect(90, 20, 81, 21))
        self.sbStepKapton_2.setReadOnly(True)
        self.sbStepKapton_2.setMinimum(-1)
        self.sbStepKapton_2.setMaximum(2147483647)
        self.sbStepKapton_2.setObjectName(_fromUtf8("sbStepKapton_2"))
        self.lineEdit_34 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_34.setGeometry(QtCore.QRect(1, 110, 119, 21))
        self.lineEdit_34.setReadOnly(True)
        self.lineEdit_34.setObjectName(_fromUtf8("lineEdit_34"))
        self.cbCheckSurface_2 = QtGui.QComboBox(self.frame_5)
        self.cbCheckSurface_2.setGeometry(QtCore.QRect(120, 90, 91, 20))
        self.cbCheckSurface_2.setObjectName(_fromUtf8("cbCheckSurface_2"))
        self.cbCheckSurface_2.addItem(_fromUtf8(""))
        self.cbCheckSurface_2.addItem(_fromUtf8(""))
        self.lineEdit_35 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_35.setGeometry(QtCore.QRect(1, 20, 90, 21))
        self.lineEdit_35.setReadOnly(True)
        self.lineEdit_35.setObjectName(_fromUtf8("lineEdit_35"))
        self.dsbKaptonFlatness_2 = QtGui.QDoubleSpinBox(self.frame_5)
        self.dsbKaptonFlatness_2.setGeometry(QtCore.QRect(120, 150, 90, 20))
        self.dsbKaptonFlatness_2.setReadOnly(True)
        self.dsbKaptonFlatness_2.setMinimum(-1.0)
        self.dsbKaptonFlatness_2.setMaximum(2147483647.0)
        self.dsbKaptonFlatness_2.setSingleStep(0.05)
        self.dsbKaptonFlatness_2.setObjectName(_fromUtf8("dsbKaptonFlatness_2"))
        self.label_5 = QtGui.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 131, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_33 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_33.setGeometry(QtCore.QRect(1, 90, 120, 21))
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.lineEdit_36 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_36.setGeometry(QtCore.QRect(1, 150, 120, 20))
        self.lineEdit_36.setReadOnly(True)
        self.lineEdit_36.setObjectName(_fromUtf8("lineEdit_36"))
        self.label_6 = QtGui.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(0, 50, 191, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pbGoStepKapton_2 = QtGui.QPushButton(self.frame_5)
        self.pbGoStepKapton_2.setGeometry(QtCore.QRect(170, 20, 41, 21))
        self.pbGoStepKapton_2.setObjectName(_fromUtf8("pbGoStepKapton_2"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(260, 480, 211, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(510, 10, 211, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(510, 100, 211, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(760, 460, 141, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(1010, 460, 16, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(920, 290, 16, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(730, 290, 16, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(630, 460, 16, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(720, 620, 16, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(920, 620, 16, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.frame_6 = QtGui.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(260, 321, 211, 101))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.dsbKaptonFlatness = QtGui.QDoubleSpinBox(self.frame_6)
        self.dsbKaptonFlatness.setGeometry(QtCore.QRect(120, 80, 90, 20))
        self.dsbKaptonFlatness.setReadOnly(True)
        self.dsbKaptonFlatness.setMinimum(-1.0)
        self.dsbKaptonFlatness.setMaximum(2147483647.0)
        self.dsbKaptonFlatness.setSingleStep(0.05)
        self.dsbKaptonFlatness.setObjectName(_fromUtf8("dsbKaptonFlatness"))
        self.lineEdit_29 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_29.setGeometry(QtCore.QRect(1, 60, 120, 20))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.cbCheckEdgesFirm = QtGui.QComboBox(self.frame_6)
        self.cbCheckEdgesFirm.setGeometry(QtCore.QRect(120, 40, 90, 20))
        self.cbCheckEdgesFirm.setObjectName(_fromUtf8("cbCheckEdgesFirm"))
        self.cbCheckEdgesFirm.addItem(_fromUtf8(""))
        self.cbCheckEdgesFirm.addItem(_fromUtf8(""))
        self.lineEdit_28 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_28.setGeometry(QtCore.QRect(1, 20, 120, 20))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.lineEdit_30 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_30.setGeometry(QtCore.QRect(1, 40, 119, 20))
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.cbCheckSurface = QtGui.QComboBox(self.frame_6)
        self.cbCheckSurface.setGeometry(QtCore.QRect(120, 20, 90, 20))
        self.cbCheckSurface.setObjectName(_fromUtf8("cbCheckSurface"))
        self.cbCheckSurface.addItem(_fromUtf8(""))
        self.cbCheckSurface.addItem(_fromUtf8(""))
        self.cbCheckGlueSpill = QtGui.QComboBox(self.frame_6)
        self.cbCheckGlueSpill.setGeometry(QtCore.QRect(120, 60, 90, 20))
        self.cbCheckGlueSpill.setObjectName(_fromUtf8("cbCheckGlueSpill"))
        self.cbCheckGlueSpill.addItem(_fromUtf8(""))
        self.cbCheckGlueSpill.addItem(_fromUtf8(""))
        self.lineEdit_31 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_31.setGeometry(QtCore.QRect(1, 80, 120, 20))
        self.lineEdit_31.setReadOnly(True)
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.cbCheckLeakage = QtGui.QComboBox(self.frame_6)
        self.cbCheckLeakage.setGeometry(QtCore.QRect(120, 1, 90, 19))
        self.cbCheckLeakage.setObjectName(_fromUtf8("cbCheckLeakage"))
        self.cbCheckLeakage.addItem(_fromUtf8(""))
        self.cbCheckLeakage.addItem(_fromUtf8(""))
        self.lineEdit_27 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_27.setGeometry(QtCore.QRect(1, 1, 119, 19))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.frame_7 = QtGui.QFrame(Form)
        self.frame_7.setGeometry(QtCore.QRect(260, 260, 211, 21))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.pbGoStepKapton = QtGui.QPushButton(self.frame_7)
        self.pbGoStepKapton.setGeometry(QtCore.QRect(170, 0, 41, 21))
        self.pbGoStepKapton.setObjectName(_fromUtf8("pbGoStepKapton"))
        self.sbStepKapton = QtGui.QSpinBox(self.frame_7)
        self.sbStepKapton.setGeometry(QtCore.QRect(90, 1, 81, 19))
        self.sbStepKapton.setReadOnly(True)
        self.sbStepKapton.setMinimum(-1)
        self.sbStepKapton.setMaximum(2147483647)
        self.sbStepKapton.setObjectName(_fromUtf8("sbStepKapton"))
        self.lineEdit_18 = QtGui.QLineEdit(self.frame_7)
        self.lineEdit_18.setGeometry(QtCore.QRect(1, 1, 90, 19))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))

        self.retranslateUi(Form)
        self.cbChirality.setCurrentIndex(-1)
        self.cbShape.setCurrentIndex(-1)
        self.cbSize.setCurrentIndex(-1)
        self.cbMaterial.setCurrentIndex(-1)
        self.cbCheckLeakage_2.setCurrentIndex(-1)
        self.cbCheckEdgesFirm_2.setCurrentIndex(-1)
        self.cbCheckGlueSpill_2.setCurrentIndex(-1)
        self.cbCheckSurface_2.setCurrentIndex(-1)
        self.cbCheckEdgesFirm.setCurrentIndex(-1)
        self.cbCheckSurface.setCurrentIndex(-1)
        self.cbCheckGlueSpill.setCurrentIndex(-1)
        self.cbCheckLeakage.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pbSave.setText(_translate("Form", "Save", None))
        self.lineEdit.setText(_translate("Form", "Baseplate ID", None))
        self.pbCancel.setText(_translate("Form", "Cancel", None))
        self.pbNew.setText(_translate("Form", "New", None))
        self.pbEdit.setText(_translate("Form", "Edit", None))
        self.cbChirality.setItemText(0, _translate("Form", "achiral", None))
        self.cbChirality.setItemText(1, _translate("Form", "left", None))
        self.cbChirality.setItemText(2, _translate("Form", "right", None))
        self.lineEdit_4.setText(_translate("Form", "Nominal Thickness (mm)", None))
        self.lineEdit_11.setText(_translate("Form", "location", None))
        self.cbShape.setItemText(0, _translate("Form", "full", None))
        self.cbShape.setItemText(1, _translate("Form", "half", None))
        self.cbShape.setItemText(2, _translate("Form", "five", None))
        self.cbShape.setItemText(3, _translate("Form", "three", None))
        self.cbShape.setItemText(4, _translate("Form", "semi", None))
        self.cbShape.setItemText(5, _translate("Form", "semi(-)", None))
        self.cbShape.setItemText(6, _translate("Form", "choptwo", None))
        self.pbGoShipment.setText(_translate("Form", "go to selected", None))
        self.lineEdit_2.setText(_translate("Form", "Identifier", None))
        self.lineEdit_10.setText(_translate("Form", "shipments", None))
        self.lineEdit_7.setText(_translate("Form", "Manufacturer", None))
        self.lineEdit_3.setText(_translate("Form", "Material", None))
        self.listShipments.setToolTip(_translate("Form", "ID (date sent) (SENDER to RECEIVER)", None))
        self.lineEdit_13.setText(_translate("Form", "Chirality", None))
        self.lineEdit_16.setText(_translate("Form", "Rotation", None))
        self.lineEdit_15.setText(_translate("Form", "Shape", None))
        self.lineEdit_6.setText(_translate("Form", "Size (inches)", None))
        self.pbAddComment.setText(_translate("Form", "add comment", None))
        self.lineEdit_14.setText(_translate("Form", "Comments", None))
        self.pbDeleteComment.setText(_translate("Form", "delete selected", None))
        self.lineEdit_12.setText(_translate("Form", "number of kapton layers", None))
        self.cbSize.setItemText(0, _translate("Form", "8", None))
        self.cbSize.setItemText(1, _translate("Form", "6", None))
        self.cbMaterial.setItemText(0, _translate("Form", "Cu", None))
        self.cbMaterial.setItemText(1, _translate("Form", "CuW", None))
        self.cbMaterial.setItemText(2, _translate("Form", "PCB", None))
        self.pbGoProtomodule.setText(_translate("Form", "Go to", None))
        self.pbGoStepSensor.setText(_translate("Form", "Go to", None))
        self.lineEdit_17.setText(_translate("Form", "On protomodule", None))
        self.lineEdit_8.setText(_translate("Form", "On module", None))
        self.lineEdit_19.setText(_translate("Form", "sensor step", None))
        self.pbGoModule.setText(_translate("Form", "Go to", None))
        self.lineEdit_5.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_5.setText(_translate("Form", "Flatness (mm)", None))
        self.lineEdit_23.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_23.setText(_translate("Form", "Corner height 2", None))
        self.lineEdit_24.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_24.setText(_translate("Form", "Corner height 4", None))
        self.lineEdit_25.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_25.setText(_translate("Form", "Corner height 5", None))
        self.dsbC2.setToolTip(_translate("Form", "Corner 2", None))
        self.lineEdit_20.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_20.setText(_translate("Form", "Corner height 0 (mm)", None))
        self.lineEdit_21.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_21.setText(_translate("Form", "Corner height 1", None))
        self.dsbC5.setToolTip(_translate("Form", "Corner 5", None))
        self.lineEdit_22.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_22.setText(_translate("Form", "Corner height 3", None))
        self.dsbC1.setToolTip(_translate("Form", "Corner 1", None))
        self.dsbC0.setToolTip(_translate("Form", "Corner 0 (the corner with the oblong hole)", None))
        self.dsbC3.setToolTip(_translate("Form", "Corner 3", None))
        self.lineEdit_26.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_26.setText(_translate("Form", "thickness (mm)", None))
        self.dsbC4.setToolTip(_translate("Form", "Corner 4", None))
        self.ckKaptonTapeApplied.setText(_translate("Form", "kapton tape applied", None))
        self.label_2.setText(_translate("Form", "baseplate qualification & preparation", None))
        self.label_3.setText(_translate("Form", "kapton application", None))
        self.label_4.setText(_translate("Form", "kaptonized baseplate qualification", None))
        self.lineEdit_37.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_37.setText(_translate("Form", "check leakage current", None))
        self.cbCheckLeakage_2.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckLeakage_2.setItemText(1, _translate("Form", "fail", None))
        self.lineEdit_32.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_32.setText(_translate("Form", "check glue spillage", None))
        self.cbCheckEdgesFirm_2.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckEdgesFirm_2.setItemText(1, _translate("Form", "fail", None))
        self.cbCheckGlueSpill_2.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckGlueSpill_2.setItemText(1, _translate("Form", "fail", None))
        self.lineEdit_34.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_34.setText(_translate("Form", "check edges firm", None))
        self.cbCheckSurface_2.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckSurface_2.setItemText(1, _translate("Form", "fail", None))
        self.lineEdit_35.setText(_translate("Form", "kapton step", None))
        self.label_5.setText(_translate("Form", "second kapton application", None))
        self.lineEdit_33.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_33.setText(_translate("Form", "check surface", None))
        self.lineEdit_36.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_36.setText(_translate("Form", "kapton flatness (mm)", None))
        self.label_6.setText(_translate("Form", "double kapton baseplate qualification", None))
        self.pbGoStepKapton_2.setText(_translate("Form", "Go to", None))
        self.label_7.setText(_translate("Form", "for double kapton baseplates", None))
        self.label_8.setText(_translate("Form", "sensor application", None))
        self.label_9.setText(_translate("Form", "module", None))
        self.label_10.setText(_translate("Form", "corner numbering reference", None))
        self.label_11.setText(_translate("Form", "0", None))
        self.label_12.setText(_translate("Form", "1", None))
        self.label_13.setText(_translate("Form", "2", None))
        self.label_14.setText(_translate("Form", "3", None))
        self.label_15.setText(_translate("Form", "4", None))
        self.label_16.setText(_translate("Form", "5", None))
        self.lineEdit_29.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_29.setText(_translate("Form", "check glue spillage", None))
        self.cbCheckEdgesFirm.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckEdgesFirm.setItemText(1, _translate("Form", "fail", None))
        self.lineEdit_28.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_28.setText(_translate("Form", "check surface", None))
        self.lineEdit_30.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_30.setText(_translate("Form", "check edges firm", None))
        self.cbCheckSurface.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckSurface.setItemText(1, _translate("Form", "fail", None))
        self.cbCheckGlueSpill.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckGlueSpill.setItemText(1, _translate("Form", "fail", None))
        self.lineEdit_31.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_31.setText(_translate("Form", "kapton flatness (mm)", None))
        self.cbCheckLeakage.setItemText(0, _translate("Form", "pass", None))
        self.cbCheckLeakage.setItemText(1, _translate("Form", "fail", None))
        self.lineEdit_27.setToolTip(_translate("Form", "height difference between highest and lowers corners", None))
        self.lineEdit_27.setText(_translate("Form", "check leakage current", None))
        self.pbGoStepKapton.setText(_translate("Form", "Go to", None))
        self.lineEdit_18.setText(_translate("Form", "kapton step", None))

