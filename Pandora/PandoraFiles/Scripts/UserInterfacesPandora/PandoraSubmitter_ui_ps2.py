# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PandoraSubmitter.ui'
#
# Created: Wed May 23 17:08:51 2018
#      by: pyside2-uic @pyside_tools_VERSION@ running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlg_pandoraSubmitter(object):
    def setupUi(self, dlg_pandoraSubmitter):
        dlg_pandoraSubmitter.setObjectName("dlg_pandoraSubmitter")
        dlg_pandoraSubmitter.resize(431, 533)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlg_pandoraSubmitter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(dlg_pandoraSubmitter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 411, 513))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.f_range = QtWidgets.QWidget(self.groupBox_2)
        self.f_range.setObjectName("f_range")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.f_range)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_framerange = QtWidgets.QLabel(self.f_range)
        self.l_framerange.setObjectName("l_framerange")
        self.horizontalLayout.addWidget(self.l_framerange)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.l_rangeStart = QtWidgets.QLabel(self.f_range)
        self.l_rangeStart.setEnabled(True)
        self.l_rangeStart.setObjectName("l_rangeStart")
        self.horizontalLayout.addWidget(self.l_rangeStart)
        self.sp_rangeStart = QtWidgets.QSpinBox(self.f_range)
        self.sp_rangeStart.setEnabled(True)
        self.sp_rangeStart.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeStart.setMaximum(99999)
        self.sp_rangeStart.setObjectName("sp_rangeStart")
        self.horizontalLayout.addWidget(self.sp_rangeStart)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.l_rangeEnd = QtWidgets.QLabel(self.f_range)
        self.l_rangeEnd.setEnabled(True)
        self.l_rangeEnd.setObjectName("l_rangeEnd")
        self.horizontalLayout.addWidget(self.l_rangeEnd)
        self.sp_rangeEnd = QtWidgets.QSpinBox(self.f_range)
        self.sp_rangeEnd.setEnabled(True)
        self.sp_rangeEnd.setMaximumSize(QtCore.QSize(55, 16777215))
        self.sp_rangeEnd.setMaximum(99999)
        self.sp_rangeEnd.setProperty("value", 100)
        self.sp_rangeEnd.setObjectName("sp_rangeEnd")
        self.horizontalLayout.addWidget(self.sp_rangeEnd)
        self.verticalLayout_4.addWidget(self.f_range)
        self.f_cam = QtWidgets.QWidget(self.groupBox_2)
        self.f_cam.setObjectName("f_cam")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.f_cam)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_camera = QtWidgets.QLabel(self.f_cam)
        self.l_camera.setObjectName("l_camera")
        self.horizontalLayout_2.addWidget(self.l_camera)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cb_cam = QtWidgets.QComboBox(self.f_cam)
        self.cb_cam.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_cam.setObjectName("cb_cam")
        self.horizontalLayout_2.addWidget(self.cb_cam)
        self.verticalLayout_4.addWidget(self.f_cam)
        self.f_resolution = QtWidgets.QWidget(self.groupBox_2)
        self.f_resolution.setObjectName("f_resolution")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.f_resolution)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.l_resOverride = QtWidgets.QLabel(self.f_resolution)
        self.l_resOverride.setEnabled(True)
        self.l_resOverride.setObjectName("l_resOverride")
        self.horizontalLayout_9.addWidget(self.l_resOverride)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.chb_resOverride = QtWidgets.QCheckBox(self.f_resolution)
        self.chb_resOverride.setText("")
        self.chb_resOverride.setObjectName("chb_resOverride")
        self.horizontalLayout_9.addWidget(self.chb_resOverride)
        self.sp_resWidth = QtWidgets.QSpinBox(self.f_resolution)
        self.sp_resWidth.setEnabled(False)
        self.sp_resWidth.setMinimum(1)
        self.sp_resWidth.setMaximum(99999)
        self.sp_resWidth.setProperty("value", 1280)
        self.sp_resWidth.setObjectName("sp_resWidth")
        self.horizontalLayout_9.addWidget(self.sp_resWidth)
        self.sp_resHeight = QtWidgets.QSpinBox(self.f_resolution)
        self.sp_resHeight.setEnabled(False)
        self.sp_resHeight.setMinimum(1)
        self.sp_resHeight.setMaximum(99999)
        self.sp_resHeight.setProperty("value", 720)
        self.sp_resHeight.setObjectName("sp_resHeight")
        self.horizontalLayout_9.addWidget(self.sp_resHeight)
        self.b_resPresets = QtWidgets.QPushButton(self.f_resolution)
        self.b_resPresets.setEnabled(False)
        self.b_resPresets.setMinimumSize(QtCore.QSize(23, 23))
        self.b_resPresets.setMaximumSize(QtCore.QSize(23, 23))
        self.b_resPresets.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_resPresets.setObjectName("b_resPresets")
        self.horizontalLayout_9.addWidget(self.b_resPresets)
        self.verticalLayout_4.addWidget(self.f_resolution)
        self.gb_outputpath = QtWidgets.QWidget(self.groupBox_2)
        self.gb_outputpath.setObjectName("gb_outputpath")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.gb_outputpath)
        self.horizontalLayout_13.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label = QtWidgets.QLabel(self.gb_outputpath)
        self.label.setObjectName("label")
        self.horizontalLayout_13.addWidget(self.label)
        self.e_outputpath = QtWidgets.QLineEdit(self.gb_outputpath)
        self.e_outputpath.setObjectName("e_outputpath")
        self.horizontalLayout_13.addWidget(self.e_outputpath)
        self.b_browseOutputpath = QtWidgets.QPushButton(self.gb_outputpath)
        self.b_browseOutputpath.setMinimumSize(QtCore.QSize(50, 0))
        self.b_browseOutputpath.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.b_browseOutputpath.setFont(font)
        self.b_browseOutputpath.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_browseOutputpath.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseOutputpath.setObjectName("b_browseOutputpath")
        self.horizontalLayout_13.addWidget(self.b_browseOutputpath)
        self.verticalLayout_4.addWidget(self.gb_outputpath)
        self.w_status = QtWidgets.QWidget(self.groupBox_2)
        self.w_status.setObjectName("w_status")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.w_status)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.l_nodeStatus = QtWidgets.QLabel(self.w_status)
        self.l_nodeStatus.setMinimumSize(QtCore.QSize(40, 0))
        self.l_nodeStatus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.l_nodeStatus.setObjectName("l_nodeStatus")
        self.horizontalLayout_5.addWidget(self.l_nodeStatus)
        self.l_status = QtWidgets.QLabel(self.w_status)
        self.l_status.setAlignment(QtCore.Qt.AlignCenter)
        self.l_status.setObjectName("l_status")
        self.horizontalLayout_5.addWidget(self.l_status)
        self.b_goTo = QtWidgets.QPushButton(self.w_status)
        self.b_goTo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_goTo.setObjectName("b_goTo")
        self.horizontalLayout_5.addWidget(self.b_goTo)
        self.verticalLayout_4.addWidget(self.w_status)
        self.w_connect = QtWidgets.QWidget(self.groupBox_2)
        self.w_connect.setObjectName("w_connect")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.w_connect)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.b_connect = QtWidgets.QPushButton(self.w_connect)
        self.b_connect.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_connect.setObjectName("b_connect")
        self.horizontalLayout_6.addWidget(self.b_connect)
        self.verticalLayout_4.addWidget(self.w_connect)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.f_taskname = QtWidgets.QWidget(self.groupBox)
        self.f_taskname.setObjectName("f_taskname")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.f_taskname)
        self.horizontalLayout_11.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.l_projectName = QtWidgets.QLabel(self.f_taskname)
        self.l_projectName.setObjectName("l_projectName")
        self.horizontalLayout_11.addWidget(self.l_projectName)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.e_projectName = QtWidgets.QLineEdit(self.f_taskname)
        self.e_projectName.setMinimumSize(QtCore.QSize(200, 0))
        self.e_projectName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.e_projectName.setObjectName("e_projectName")
        self.horizontalLayout_11.addWidget(self.e_projectName)
        self.verticalLayout_2.addWidget(self.f_taskname)
        self.w_jobname = QtWidgets.QWidget(self.groupBox)
        self.w_jobname.setObjectName("w_jobname")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.w_jobname)
        self.horizontalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.l_jobName = QtWidgets.QLabel(self.w_jobname)
        self.l_jobName.setObjectName("l_jobName")
        self.horizontalLayout_10.addWidget(self.l_jobName)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.e_jobName = QtWidgets.QLineEdit(self.w_jobname)
        self.e_jobName.setMinimumSize(QtCore.QSize(200, 0))
        self.e_jobName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.e_jobName.setObjectName("e_jobName")
        self.horizontalLayout_10.addWidget(self.e_jobName)
        self.verticalLayout_2.addWidget(self.w_jobname)
        self.f_rjPrio_2 = QtWidgets.QWidget(self.groupBox)
        self.f_rjPrio_2.setObjectName("f_rjPrio_2")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.f_rjPrio_2)
        self.horizontalLayout_25.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.l_prio = QtWidgets.QLabel(self.f_rjPrio_2)
        self.l_prio.setObjectName("l_prio")
        self.horizontalLayout_25.addWidget(self.l_prio)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem6)
        self.sp_priority = QtWidgets.QSpinBox(self.f_rjPrio_2)
        self.sp_priority.setMaximum(100)
        self.sp_priority.setProperty("value", 50)
        self.sp_priority.setObjectName("sp_priority")
        self.horizontalLayout_25.addWidget(self.sp_priority)
        self.verticalLayout_2.addWidget(self.f_rjPrio_2)
        self.f_rjWidgetsPerTask_2 = QtWidgets.QWidget(self.groupBox)
        self.f_rjWidgetsPerTask_2.setObjectName("f_rjWidgetsPerTask_2")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.f_rjWidgetsPerTask_2)
        self.horizontalLayout_30.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.l_framesPerTask = QtWidgets.QLabel(self.f_rjWidgetsPerTask_2)
        self.l_framesPerTask.setObjectName("l_framesPerTask")
        self.horizontalLayout_30.addWidget(self.l_framesPerTask)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem7)
        self.sp_framesPerTask = QtWidgets.QSpinBox(self.f_rjWidgetsPerTask_2)
        self.sp_framesPerTask.setMaximum(9999)
        self.sp_framesPerTask.setProperty("value", 5)
        self.sp_framesPerTask.setObjectName("sp_framesPerTask")
        self.horizontalLayout_30.addWidget(self.sp_framesPerTask)
        self.verticalLayout_2.addWidget(self.f_rjWidgetsPerTask_2)
        self.f_rjTimeout = QtWidgets.QWidget(self.groupBox)
        self.f_rjTimeout.setObjectName("f_rjTimeout")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.f_rjTimeout)
        self.horizontalLayout_31.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.l_rjTimeout = QtWidgets.QLabel(self.f_rjTimeout)
        self.l_rjTimeout.setObjectName("l_rjTimeout")
        self.horizontalLayout_31.addWidget(self.l_rjTimeout)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem8)
        self.sp_rjTimeout = QtWidgets.QSpinBox(self.f_rjTimeout)
        self.sp_rjTimeout.setMinimum(1)
        self.sp_rjTimeout.setMaximum(9999)
        self.sp_rjTimeout.setProperty("value", 180)
        self.sp_rjTimeout.setObjectName("sp_rjTimeout")
        self.horizontalLayout_31.addWidget(self.sp_rjTimeout)
        self.verticalLayout_2.addWidget(self.f_rjTimeout)
        self.f_suspended = QtWidgets.QWidget(self.groupBox)
        self.f_suspended.setObjectName("f_suspended")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.f_suspended)
        self.horizontalLayout_29.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.l_submitSuspended = QtWidgets.QLabel(self.f_suspended)
        self.l_submitSuspended.setObjectName("l_submitSuspended")
        self.horizontalLayout_29.addWidget(self.l_submitSuspended)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem9)
        self.chb_suspended = QtWidgets.QCheckBox(self.f_suspended)
        self.chb_suspended.setText("")
        self.chb_suspended.setChecked(False)
        self.chb_suspended.setObjectName("chb_suspended")
        self.horizontalLayout_29.addWidget(self.chb_suspended)
        self.verticalLayout_2.addWidget(self.f_suspended)
        self.f_osDependencies = QtWidgets.QWidget(self.groupBox)
        self.f_osDependencies.setObjectName("f_osDependencies")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.f_osDependencies)
        self.horizontalLayout_28.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.l_submitDependent = QtWidgets.QLabel(self.f_osDependencies)
        self.l_submitDependent.setObjectName("l_submitDependent")
        self.horizontalLayout_28.addWidget(self.l_submitDependent)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem10)
        self.chb_dependencies = QtWidgets.QCheckBox(self.f_osDependencies)
        self.chb_dependencies.setText("")
        self.chb_dependencies.setChecked(True)
        self.chb_dependencies.setObjectName("chb_dependencies")
        self.horizontalLayout_28.addWidget(self.chb_dependencies)
        self.verticalLayout_2.addWidget(self.f_osDependencies)
        self.f_osUpload = QtWidgets.QWidget(self.groupBox)
        self.f_osUpload.setObjectName("f_osUpload")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.f_osUpload)
        self.horizontalLayout_23.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.l_uploadOutput = QtWidgets.QLabel(self.f_osUpload)
        self.l_uploadOutput.setObjectName("l_uploadOutput")
        self.horizontalLayout_23.addWidget(self.l_uploadOutput)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem11)
        self.chb_uploadOutput = QtWidgets.QCheckBox(self.f_osUpload)
        self.chb_uploadOutput.setText("")
        self.chb_uploadOutput.setChecked(True)
        self.chb_uploadOutput.setObjectName("chb_uploadOutput")
        self.horizontalLayout_23.addWidget(self.chb_uploadOutput)
        self.verticalLayout_2.addWidget(self.f_osUpload)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.b_submit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.b_submit.setObjectName("b_submit")
        self.verticalLayout_3.addWidget(self.b_submit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(dlg_pandoraSubmitter)
        QtCore.QMetaObject.connectSlotsByName(dlg_pandoraSubmitter)

    def retranslateUi(self, dlg_pandoraSubmitter):
        dlg_pandoraSubmitter.setWindowTitle(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Submit Pandora renderjob", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Scene settings", None, -1))
        self.l_framerange.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Framerange:", None, -1))
        self.l_rangeStart.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "from:", None, -1))
        self.l_rangeEnd.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "to:", None, -1))
        self.l_camera.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Camera:", None, -1))
        self.l_resOverride.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Resolution override:", None, -1))
        self.b_resPresets.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "▼", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Outputpath:", None, -1))
        self.b_browseOutputpath.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "...", None, -1))
        self.l_nodeStatus.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Status:", None, -1))
        self.l_status.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Not connected", None, -1))
        self.b_goTo.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Go to Node", None, -1))
        self.b_connect.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Connect with selected render Node", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Job settings", None, -1))
        self.l_projectName.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Projectname:", None, -1))
        self.l_jobName.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Jobname:", None, -1))
        self.l_prio.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Priority:", None, -1))
        self.l_framesPerTask.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Frames per Task:", None, -1))
        self.l_rjTimeout.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Task Timeout (min)", None, -1))
        self.l_submitSuspended.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Submit suspended:", None, -1))
        self.l_submitDependent.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Submit dependent files:", None, -1))
        self.l_uploadOutput.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Upload output:", None, -1))
        self.b_submit.setText(QtWidgets.QApplication.translate("dlg_pandoraSubmitter", "Submit", None, -1))

