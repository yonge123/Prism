# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateProject.ui'
#
# Created: Thu Jul 12 20:01:56 2018
#      by: pyside2-uic @pyside_tools_VERSION@ running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlg_createProject(object):
    def setupUi(self, dlg_createProject):
        dlg_createProject.setObjectName("dlg_createProject")
        dlg_createProject.resize(726, 438)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(dlg_createProject)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.scrollArea = QtWidgets.QScrollArea(dlg_createProject)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 724, 436))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_32 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_32.setObjectName("widget_32")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_32)
        self.verticalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(self.widget_32)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.e_path = QtWidgets.QLineEdit(self.widget)
        self.e_path.setObjectName("e_path")
        self.gridLayout.addWidget(self.e_path, 1, 1, 1, 1)
        self.e_name = QtWidgets.QLineEdit(self.widget)
        self.e_name.setObjectName("e_name")
        self.gridLayout.addWidget(self.e_name, 0, 1, 1, 1)
        self.l_path = QtWidgets.QLabel(self.widget)
        self.l_path.setObjectName("l_path")
        self.gridLayout.addWidget(self.l_path, 1, 0, 1, 1)
        self.l_name = QtWidgets.QLabel(self.widget)
        self.l_name.setObjectName("l_name")
        self.gridLayout.addWidget(self.l_name, 0, 0, 1, 1)
        self.b_browse = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_browse.sizePolicy().hasHeightForWidth())
        self.b_browse.setSizePolicy(sizePolicy)
        self.b_browse.setMinimumSize(QtCore.QSize(40, 0))
        self.b_browse.setMaximumSize(QtCore.QSize(40, 16777215))
        self.b_browse.setObjectName("b_browse")
        self.gridLayout.addWidget(self.b_browse, 1, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.widget)
        self.gb_folderStructure = QtWidgets.QGroupBox(self.widget_32)
        self.gb_folderStructure.setMinimumSize(QtCore.QSize(0, 225))
        self.gb_folderStructure.setMaximumSize(QtCore.QSize(16777215, 225))
        self.gb_folderStructure.setObjectName("gb_folderStructure")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.gb_folderStructure)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tw_dirStruct = QtWidgets.QTreeView(self.gb_folderStructure)
        self.tw_dirStruct.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.tw_dirStruct.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_dirStruct.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tw_dirStruct.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tw_dirStruct.setExpandsOnDoubleClick(False)
        self.tw_dirStruct.setObjectName("tw_dirStruct")
        self.horizontalLayout_3.addWidget(self.tw_dirStruct)
        self.widget_6 = QtWidgets.QWidget(self.gb_folderStructure)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.b_addDir = QtWidgets.QPushButton(self.widget_6)
        self.b_addDir.setObjectName("b_addDir")
        self.verticalLayout_3.addWidget(self.b_addDir)
        self.b_delDir = QtWidgets.QPushButton(self.widget_6)
        self.b_delDir.setObjectName("b_delDir")
        self.verticalLayout_3.addWidget(self.b_delDir)
        self.b_upDir = QtWidgets.QPushButton(self.widget_6)
        self.b_upDir.setObjectName("b_upDir")
        self.verticalLayout_3.addWidget(self.b_upDir)
        self.b_downDir = QtWidgets.QPushButton(self.widget_6)
        self.b_downDir.setObjectName("b_downDir")
        self.verticalLayout_3.addWidget(self.b_downDir)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.verticalLayout_6.addWidget(self.gb_folderStructure)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget_32)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.b_create = QtWidgets.QPushButton(self.widget_32)
        self.b_create.setMinimumSize(QtCore.QSize(0, 40))
        self.b_create.setObjectName("b_create")
        self.verticalLayout_6.addWidget(self.b_create)
        self.horizontalLayout_13.addWidget(self.widget_32)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.addWidget(self.scrollArea)

        self.retranslateUi(dlg_createProject)
        QtCore.QMetaObject.connectSlotsByName(dlg_createProject)
        dlg_createProject.setTabOrder(self.scrollArea, self.e_name)
        dlg_createProject.setTabOrder(self.e_name, self.e_path)
        dlg_createProject.setTabOrder(self.e_path, self.b_browse)
        dlg_createProject.setTabOrder(self.b_browse, self.tw_dirStruct)
        dlg_createProject.setTabOrder(self.tw_dirStruct, self.b_addDir)
        dlg_createProject.setTabOrder(self.b_addDir, self.b_delDir)
        dlg_createProject.setTabOrder(self.b_delDir, self.b_upDir)
        dlg_createProject.setTabOrder(self.b_upDir, self.b_downDir)
        dlg_createProject.setTabOrder(self.b_downDir, self.b_create)

    def retranslateUi(self, dlg_createProject):
        dlg_createProject.setWindowTitle(QtWidgets.QApplication.translate("dlg_createProject", "Create Project", None, -1))
        self.l_path.setText(QtWidgets.QApplication.translate("dlg_createProject", "Project Path:", None, -1))
        self.l_name.setText(QtWidgets.QApplication.translate("dlg_createProject", "Project Name:", None, -1))
        self.b_browse.setToolTip(QtWidgets.QApplication.translate("dlg_createProject", "browse", None, -1))
        self.b_browse.setText(QtWidgets.QApplication.translate("dlg_createProject", "...", None, -1))
        self.gb_folderStructure.setTitle(QtWidgets.QApplication.translate("dlg_createProject", "Folder Structure:", None, -1))
        self.b_addDir.setToolTip(QtWidgets.QApplication.translate("dlg_createProject", "adds a new folder to the folder structure", None, -1))
        self.b_addDir.setText(QtWidgets.QApplication.translate("dlg_createProject", "Add", None, -1))
        self.b_delDir.setToolTip(QtWidgets.QApplication.translate("dlg_createProject", "deletes the selected folder from the folder structure", None, -1))
        self.b_delDir.setText(QtWidgets.QApplication.translate("dlg_createProject", "Delete", None, -1))
        self.b_upDir.setToolTip(QtWidgets.QApplication.translate("dlg_createProject", "moves the selected folder up one step", None, -1))
        self.b_upDir.setText(QtWidgets.QApplication.translate("dlg_createProject", "Up", None, -1))
        self.b_downDir.setToolTip(QtWidgets.QApplication.translate("dlg_createProject", "moves the selected folder down one step", None, -1))
        self.b_downDir.setText(QtWidgets.QApplication.translate("dlg_createProject", "Down", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("dlg_createProject", "Additional project settings can be defined later in the \"project settings\" tab of the Prism settings.", None, -1))
        self.b_create.setText(QtWidgets.QApplication.translate("dlg_createProject", "Create Project", None, -1))

