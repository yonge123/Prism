# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hou_ImportFile.ui'
#
# Created: Mon Sep 24 18:31:00 2018
#      by: pyside2-uic @pyside_tools_VERSION@ running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_wg_ImportFile(object):
    def setupUi(self, wg_ImportFile):
        wg_ImportFile.setObjectName("wg_ImportFile")
        wg_ImportFile.resize(340, 397)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_ImportFile.sizePolicy().hasHeightForWidth())
        wg_ImportFile.setSizePolicy(sizePolicy)
        wg_ImportFile.setMinimumSize(QtCore.QSize(340, 0))
        wg_ImportFile.setMaximumSize(QtCore.QSize(340, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(wg_ImportFile)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(wg_ImportFile)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 18, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_name = QtWidgets.QLabel(self.widget_4)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_2.addWidget(self.l_name)
        self.e_name = QtWidgets.QLineEdit(self.widget_4)
        self.e_name.setMinimumSize(QtCore.QSize(0, 0))
        self.e_name.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.e_name.setObjectName("e_name")
        self.horizontalLayout_2.addWidget(self.e_name)
        self.l_class = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_class.setFont(font)
        self.l_class.setObjectName("l_class")
        self.horizontalLayout_2.addWidget(self.l_class)
        self.verticalLayout.addWidget(self.widget_4)
        self.gb_import = QtWidgets.QGroupBox(wg_ImportFile)
        self.gb_import.setObjectName("gb_import")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_import)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.gb_import)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_file = QtWidgets.QLabel(self.widget)
        self.l_file.setObjectName("l_file")
        self.horizontalLayout.addWidget(self.l_file)
        self.e_file = QtWidgets.QLineEdit(self.widget)
        self.e_file.setReadOnly(False)
        self.e_file.setObjectName("e_file")
        self.horizontalLayout.addWidget(self.e_file)
        self.b_browse = QtWidgets.QPushButton(self.widget)
        self.b_browse.setMinimumSize(QtCore.QSize(22, 0))
        self.b_browse.setMaximumSize(QtCore.QSize(22, 16777215))
        self.b_browse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_browse.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browse.setObjectName("b_browse")
        self.horizontalLayout.addWidget(self.b_browse)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.gb_import)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.l_status = QtWidgets.QLabel(self.widget_3)
        self.l_status.setAlignment(QtCore.Qt.AlignCenter)
        self.l_status.setObjectName("l_status")
        self.horizontalLayout_4.addWidget(self.l_status)
        self.b_goTo = QtWidgets.QPushButton(self.widget_3)
        self.b_goTo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_goTo.setObjectName("b_goTo")
        self.horizontalLayout_4.addWidget(self.b_goTo)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.gb_import)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_import = QtWidgets.QPushButton(self.widget_2)
        self.b_import.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_import.setObjectName("b_import")
        self.horizontalLayout_3.addWidget(self.b_import)
        self.b_objMerge = QtWidgets.QPushButton(self.widget_2)
        self.b_objMerge.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_objMerge.setObjectName("b_objMerge")
        self.horizontalLayout_3.addWidget(self.b_objMerge)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.groupBox = QtWidgets.QGroupBox(self.gb_import)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.groupBox)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.l_curVersion = QtWidgets.QLabel(self.widget_5)
        self.l_curVersion.setObjectName("l_curVersion")
        self.horizontalLayout_5.addWidget(self.l_curVersion)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.groupBox)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.l_latestVersion = QtWidgets.QLabel(self.widget_6)
        self.l_latestVersion.setObjectName("l_latestVersion")
        self.horizontalLayout_6.addWidget(self.l_latestVersion)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.groupBox)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.b_importLatest = QtWidgets.QPushButton(self.widget_7)
        self.b_importLatest.setMinimumSize(QtCore.QSize(0, 0))
        self.b_importLatest.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.b_importLatest.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_importLatest.setObjectName("b_importLatest")
        self.horizontalLayout_7.addWidget(self.b_importLatest)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gb_options = QtWidgets.QGroupBox(self.gb_import)
        self.gb_options.setObjectName("gb_options")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gb_options)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.f_updateOnly = QtWidgets.QWidget(self.gb_options)
        self.f_updateOnly.setObjectName("f_updateOnly")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.f_updateOnly)
        self.horizontalLayout_16.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.l_updateOnly = QtWidgets.QLabel(self.f_updateOnly)
        self.l_updateOnly.setObjectName("l_updateOnly")
        self.horizontalLayout_16.addWidget(self.l_updateOnly)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.chb_updateOnly = QtWidgets.QCheckBox(self.f_updateOnly)
        self.chb_updateOnly.setText("")
        self.chb_updateOnly.setChecked(True)
        self.chb_updateOnly.setObjectName("chb_updateOnly")
        self.horizontalLayout_16.addWidget(self.chb_updateOnly)
        self.verticalLayout_6.addWidget(self.f_updateOnly)
        self.f_nameSpaces = QtWidgets.QWidget(self.gb_options)
        self.f_nameSpaces.setObjectName("f_nameSpaces")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.f_nameSpaces)
        self.horizontalLayout_12.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.l_keepRefEdits_2 = QtWidgets.QLabel(self.f_nameSpaces)
        self.l_keepRefEdits_2.setObjectName("l_keepRefEdits_2")
        self.horizontalLayout_12.addWidget(self.l_keepRefEdits_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.chb_autoNameSpaces = QtWidgets.QCheckBox(self.f_nameSpaces)
        self.chb_autoNameSpaces.setChecked(False)
        self.chb_autoNameSpaces.setObjectName("chb_autoNameSpaces")
        self.horizontalLayout_12.addWidget(self.chb_autoNameSpaces)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.b_nameSpaces = QtWidgets.QPushButton(self.f_nameSpaces)
        self.b_nameSpaces.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_nameSpaces.setObjectName("b_nameSpaces")
        self.horizontalLayout_12.addWidget(self.b_nameSpaces)
        self.verticalLayout_6.addWidget(self.f_nameSpaces)
        self.f_unitConversion = QtWidgets.QWidget(self.gb_options)
        self.f_unitConversion.setObjectName("f_unitConversion")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.f_unitConversion)
        self.horizontalLayout_13.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.l_keepRefEdits_3 = QtWidgets.QLabel(self.f_unitConversion)
        self.l_keepRefEdits_3.setObjectName("l_keepRefEdits_3")
        self.horizontalLayout_13.addWidget(self.l_keepRefEdits_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.b_unitConversion = QtWidgets.QPushButton(self.f_unitConversion)
        self.b_unitConversion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_unitConversion.setObjectName("b_unitConversion")
        self.horizontalLayout_13.addWidget(self.b_unitConversion)
        self.verticalLayout_6.addWidget(self.f_unitConversion)
        self.w_preferUnit = QtWidgets.QWidget(self.gb_options)
        self.w_preferUnit.setObjectName("w_preferUnit")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.w_preferUnit)
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.l_preferUnit = QtWidgets.QLabel(self.w_preferUnit)
        self.l_preferUnit.setObjectName("l_preferUnit")
        self.horizontalLayout_8.addWidget(self.l_preferUnit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.chb_preferUnit = QtWidgets.QCheckBox(self.w_preferUnit)
        self.chb_preferUnit.setText("")
        self.chb_preferUnit.setObjectName("chb_preferUnit")
        self.horizontalLayout_8.addWidget(self.chb_preferUnit)
        self.verticalLayout_6.addWidget(self.w_preferUnit)
        self.verticalLayout_2.addWidget(self.gb_options)
        self.verticalLayout.addWidget(self.gb_import)

        self.retranslateUi(wg_ImportFile)
        QtCore.QMetaObject.connectSlotsByName(wg_ImportFile)

    def retranslateUi(self, wg_ImportFile):
        wg_ImportFile.setWindowTitle(QtWidgets.QApplication.translate("wg_ImportFile", "ImportFile", None, -1))
        self.l_name.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Name:", None, -1))
        self.l_class.setText(QtWidgets.QApplication.translate("wg_ImportFile", "ImportFile", None, -1))
        self.gb_import.setTitle(QtWidgets.QApplication.translate("wg_ImportFile", "Import", None, -1))
        self.l_file.setText(QtWidgets.QApplication.translate("wg_ImportFile", "File:", None, -1))
        self.b_browse.setText(QtWidgets.QApplication.translate("wg_ImportFile", "...", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Status:", None, -1))
        self.l_status.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Not found in scene", None, -1))
        self.b_goTo.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Go to Node", None, -1))
        self.b_import.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Import", None, -1))
        self.b_objMerge.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Create Obj Merge", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("wg_ImportFile", "Version", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Current Version:", None, -1))
        self.l_curVersion.setText(QtWidgets.QApplication.translate("wg_ImportFile", "-", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Latest Version:", None, -1))
        self.l_latestVersion.setText(QtWidgets.QApplication.translate("wg_ImportFile", "-", None, -1))
        self.b_importLatest.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Import latest Version", None, -1))
        self.gb_options.setTitle(QtWidgets.QApplication.translate("wg_ImportFile", "Options", None, -1))
        self.l_updateOnly.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Update path only:", None, -1))
        self.l_keepRefEdits_2.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Maya Namespaces:", None, -1))
        self.chb_autoNameSpaces.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Auto", None, -1))
        self.b_nameSpaces.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Remove", None, -1))
        self.l_keepRefEdits_3.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Unit conversion:", None, -1))
        self.b_unitConversion.setText(QtWidgets.QApplication.translate("wg_ImportFile", "cm -> m", None, -1))
        self.l_preferUnit.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Prefer versions in centimeter:", None, -1))

