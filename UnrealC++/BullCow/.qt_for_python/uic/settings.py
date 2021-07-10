# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(651, 744)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 631, 724))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.config_name_label = QLabel(self.scrollAreaWidgetContents)
        self.config_name_label.setObjectName(u"config_name_label")
        self.config_name_label.setMinimumSize(QSize(74, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.config_name_label.setFont(font)
        self.config_name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.config_name_label)

        self.config_name_line_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.config_name_line_edit.setObjectName(u"config_name_line_edit")
        self.config_name_line_edit.setFont(font)

        self.horizontalLayout_9.addWidget(self.config_name_line_edit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ip_address_line_edit = QLineEdit(self.groupBox_2)
        self.ip_address_line_edit.setObjectName(u"ip_address_line_edit")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.ip_address_line_edit)

        self.transport_path_label = QLabel(self.groupBox_2)
        self.transport_path_label.setObjectName(u"transport_path_label")
        self.transport_path_label.setEnabled(False)
        self.transport_path_label.setMinimumSize(QSize(0, 0))

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.transport_path_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.transport_path_line_edit = QLineEdit(self.groupBox_2)
        self.transport_path_line_edit.setObjectName(u"transport_path_line_edit")
        self.transport_path_line_edit.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.transport_path_line_edit)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.formLayout_4.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.listener_exe_label = QLabel(self.groupBox_2)
        self.listener_exe_label.setObjectName(u"listener_exe_label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.listener_exe_label)

        self.listener_exe_line_edit = QLineEdit(self.groupBox_2)
        self.listener_exe_line_edit.setObjectName(u"listener_exe_line_edit")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.listener_exe_line_edit)


        self.verticalLayout_3.addLayout(self.formLayout_4)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.project_name_label = QLabel(self.groupBox)
        self.project_name_label.setObjectName(u"project_name_label")
        self.project_name_label.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.project_name_label)

        self.project_name_line_edit = QLineEdit(self.groupBox)
        self.project_name_line_edit.setObjectName(u"project_name_line_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.project_name_line_edit)

        self.uproject_label = QLabel(self.groupBox)
        self.uproject_label.setObjectName(u"uproject_label")
        self.uproject_label.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.uproject_label)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.uproject_line_edit = QLineEdit(self.groupBox)
        self.uproject_line_edit.setObjectName(u"uproject_line_edit")

        self.horizontalLayout_13.addWidget(self.uproject_line_edit)

        self.uproject_browse_button = QPushButton(self.groupBox)
        self.uproject_browse_button.setObjectName(u"uproject_browse_button")

        self.horizontalLayout_13.addWidget(self.uproject_browse_button)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_13)

        self.engine_dir_label = QLabel(self.groupBox)
        self.engine_dir_label.setObjectName(u"engine_dir_label")
        self.engine_dir_label.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.engine_dir_label)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.engine_dir_line_edit = QLineEdit(self.groupBox)
        self.engine_dir_line_edit.setObjectName(u"engine_dir_line_edit")

        self.horizontalLayout_14.addWidget(self.engine_dir_line_edit)

        self.engine_dir_browse_button = QPushButton(self.groupBox)
        self.engine_dir_browse_button.setObjectName(u"engine_dir_browse_button")

        self.horizontalLayout_14.addWidget(self.engine_dir_browse_button)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_14)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.build_engine_checkbox = QCheckBox(self.groupBox)
        self.build_engine_checkbox.setObjectName(u"build_engine_checkbox")
        self.build_engine_checkbox.setAutoFillBackground(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.build_engine_checkbox)

        self.map_path_label = QLabel(self.groupBox)
        self.map_path_label.setObjectName(u"map_path_label")
        self.map_path_label.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.map_path_label)

        self.map_path_line_edit = QLineEdit(self.groupBox)
        self.map_path_line_edit.setObjectName(u"map_path_line_edit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.map_path_line_edit)

        self.map_filter_label = QLabel(self.groupBox)
        self.map_filter_label.setObjectName(u"map_filter_label")
        self.map_filter_label.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.map_filter_label)

        self.map_filter_line_edit = QLineEdit(self.groupBox)
        self.map_filter_line_edit.setObjectName(u"map_filter_line_edit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.map_filter_line_edit)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.osc_server_port_line_edit = QLineEdit(self.groupBox_5)
        self.osc_server_port_line_edit.setObjectName(u"osc_server_port_line_edit")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.osc_server_port_line_edit)

        self.osc_client_port_line_edit = QLineEdit(self.groupBox_5)
        self.osc_client_port_line_edit.setObjectName(u"osc_client_port_line_edit")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.osc_client_port_line_edit)


        self.verticalLayout_7.addLayout(self.formLayout_6)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.p4_group_box = QGroupBox(self.groupBox)
        self.p4_group_box.setObjectName(u"p4_group_box")
        self.p4_group_box.setCheckable(True)
        self.p4_group_box.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.p4_group_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.p4_project_path_label = QLabel(self.p4_group_box)
        self.p4_project_path_label.setObjectName(u"p4_project_path_label")
        self.p4_project_path_label.setMinimumSize(QSize(0, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.p4_project_path_label)

        self.p4_project_path_line_edit = QLineEdit(self.p4_group_box)
        self.p4_project_path_line_edit.setObjectName(u"p4_project_path_line_edit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.p4_project_path_line_edit)

        self.source_control_workspace_label = QLabel(self.p4_group_box)
        self.source_control_workspace_label.setObjectName(u"source_control_workspace_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.source_control_workspace_label)

        self.source_control_workspace_line_edit = QLineEdit(self.p4_group_box)
        self.source_control_workspace_line_edit.setObjectName(u"source_control_workspace_line_edit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.source_control_workspace_line_edit)

        self.p4_engine_path_label = QLabel(self.p4_group_box)
        self.p4_engine_path_label.setObjectName(u"p4_engine_path_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.p4_engine_path_label)

        self.p4_engine_path_line_edit = QLineEdit(self.p4_group_box)
        self.p4_engine_path_line_edit.setObjectName(u"p4_engine_path_line_edit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.p4_engine_path_line_edit)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.verticalLayout_2.addWidget(self.p4_group_box)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.mu_server_name_label = QLabel(self.groupBox_4)
        self.mu_server_name_label.setObjectName(u"mu_server_name_label")
        self.mu_server_name_label.setMinimumSize(QSize(0, 0))
        self.mu_server_name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.mu_server_name_label)

        self.mu_server_name_line_edit = QLineEdit(self.groupBox_4)
        self.mu_server_name_line_edit.setObjectName(u"mu_server_name_line_edit")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.mu_server_name_line_edit)

        self.mu_cmd_line_args_label = QLabel(self.groupBox_4)
        self.mu_cmd_line_args_label.setObjectName(u"mu_cmd_line_args_label")
        self.mu_cmd_line_args_label.setMinimumSize(QSize(0, 0))
        self.mu_cmd_line_args_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.mu_cmd_line_args_label)

        self.mu_cmd_line_args_line_edit = QLineEdit(self.groupBox_4)
        self.mu_cmd_line_args_line_edit.setObjectName(u"mu_cmd_line_args_line_edit")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.mu_cmd_line_args_line_edit)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.mu_auto_join_check_box = QCheckBox(self.groupBox_4)
        self.mu_auto_join_check_box.setObjectName(u"mu_auto_join_check_box")
        self.mu_auto_join_check_box.setChecked(True)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.mu_auto_join_check_box)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.mu_clean_history_check_box = QCheckBox(self.groupBox_4)
        self.mu_clean_history_check_box.setObjectName(u"mu_clean_history_check_box")
        self.mu_clean_history_check_box.setChecked(True)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.mu_clean_history_check_box)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.mu_auto_launch_check_box = QCheckBox(self.groupBox_4)
        self.mu_auto_launch_check_box.setObjectName(u"mu_auto_launch_check_box")
        self.mu_auto_launch_check_box.setChecked(True)

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.mu_auto_launch_check_box)

        self.muserver_exe_label = QLabel(self.groupBox_4)
        self.muserver_exe_label.setObjectName(u"muserver_exe_label")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.muserver_exe_label)

        self.muserver_exe_line_edit = QLineEdit(self.groupBox_4)
        self.muserver_exe_line_edit.setObjectName(u"muserver_exe_line_edit")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.muserver_exe_line_edit)

        self.muserver_auto_build_label = QLabel(self.groupBox_4)
        self.muserver_auto_build_label.setObjectName(u"muserver_auto_build_label")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.muserver_auto_build_label)

        self.muserver_auto_build_check_box = QCheckBox(self.groupBox_4)
        self.muserver_auto_build_check_box.setObjectName(u"muserver_auto_build_check_box")
        self.muserver_auto_build_check_box.setChecked(True)

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.muserver_auto_build_check_box)


        self.verticalLayout_6.addLayout(self.formLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.device_override_layout = QVBoxLayout()
        self.device_override_layout.setObjectName(u"device_override_layout")
        self.device_override_layout.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_4.addLayout(self.device_override_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.config_name_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.config_name_label.setText(QCoreApplication.translate("Dialog", u"Config Name", None))
#if QT_CONFIG(tooltip)
        self.config_name_line_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Switchboard", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Dialog", u"Current Machine IP Address. Used as OSC send target", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Dialog", u"IP Address", None))
#if QT_CONFIG(tooltip)
        self.ip_address_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Current Machine IP Address. Used as OSC send target", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.transport_path_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.transport_path_label.setText(QCoreApplication.translate("Dialog", u"Transport Path", None))
#if QT_CONFIG(tooltip)
        self.transport_path_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Feature coming soon", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.listener_exe_label.setToolTip(QCoreApplication.translate("Dialog", u"Filename of the Switchboard listener executable. (The .exe extension can be omitted on Windows.)", None))
#endif // QT_CONFIG(tooltip)
        self.listener_exe_label.setText(QCoreApplication.translate("Dialog", u"Listener Executable Name", None))
#if QT_CONFIG(tooltip)
        self.listener_exe_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Filename of the Switchboard listener executable. (The .exe extension can be omitted on Windows.)", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Project Settings", None))
#if QT_CONFIG(tooltip)
        self.project_name_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.project_name_label.setText(QCoreApplication.translate("Dialog", u"Project Name", None))
#if QT_CONFIG(tooltip)
        self.project_name_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Name of your project. All takes will be recorded into a folder structure with this name as the root name.", None))
#endif // QT_CONFIG(tooltip)
        self.project_name_line_edit.setText("")
        self.project_name_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"MyProject", None))
#if QT_CONFIG(tooltip)
        self.uproject_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.uproject_label.setText(QCoreApplication.translate("Dialog", u"UProject", None))
#if QT_CONFIG(tooltip)
        self.uproject_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Path to uProject", None))
#endif // QT_CONFIG(tooltip)
        self.uproject_line_edit.setText("")
        self.uproject_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"C:\\Users\\UserName\\Documents\\Unreal Projects\\MyProject\\MyProject.uproject", None))
        self.uproject_browse_button.setText(QCoreApplication.translate("Dialog", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.engine_dir_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.engine_dir_label.setText(QCoreApplication.translate("Dialog", u"Engine Dir", None))
#if QT_CONFIG(tooltip)
        self.engine_dir_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Path to UE4 Engine directory", None))
#endif // QT_CONFIG(tooltip)
        self.engine_dir_line_edit.setText("")
        self.engine_dir_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"C:\\Program Files\\Epic Games\\UE_4.26\\Engine", None))
        self.engine_dir_browse_button.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Build Engine", None))
#if QT_CONFIG(tooltip)
        self.build_engine_checkbox.setToolTip(QCoreApplication.translate("Dialog", u"Check if engine needs to be built from source", None))
#endif // QT_CONFIG(tooltip)
        self.build_engine_checkbox.setText("")
        self.map_path_label.setText(QCoreApplication.translate("Dialog", u"Map Path", None))
#if QT_CONFIG(tooltip)
        self.map_path_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Relative path from Content folder that contains maps to launch into.", None))
#endif // QT_CONFIG(tooltip)
        self.map_path_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Maps", None))
        self.map_filter_label.setText(QCoreApplication.translate("Dialog", u"Map Filter", None))
#if QT_CONFIG(tooltip)
        self.map_filter_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Walk every file in the Map Path and run a fnmatch to filter the file names", None))
#endif // QT_CONFIG(tooltip)
        self.map_filter_line_edit.setText("")
        self.map_filter_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"*.umap", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"OSC", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Server Port", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Client Port", None))
        self.p4_group_box.setTitle(QCoreApplication.translate("Dialog", u"Source Control", None))
        self.p4_project_path_label.setText(QCoreApplication.translate("Dialog", u"P4 Project Path", None))
        self.p4_project_path_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"//Depot/Project   (.uproject Directory)", None))
        self.source_control_workspace_label.setText(QCoreApplication.translate("Dialog", u"Workspace Name", None))
        self.p4_engine_path_label.setText(QCoreApplication.translate("Dialog", u"P4 Engine Path", None))
        self.p4_engine_path_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"//Depot/Engine    (Engine Directory)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Multi User Server", None))
#if QT_CONFIG(tooltip)
        self.mu_server_name_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.mu_server_name_label.setText(QCoreApplication.translate("Dialog", u"Server Name", None))
#if QT_CONFIG(tooltip)
        self.mu_server_name_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Path to uProject", None))
#endif // QT_CONFIG(tooltip)
        self.mu_server_name_line_edit.setText("")
        self.mu_server_name_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"MU_Server", None))
#if QT_CONFIG(tooltip)
        self.mu_cmd_line_args_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.mu_cmd_line_args_label.setText(QCoreApplication.translate("Dialog", u"Command Line Args", None))
#if QT_CONFIG(tooltip)
        self.mu_cmd_line_args_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"MU Server Command line arguments", None))
#endif // QT_CONFIG(tooltip)
        self.mu_cmd_line_args_line_edit.setText("")
        self.mu_cmd_line_args_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"-UDPMESSAGING_TRANSPORT_UNICAST={IP_ADDRESS}:5555'", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Auto Join", None))
#if QT_CONFIG(tooltip)
        self.mu_auto_join_check_box.setToolTip(QCoreApplication.translate("Dialog", u"Unreal Machines that have been launched join the Multi User Server", None))
#endif // QT_CONFIG(tooltip)
        self.mu_auto_join_check_box.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Clean History", None))
        self.mu_clean_history_check_box.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Auto Launch", None))
#if QT_CONFIG(tooltip)
        self.mu_auto_launch_check_box.setToolTip(QCoreApplication.translate("Dialog", u"Launch the Multi User server when Unreal is launched", None))
#endif // QT_CONFIG(tooltip)
        self.mu_auto_launch_check_box.setText("")
        self.muserver_exe_label.setText(QCoreApplication.translate("Dialog", u"Executable Name", None))
#if QT_CONFIG(tooltip)
        self.muserver_exe_label.setToolTip(QCoreApplication.translate("Dialog", u"Filename of the multi-user server executable. (The .exe extension can be omitted on Windows.)", None))
#endif // QT_CONFIG(tooltip)
        self.muserver_exe_line_edit.setText(QCoreApplication.translate("Dialog", u"UnrealMultiUserServer", None))
        self.muserver_exe_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"UnrealMultiUserServer", None))
#if QT_CONFIG(tooltip)
        self.muserver_exe_line_edit.setToolTip(QCoreApplication.translate("Dialog", u"Filename of the multi-user server executable. (The .exe extension can be omitted on Windows.)", None))
#endif // QT_CONFIG(tooltip)
        self.muserver_auto_build_label.setText(QCoreApplication.translate("Dialog", u"Auto Build", None))
#if QT_CONFIG(tooltip)
        self.muserver_auto_build_label.setToolTip(QCoreApplication.translate("Dialog", u"Whether to include the UnrealMultiUserServer project when performing local device builds.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.muserver_auto_build_check_box.setToolTip(QCoreApplication.translate("Dialog", u"Whether to include the UnrealMultiUserServer project when performing local device builds.", None))
#endif // QT_CONFIG(tooltip)
        self.muserver_auto_build_check_box.setText("")
    # retranslateUi

