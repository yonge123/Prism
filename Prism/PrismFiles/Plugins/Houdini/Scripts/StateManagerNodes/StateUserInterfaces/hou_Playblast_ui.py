# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hou_Playblast.ui'
#
# Created: Sun Aug 12 21:12:40 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_wg_Playblast(object):
    def setupUi(self, wg_Playblast):
        wg_Playblast.setObjectName("wg_Playblast")
        wg_Playblast.resize(340, 296)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_Playblast.sizePolicy().hasHeightForWidth())
        wg_Playblast.setSizePolicy(sizePolicy)
        wg_Playblast.setMinimumSize(QtCore.QSize(340, 0))
        wg_Playblast.setMaximumSize(QtCore.QSize(340, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(wg_Playblast)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtGui.QWidget(wg_Playblast)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(-1, 0, 18, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l_name = QtGui.QLabel(self.widget_4)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_4.addWidget(self.l_name)
        self.e_name = QtGui.QLineEdit(self.widget_4)
        self.e_name.setObjectName("e_name")
        self.horizontalLayout_4.addWidget(self.e_name)
        self.l_class = QtGui.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_class.setFont(font)
        self.l_class.setObjectName("l_class")
        self.horizontalLayout_4.addWidget(self.l_class)
        self.verticalLayout.addWidget(self.widget_4)
        self.groupBox = QtGui.QGroupBox(wg_Playblast)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_10 = QtGui.QWidget(self.groupBox)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtGui.QLabel(self.widget_10)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.l_taskName = QtGui.QLabel(self.widget_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_taskName.sizePolicy().hasHeightForWidth())
        self.l_taskName.setSizePolicy(sizePolicy)
        self.l_taskName.setText("")
        self.l_taskName.setAlignment(QtCore.Qt.AlignCenter)
        self.l_taskName.setObjectName("l_taskName")
        self.horizontalLayout_10.addWidget(self.l_taskName)
        self.b_changeTask = QtGui.QPushButton(self.widget_10)
        self.b_changeTask.setEnabled(True)
        self.b_changeTask.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_changeTask.setObjectName("b_changeTask")
        self.horizontalLayout_10.addWidget(self.b_changeTask)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.chb_globalRange = QtGui.QCheckBox(self.widget_2)
        self.chb_globalRange.setChecked(True)
        self.chb_globalRange.setObjectName("chb_globalRange")
        self.horizontalLayout.addWidget(self.chb_globalRange)
        self.sp_rangeStart = QtGui.QSpinBox(self.widget_2)
        self.sp_rangeStart.setEnabled(False)
        self.sp_rangeStart.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeStart.setMaximum(99999)
        self.sp_rangeStart.setObjectName("sp_rangeStart")
        self.horizontalLayout.addWidget(self.sp_rangeStart)
        spacerItem1 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.l_rangeEnd = QtGui.QLabel(self.widget_2)
        self.l_rangeEnd.setEnabled(False)
        self.l_rangeEnd.setObjectName("l_rangeEnd")
        self.horizontalLayout.addWidget(self.l_rangeEnd)
        self.sp_rangeEnd = QtGui.QSpinBox(self.widget_2)
        self.sp_rangeEnd.setEnabled(False)
        self.sp_rangeEnd.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeEnd.setMaximum(99999)
        self.sp_rangeEnd.setProperty("value", 100)
        self.sp_rangeEnd.setObjectName("sp_rangeEnd")
        self.horizontalLayout.addWidget(self.sp_rangeEnd)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cb_cams = QtGui.QComboBox(self.widget)
        self.cb_cams.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_cams.setObjectName("cb_cams")
        self.horizontalLayout_2.addWidget(self.cb_cams)
        self.verticalLayout_2.addWidget(self.widget)
        self.f_resolution = QtGui.QWidget(self.groupBox)
        self.f_resolution.setObjectName("f_resolution")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.f_resolution)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtGui.QLabel(self.f_resolution)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.chb_resOverride = QtGui.QCheckBox(self.f_resolution)
        self.chb_resOverride.setText("")
        self.chb_resOverride.setChecked(True)
        self.chb_resOverride.setObjectName("chb_resOverride")
        self.horizontalLayout_9.addWidget(self.chb_resOverride)
        self.sp_resWidth = QtGui.QSpinBox(self.f_resolution)
        self.sp_resWidth.setEnabled(True)
        self.sp_resWidth.setMinimum(1)
        self.sp_resWidth.setMaximum(99999)
        self.sp_resWidth.setProperty("value", 1280)
        self.sp_resWidth.setObjectName("sp_resWidth")
        self.horizontalLayout_9.addWidget(self.sp_resWidth)
        self.sp_resHeight = QtGui.QSpinBox(self.f_resolution)
        self.sp_resHeight.setEnabled(True)
        self.sp_resHeight.setMinimum(1)
        self.sp_resHeight.setMaximum(99999)
        self.sp_resHeight.setProperty("value", 720)
        self.sp_resHeight.setObjectName("sp_resHeight")
        self.horizontalLayout_9.addWidget(self.sp_resHeight)
        self.b_resPresets = QtGui.QPushButton(self.f_resolution)
        self.b_resPresets.setEnabled(True)
        self.b_resPresets.setMinimumSize(QtCore.QSize(23, 23))
        self.b_resPresets.setMaximumSize(QtCore.QSize(23, 23))
        self.b_resPresets.setObjectName("b_resPresets")
        self.horizontalLayout_9.addWidget(self.b_resPresets)
        self.verticalLayout_2.addWidget(self.f_resolution)
        self.f_displayMode = QtGui.QWidget(self.groupBox)
        self.f_displayMode.setObjectName("f_displayMode")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.f_displayMode)
        self.horizontalLayout_11.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtGui.QLabel(self.f_displayMode)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.cb_displayMode = QtGui.QComboBox(self.f_displayMode)
        self.cb_displayMode.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_displayMode.setObjectName("cb_displayMode")
        self.horizontalLayout_11.addWidget(self.cb_displayMode)
        self.verticalLayout_2.addWidget(self.f_displayMode)
        self.f_localOutput = QtGui.QWidget(self.groupBox)
        self.f_localOutput.setObjectName("f_localOutput")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.f_localOutput)
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.l_localOutput = QtGui.QLabel(self.f_localOutput)
        self.l_localOutput.setObjectName("l_localOutput")
        self.horizontalLayout_16.addWidget(self.l_localOutput)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.chb_localOutput = QtGui.QCheckBox(self.f_localOutput)
        self.chb_localOutput.setText("")
        self.chb_localOutput.setChecked(True)
        self.chb_localOutput.setObjectName("chb_localOutput")
        self.horizontalLayout_16.addWidget(self.chb_localOutput)
        self.verticalLayout_2.addWidget(self.f_localOutput)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(wg_Playblast)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(18, -1, 18, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_pathLast = QtGui.QLabel(self.groupBox_3)
        self.l_pathLast.setObjectName("l_pathLast")
        self.verticalLayout_4.addWidget(self.l_pathLast)
        self.widget_21 = QtGui.QWidget(self.groupBox_3)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.widget_21)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.b_openLast = QtGui.QPushButton(self.widget_21)
        self.b_openLast.setEnabled(False)
        self.b_openLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_openLast.setObjectName("b_openLast")
        self.horizontalLayout_19.addWidget(self.b_openLast)
        self.b_copyLast = QtGui.QPushButton(self.widget_21)
        self.b_copyLast.setEnabled(False)
        self.b_copyLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_copyLast.setObjectName("b_copyLast")
        self.horizontalLayout_19.addWidget(self.b_copyLast)
        self.verticalLayout_4.addWidget(self.widget_21)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(wg_Playblast)
        QtCore.QMetaObject.connectSlotsByName(wg_Playblast)

    def retranslateUi(self, wg_Playblast):
        wg_Playblast.setWindowTitle(QtGui.QApplication.translate("wg_Playblast", "Playblast", None, QtGui.QApplication.UnicodeUTF8))
        self.l_name.setText(QtGui.QApplication.translate("wg_Playblast", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_class.setText(QtGui.QApplication.translate("wg_Playblast", "Playblast", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("wg_Playblast", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("wg_Playblast", "Taskname:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_changeTask.setText(QtGui.QApplication.translate("wg_Playblast", "change", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("wg_Playblast", "Framerange:", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_globalRange.setText(QtGui.QApplication.translate("wg_Playblast", "global", None, QtGui.QApplication.UnicodeUTF8))
        self.l_rangeEnd.setText(QtGui.QApplication.translate("wg_Playblast", "to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("wg_Playblast", "Camera:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("wg_Playblast", "Resolution override:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_resPresets.setText(QtGui.QApplication.translate("wg_Playblast", "▼", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("wg_Playblast", "Display mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_localOutput.setText(QtGui.QApplication.translate("wg_Playblast", "Local output:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("wg_Playblast", "Last playblast", None, QtGui.QApplication.UnicodeUTF8))
        self.l_pathLast.setText(QtGui.QApplication.translate("wg_Playblast", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.b_openLast.setText(QtGui.QApplication.translate("wg_Playblast", "Open in explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.b_copyLast.setText(QtGui.QApplication.translate("wg_Playblast", "Copy path to clipboard", None, QtGui.QApplication.UnicodeUTF8))

