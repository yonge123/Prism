# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrismSettings.ui'
#
# Created: Wed Sep 26 22:49:48 2018
#      by: pyside2-uic @pyside_tools_VERSION@ running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlg_PrismSettings(object):
    def setupUi(self, dlg_PrismSettings):
        dlg_PrismSettings.setObjectName("dlg_PrismSettings")
        dlg_PrismSettings.resize(843, 738)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlg_PrismSettings)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(dlg_PrismSettings)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 841, 736))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tw_settings = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tw_settings.setObjectName("tw_settings")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(self.tabWidgetPage1)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l_abbreviation = QtWidgets.QLabel(self.widget)
        self.l_abbreviation.setText("")
        self.l_abbreviation.setObjectName("l_abbreviation")
        self.gridLayout_2.addWidget(self.l_abbreviation, 2, 2, 1, 1)
        self.e_lname = QtWidgets.QLineEdit(self.widget)
        self.e_lname.setObjectName("e_lname")
        self.gridLayout_2.addWidget(self.e_lname, 1, 2, 1, 1)
        self.l_fname = QtWidgets.QLabel(self.widget)
        self.l_fname.setObjectName("l_fname")
        self.gridLayout_2.addWidget(self.l_fname, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.l_lname = QtWidgets.QLabel(self.widget)
        self.l_lname.setObjectName("l_lname")
        self.gridLayout_2.addWidget(self.l_lname, 1, 0, 1, 1)
        self.e_fname = QtWidgets.QLineEdit(self.widget)
        self.e_fname.setObjectName("e_fname")
        self.gridLayout_2.addWidget(self.e_fname, 0, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.tw_settings.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.w_curPrj = QtWidgets.QGroupBox(self.tabWidgetPage2)
        self.w_curPrj.setObjectName("w_curPrj")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.w_curPrj)
        self.verticalLayout_6.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.l_projectName = QtWidgets.QLabel(self.w_curPrj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_projectName.sizePolicy().hasHeightForWidth())
        self.l_projectName.setSizePolicy(sizePolicy)
        self.l_projectName.setText("")
        self.l_projectName.setObjectName("l_projectName")
        self.verticalLayout_6.addWidget(self.l_projectName)
        self.l_projectPath = QtWidgets.QLabel(self.w_curPrj)
        self.l_projectPath.setText("")
        self.l_projectPath.setObjectName("l_projectPath")
        self.verticalLayout_6.addWidget(self.l_projectPath)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.l_localPath = QtWidgets.QLabel(self.w_curPrj)
        self.l_localPath.setObjectName("l_localPath")
        self.verticalLayout_6.addWidget(self.l_localPath)
        self.widget_3 = QtWidgets.QWidget(self.w_curPrj)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.e_localPath = QtWidgets.QLineEdit(self.widget_3)
        self.e_localPath.setObjectName("e_localPath")
        self.horizontalLayout.addWidget(self.e_localPath)
        self.b_browseLocal = QtWidgets.QPushButton(self.widget_3)
        self.b_browseLocal.setMinimumSize(QtCore.QSize(50, 0))
        self.b_browseLocal.setMaximumSize(QtCore.QSize(50, 16777215))
        self.b_browseLocal.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseLocal.setObjectName("b_browseLocal")
        self.horizontalLayout.addWidget(self.b_browseLocal)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.w_resetPrjScripts = QtWidgets.QWidget(self.w_curPrj)
        self.w_resetPrjScripts.setObjectName("w_resetPrjScripts")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.w_resetPrjScripts)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.b_resetPrjScripts = QtWidgets.QPushButton(self.w_resetPrjScripts)
        self.b_resetPrjScripts.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_resetPrjScripts.setObjectName("b_resetPrjScripts")
        self.horizontalLayout_2.addWidget(self.b_resetPrjScripts)
        self.verticalLayout_6.addWidget(self.w_resetPrjScripts)
        self.verticalLayout_8.addWidget(self.w_curPrj)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem3)
        self.widget_2 = QtWidgets.QWidget(self.tabWidgetPage2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8.addWidget(self.widget_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem4)
        self.widget_9 = QtWidgets.QWidget(self.tabWidgetPage2)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8.addWidget(self.widget_9)
        self.w_projects = QtWidgets.QWidget(self.tabWidgetPage2)
        self.w_projects.setObjectName("w_projects")
        self.lo_projects = QtWidgets.QVBoxLayout(self.w_projects)
        self.lo_projects.setContentsMargins(0, 0, 0, 0)
        self.lo_projects.setContentsMargins(0, 0, 0, 0)
        self.lo_projects.setObjectName("lo_projects")
        self.verticalLayout_8.addWidget(self.w_projects)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.tw_settings.addTab(self.tabWidgetPage2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.w_prjSettings = QtWidgets.QWidget(self.tab)
        self.w_prjSettings.setEnabled(True)
        self.w_prjSettings.setObjectName("w_prjSettings")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.w_prjSettings)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem6)
        self.widget_5 = QtWidgets.QWidget(self.w_prjSettings)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.e_curPname = QtWidgets.QLineEdit(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e_curPname.sizePolicy().hasHeightForWidth())
        self.e_curPname.setSizePolicy(sizePolicy)
        self.e_curPname.setObjectName("e_curPname")
        self.gridLayout.addWidget(self.e_curPname, 0, 2, 1, 1)
        self.l_curPname = QtWidgets.QLabel(self.widget_5)
        self.l_curPname.setObjectName("l_curPname")
        self.gridLayout.addWidget(self.l_curPname, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_5)
        self.widget_10 = QtWidgets.QWidget(self.w_prjSettings)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_10)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.chb_curPuseLocal = QtWidgets.QCheckBox(self.widget_10)
        self.chb_curPuseLocal.setText("")
        self.chb_curPuseLocal.setChecked(True)
        self.chb_curPuseLocal.setObjectName("chb_curPuseLocal")
        self.horizontalLayout_5.addWidget(self.chb_curPuseLocal)
        self.verticalLayout_9.addWidget(self.widget_10)
        self.w_curPfps = QtWidgets.QWidget(self.w_prjSettings)
        self.w_curPfps.setObjectName("w_curPfps")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.w_curPfps)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.w_curPfps)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.chb_curPuseFps = QtWidgets.QCheckBox(self.w_curPfps)
        self.chb_curPuseFps.setText("")
        self.chb_curPuseFps.setChecked(False)
        self.chb_curPuseFps.setObjectName("chb_curPuseFps")
        self.horizontalLayout_6.addWidget(self.chb_curPuseFps)
        self.sp_curPfps = QtWidgets.QDoubleSpinBox(self.w_curPfps)
        self.sp_curPfps.setMinimumSize(QtCore.QSize(60, 0))
        self.sp_curPfps.setMinimum(1.0)
        self.sp_curPfps.setMaximum(9999.99)
        self.sp_curPfps.setProperty("value", 24.0)
        self.sp_curPfps.setObjectName("sp_curPfps")
        self.horizontalLayout_6.addWidget(self.sp_curPfps)
        self.verticalLayout_9.addWidget(self.w_curPfps)
        self.gb_curPversions = QtWidgets.QGroupBox(self.w_prjSettings)
        self.gb_curPversions.setCheckable(True)
        self.gb_curPversions.setChecked(False)
        self.gb_curPversions.setObjectName("gb_curPversions")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.gb_curPversions)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.w_versions = QtWidgets.QWidget(self.gb_curPversions)
        self.w_versions.setObjectName("w_versions")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.w_versions)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_11.addWidget(self.w_versions)
        self.verticalLayout_9.addWidget(self.gb_curPversions)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.verticalLayout_13.addWidget(self.w_prjSettings)
        self.tw_settings.addTab(self.tab, "")
        self.tab_dccApps = QtWidgets.QWidget()
        self.tab_dccApps.setObjectName("tab_dccApps")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.tab_dccApps)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.widget_23 = QtWidgets.QWidget(self.tab_dccApps)
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.widget_23)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_24.addWidget(self.widget_23)
        self.tw_settings.addTab(self.tab_dccApps, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabWidgetPage4)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_17 = QtWidgets.QWidget(self.tabWidgetPage4)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_16.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.b_about = QtWidgets.QPushButton(self.widget_17)
        self.b_about.setObjectName("b_about")
        self.horizontalLayout_16.addWidget(self.b_about)
        spacerItem11 = QtWidgets.QSpacerItem(457, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.verticalLayout_3.addWidget(self.widget_17)
        self.chb_autosave = QtWidgets.QCheckBox(self.tabWidgetPage4)
        self.chb_autosave.setChecked(True)
        self.chb_autosave.setObjectName("chb_autosave")
        self.verticalLayout_3.addWidget(self.chb_autosave)
        self.chb_browserStartup = QtWidgets.QCheckBox(self.tabWidgetPage4)
        self.chb_browserStartup.setChecked(True)
        self.chb_browserStartup.setObjectName("chb_browserStartup")
        self.verticalLayout_3.addWidget(self.chb_browserStartup)
        self.chb_trayStartup = QtWidgets.QCheckBox(self.tabWidgetPage4)
        self.chb_trayStartup.setChecked(True)
        self.chb_trayStartup.setObjectName("chb_trayStartup")
        self.verticalLayout_3.addWidget(self.chb_trayStartup)
        self.w_startTray = QtWidgets.QWidget(self.tabWidgetPage4)
        self.w_startTray.setObjectName("w_startTray")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.w_startTray)
        self.horizontalLayout_7.setContentsMargins(17, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.b_startTray = QtWidgets.QPushButton(self.w_startTray)
        self.b_startTray.setMinimumSize(QtCore.QSize(150, 0))
        self.b_startTray.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.b_startTray.setObjectName("b_startTray")
        self.horizontalLayout_7.addWidget(self.b_startTray)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_3.addWidget(self.w_startTray)
        self.chb_highDPI = QtWidgets.QCheckBox(self.tabWidgetPage4)
        self.chb_highDPI.setObjectName("chb_highDPI")
        self.verticalLayout_3.addWidget(self.chb_highDPI)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabWidgetPage4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_15.addWidget(self.label_10)
        self.widget_7 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.e_rvPath = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.e_rvPath.setFont(font)
        self.e_rvPath.setObjectName("e_rvPath")
        self.horizontalLayout_3.addWidget(self.e_rvPath)
        self.b_browseRV = QtWidgets.QPushButton(self.widget_7)
        self.b_browseRV.setMinimumSize(QtCore.QSize(50, 0))
        self.b_browseRV.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.b_browseRV.setFont(font)
        self.b_browseRV.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseRV.setObjectName("b_browseRV")
        self.horizontalLayout_3.addWidget(self.b_browseRV)
        self.verticalLayout_15.addWidget(self.widget_7)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_15.addWidget(self.label_11)
        self.widget_19 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.e_djvPath = QtWidgets.QLineEdit(self.widget_19)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.e_djvPath.setFont(font)
        self.e_djvPath.setObjectName("e_djvPath")
        self.horizontalLayout_9.addWidget(self.e_djvPath)
        self.b_browseDJV = QtWidgets.QPushButton(self.widget_19)
        self.b_browseDJV.setMinimumSize(QtCore.QSize(50, 0))
        self.b_browseDJV.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.b_browseDJV.setFont(font)
        self.b_browseDJV.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseDJV.setObjectName("b_browseDJV")
        self.horizontalLayout_9.addWidget(self.b_browseDJV)
        self.verticalLayout_15.addWidget(self.widget_19)
        self.chb_preferDJV = QtWidgets.QCheckBox(self.groupBox_2)
        self.chb_preferDJV.setObjectName("chb_preferDJV")
        self.verticalLayout_15.addWidget(self.chb_preferDJV)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.tw_settings.addTab(self.tabWidgetPage4, "")
        self.verticalLayout_5.addWidget(self.tw_settings)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(dlg_PrismSettings)
        self.tw_settings.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlg_PrismSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlg_PrismSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_PrismSettings)
        dlg_PrismSettings.setTabOrder(self.scrollArea, self.tw_settings)
        dlg_PrismSettings.setTabOrder(self.tw_settings, self.e_fname)
        dlg_PrismSettings.setTabOrder(self.e_fname, self.e_lname)
        dlg_PrismSettings.setTabOrder(self.e_lname, self.e_localPath)
        dlg_PrismSettings.setTabOrder(self.e_localPath, self.b_browseLocal)
        dlg_PrismSettings.setTabOrder(self.b_browseLocal, self.e_curPname)
        dlg_PrismSettings.setTabOrder(self.e_curPname, self.chb_curPuseLocal)
        dlg_PrismSettings.setTabOrder(self.chb_curPuseLocal, self.chb_curPuseFps)
        dlg_PrismSettings.setTabOrder(self.chb_curPuseFps, self.sp_curPfps)
        dlg_PrismSettings.setTabOrder(self.sp_curPfps, self.gb_curPversions)
        dlg_PrismSettings.setTabOrder(self.gb_curPversions, self.b_about)
        dlg_PrismSettings.setTabOrder(self.b_about, self.chb_autosave)
        dlg_PrismSettings.setTabOrder(self.chb_autosave, self.chb_browserStartup)
        dlg_PrismSettings.setTabOrder(self.chb_browserStartup, self.chb_trayStartup)
        dlg_PrismSettings.setTabOrder(self.chb_trayStartup, self.b_startTray)
        dlg_PrismSettings.setTabOrder(self.b_startTray, self.e_rvPath)
        dlg_PrismSettings.setTabOrder(self.e_rvPath, self.b_browseRV)
        dlg_PrismSettings.setTabOrder(self.b_browseRV, self.e_djvPath)
        dlg_PrismSettings.setTabOrder(self.e_djvPath, self.b_browseDJV)
        dlg_PrismSettings.setTabOrder(self.b_browseDJV, self.chb_preferDJV)
        dlg_PrismSettings.setTabOrder(self.chb_preferDJV, self.buttonBox)

    def retranslateUi(self, dlg_PrismSettings):
        dlg_PrismSettings.setWindowTitle(QtWidgets.QApplication.translate("dlg_PrismSettings", "Prism Settings", None, -1))
        self.l_fname.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "First Name:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Abbreviation:    ", None, -1))
        self.l_lname.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Last Name:", None, -1))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tabWidgetPage1), QtWidgets.QApplication.translate("dlg_PrismSettings", "User", None, -1))
        self.w_curPrj.setTitle(QtWidgets.QApplication.translate("dlg_PrismSettings", "Current Project", None, -1))
        self.l_projectName.setToolTip(QtWidgets.QApplication.translate("dlg_PrismSettings", "current project", None, -1))
        self.l_projectPath.setToolTip(QtWidgets.QApplication.translate("dlg_PrismSettings", "current project path", None, -1))
        self.l_localPath.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Local path:", None, -1))
        self.b_browseLocal.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "...", None, -1))
        self.b_resetPrjScripts.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Reset project scripts", None, -1))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tabWidgetPage2), QtWidgets.QApplication.translate("dlg_PrismSettings", "Project", None, -1))
        self.l_curPname.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Project Name:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Use additional local project folder:", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Force FPS in scenefiles:", None, -1))
        self.gb_curPversions.setTitle(QtWidgets.QApplication.translate("dlg_PrismSettings", "Force program versions", None, -1))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab), QtWidgets.QApplication.translate("dlg_PrismSettings", "Project Settings", None, -1))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_dccApps), QtWidgets.QApplication.translate("dlg_PrismSettings", "DCC apps", None, -1))
        self.b_about.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "About", None, -1))
        self.chb_autosave.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Autosave popup", None, -1))
        self.chb_browserStartup.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Open Project Browser on application startup", None, -1))
        self.chb_trayStartup.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Show Prism tray icon on system startup", None, -1))
        self.b_startTray.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "Start Prism tray now", None, -1))
        self.chb_highDPI.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "HighDPI support (requires complete application restart) (experimental)", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("dlg_PrismSettings", "Image player", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "RV path:", None, -1))
        self.b_browseRV.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "...", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "DJV path:", None, -1))
        self.b_browseDJV.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "...", None, -1))
        self.chb_preferDJV.setText(QtWidgets.QApplication.translate("dlg_PrismSettings", "prefer DJV", None, -1))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tabWidgetPage4), QtWidgets.QApplication.translate("dlg_PrismSettings", "Miscellaneous", None, -1))
