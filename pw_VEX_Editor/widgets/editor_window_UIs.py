# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_pipeline\pw_pipeline\assets\houdini\python\VEX\pw_Houdini_VEX_Editor\pw_VEX_Editor\widgets\editor_window.ui'
#
# Created: Thu Mar 17 10:44:37 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_editor_window(object):
    def setupUi(self, editor_window):
        editor_window.setObjectName("editor_window")
        editor_window.resize(1221, 587)
        self.centralwidget = QtGui.QWidget(editor_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolbar_wd = QtGui.QFrame(self.centralwidget)
        self.toolbar_wd.setFrameShape(QtGui.QFrame.StyledPanel)
        self.toolbar_wd.setFrameShadow(QtGui.QFrame.Raised)
        self.toolbar_wd.setObjectName("toolbar_wd")
        self.horizontalLayout = QtGui.QHBoxLayout(self.toolbar_wd)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_from_selected_btn = QtGui.QPushButton(self.toolbar_wd)
        self.load_from_selected_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.load_from_selected_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.load_from_selected_btn.setObjectName("load_from_selected_btn")
        self.horizontalLayout.addWidget(self.load_from_selected_btn)
        self.load_from_selected_extra_btn = QtGui.QPushButton(self.toolbar_wd)
        self.load_from_selected_extra_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.load_from_selected_extra_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.load_from_selected_extra_btn.setObjectName("load_from_selected_extra_btn")
        self.horizontalLayout.addWidget(self.load_from_selected_extra_btn)
        self.load_from_file_btn = QtGui.QPushButton(self.toolbar_wd)
        self.load_from_file_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.load_from_file_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.load_from_file_btn.setObjectName("load_from_file_btn")
        self.horizontalLayout.addWidget(self.load_from_file_btn)
        self.blank_tab_btn = QtGui.QPushButton(self.toolbar_wd)
        self.blank_tab_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.blank_tab_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.blank_tab_btn.setObjectName("blank_tab_btn")
        self.horizontalLayout.addWidget(self.blank_tab_btn)
        self.line_2 = QtGui.QFrame(self.toolbar_wd)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.save_current_btn = QtGui.QPushButton(self.toolbar_wd)
        self.save_current_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.save_current_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.save_current_btn.setObjectName("save_current_btn")
        self.horizontalLayout.addWidget(self.save_current_btn)
        self.reload_current_btn = QtGui.QPushButton(self.toolbar_wd)
        self.reload_current_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.reload_current_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.reload_current_btn.setObjectName("reload_current_btn")
        self.horizontalLayout.addWidget(self.reload_current_btn)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line = QtGui.QFrame(self.toolbar_wd)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.node_info_wd = QtGui.QWidget(self.toolbar_wd)
        self.node_info_wd.setObjectName("node_info_wd")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.node_info_wd)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.node_info_lb = QtGui.QLabel(self.node_info_wd)
        self.node_info_lb.setObjectName("node_info_lb")
        self.horizontalLayout_2.addWidget(self.node_info_lb)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.show_sourse_btn = QtGui.QPushButton(self.node_info_wd)
        self.show_sourse_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.show_sourse_btn.setObjectName("show_sourse_btn")
        self.horizontalLayout_2.addWidget(self.show_sourse_btn)
        self.horizontalLayout.addWidget(self.node_info_wd)
        self.file_info_wd = QtGui.QWidget(self.toolbar_wd)
        self.file_info_wd.setObjectName("file_info_wd")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.file_info_wd)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_info_static_lb = QtGui.QLabel(self.file_info_wd)
        self.file_info_static_lb.setObjectName("file_info_static_lb")
        self.verticalLayout.addWidget(self.file_info_static_lb)
        self.scrollArea = QtGui.QScrollArea(self.file_info_wd)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 18))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 69, 16))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.file_info_lb = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.file_info_lb.setObjectName("file_info_lb")
        self.verticalLayout_3.addWidget(self.file_info_lb)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.show_sourse_btn_2 = QtGui.QPushButton(self.file_info_wd)
        self.show_sourse_btn_2.setMinimumSize(QtCore.QSize(0, 40))
        self.show_sourse_btn_2.setObjectName("show_sourse_btn_2")
        self.horizontalLayout_3.addWidget(self.show_sourse_btn_2)
        self.horizontalLayout.addWidget(self.file_info_wd)
        self.empty_wd = QtGui.QWidget(self.toolbar_wd)
        self.empty_wd.setObjectName("empty_wd")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.empty_wd)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.empty_wd)
        self.horizontalLayout.setStretch(7, 1)
        self.horizontalLayout.setStretch(8, 1)
        self.horizontalLayout.setStretch(9, 1)
        self.verticalLayout_2.addWidget(self.toolbar_wd)
        self.tab_ly = QtGui.QVBoxLayout()
        self.tab_ly.setObjectName("tab_ly")
        self.verticalLayout_2.addLayout(self.tab_ly)
        self.error_browser_ly = QtGui.QVBoxLayout()
        self.error_browser_ly.setObjectName("error_browser_ly")
        self.verticalLayout_2.addLayout(self.error_browser_ly)
        self.help_ly = QtGui.QVBoxLayout()
        self.help_ly.setObjectName("help_ly")
        self.verticalLayout_2.addLayout(self.help_ly)
        self.verticalLayout_2.setStretch(1, 1)
        editor_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(editor_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1221, 21))
        self.menubar.setObjectName("menubar")
        self.menu_tabs = QtGui.QMenu(self.menubar)
        self.menu_tabs.setObjectName("menu_tabs")
        self.backup_menu_act = QtGui.QMenu(self.menu_tabs)
        self.backup_menu_act.setObjectName("backup_menu_act")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEditor = QtGui.QMenu(self.menubar)
        self.menuEditor.setObjectName("menuEditor")
        self.menuTheme = QtGui.QMenu(self.menuEditor)
        self.menuTheme.setObjectName("menuTheme")
        self.menuTemplates = QtGui.QMenu(self.menubar)
        self.menuTemplates.setObjectName("menuTemplates")
        editor_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(editor_window)
        self.statusbar.setObjectName("statusbar")
        editor_window.setStatusBar(self.statusbar)
        self.actionSave_to_file = QtGui.QAction(editor_window)
        self.actionSave_to_file.setObjectName("actionSave_to_file")
        self.actionLoad_from_File = QtGui.QAction(editor_window)
        self.actionLoad_from_File.setObjectName("actionLoad_from_File")
        self.create_from_node_act = QtGui.QAction(editor_window)
        self.create_from_node_act.setObjectName("create_from_node_act")
        self.reload_source_act = QtGui.QAction(editor_window)
        self.reload_source_act.setObjectName("reload_source_act")
        self.save_section_act = QtGui.QAction(editor_window)
        self.save_section_act.setObjectName("save_section_act")
        self.manual_act = QtGui.QAction(editor_window)
        self.manual_act.setObjectName("manual_act")
        self.about_act = QtGui.QAction(editor_window)
        self.about_act.setObjectName("about_act")
        self.actionHelp_Window_2 = QtGui.QAction(editor_window)
        self.actionHelp_Window_2.setCheckable(True)
        self.actionHelp_Window_2.setObjectName("actionHelp_Window_2")
        self.actionAutocompletion = QtGui.QAction(editor_window)
        self.actionAutocompletion.setCheckable(True)
        self.actionAutocompletion.setObjectName("actionAutocompletion")
        self.vex_manual_act = QtGui.QAction(editor_window)
        self.vex_manual_act.setObjectName("vex_manual_act")
        self.context_help_act = QtGui.QAction(editor_window)
        self.context_help_act.setObjectName("context_help_act")
        self.save_tabs_in_hip_act = QtGui.QAction(editor_window)
        self.save_tabs_in_hip_act.setCheckable(True)
        self.save_tabs_in_hip_act.setObjectName("save_tabs_in_hip_act")
        self.actionLoad_tabs = QtGui.QAction(editor_window)
        self.actionLoad_tabs.setObjectName("actionLoad_tabs")
        self.create_from_file_act = QtGui.QAction(editor_window)
        self.create_from_file_act.setObjectName("create_from_file_act")
        self.create_empty_act = QtGui.QAction(editor_window)
        self.create_empty_act.setObjectName("create_empty_act")
        self.use_hou_browser_act = QtGui.QAction(editor_window)
        self.use_hou_browser_act.setCheckable(True)
        self.use_hou_browser_act.setChecked(True)
        self.use_hou_browser_act.setObjectName("use_hou_browser_act")
        self.clear_tabs_act = QtGui.QAction(editor_window)
        self.clear_tabs_act.setObjectName("clear_tabs_act")
        self.open_theme_editor_act = QtGui.QAction(editor_window)
        self.open_theme_editor_act.setEnabled(True)
        self.open_theme_editor_act.setObjectName("open_theme_editor_act")
        self.set_font_size_act = QtGui.QAction(editor_window)
        self.set_font_size_act.setObjectName("set_font_size_act")
        self.load_tabs_from_hip_act = QtGui.QAction(editor_window)
        self.load_tabs_from_hip_act.setObjectName("load_tabs_from_hip_act")
        self.auto_create_parms_act = QtGui.QAction(editor_window)
        self.auto_create_parms_act.setCheckable(True)
        self.auto_create_parms_act.setObjectName("auto_create_parms_act")
        self.theme_light_act = QtGui.QAction(editor_window)
        self.theme_light_act.setObjectName("theme_light_act")
        self.theme_dark_act = QtGui.QAction(editor_window)
        self.theme_dark_act.setObjectName("theme_dark_act")
        self.live_template_editor_act = QtGui.QAction(editor_window)
        self.live_template_editor_act.setEnabled(True)
        self.live_template_editor_act.setObjectName("live_template_editor_act")
        self.use_online_manual_act = QtGui.QAction(editor_window)
        self.use_online_manual_act.setCheckable(True)
        self.use_online_manual_act.setObjectName("use_online_manual_act")
        self.show_whitespaces_act = QtGui.QAction(editor_window)
        self.show_whitespaces_act.setCheckable(True)
        self.show_whitespaces_act.setObjectName("show_whitespaces_act")
        self.check_new_version_act = QtGui.QAction(editor_window)
        self.check_new_version_act.setObjectName("check_new_version_act")
        self.options_act = QtGui.QAction(editor_window)
        self.options_act.setObjectName("options_act")
        self.clear_backups_act = QtGui.QAction(editor_window)
        self.clear_backups_act.setObjectName("clear_backups_act")
        self.open_backup_folder_act = QtGui.QAction(editor_window)
        self.open_backup_folder_act.setObjectName("open_backup_folder_act")
        self.save_to_new_act = QtGui.QAction(editor_window)
        self.save_to_new_act.setObjectName("save_to_new_act")
        self.open_settings_folder_act = QtGui.QAction(editor_window)
        self.open_settings_folder_act.setObjectName("open_settings_folder_act")
        self.help_window_act = QtGui.QAction(editor_window)
        self.help_window_act.setCheckable(True)
        self.help_window_act.setObjectName("help_window_act")
        self.find_replace_act = QtGui.QAction(editor_window)
        self.find_replace_act.setObjectName("find_replace_act")
        self.backup_menu_act.addAction(self.clear_backups_act)
        self.backup_menu_act.addAction(self.open_backup_folder_act)
        self.backup_menu_act.addSeparator()
        self.menu_tabs.addAction(self.create_from_node_act)
        self.menu_tabs.addAction(self.create_from_file_act)
        self.menu_tabs.addAction(self.create_empty_act)
        self.menu_tabs.addSeparator()
        self.menu_tabs.addAction(self.save_section_act)
        self.menu_tabs.addAction(self.save_to_new_act)
        self.menu_tabs.addAction(self.reload_source_act)
        self.menu_tabs.addSeparator()
        self.menu_tabs.addAction(self.load_tabs_from_hip_act)
        self.menu_tabs.addAction(self.clear_tabs_act)
        self.menu_tabs.addSeparator()
        self.menu_tabs.addAction(self.backup_menu_act.menuAction())
        self.menuHelp.addAction(self.manual_act)
        self.menuHelp.addAction(self.vex_manual_act)
        self.menuHelp.addAction(self.context_help_act)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.check_new_version_act)
        self.menuHelp.addAction(self.about_act)
        self.menuTheme.addAction(self.open_theme_editor_act)
        self.menuTheme.addSeparator()
        self.menuEditor.addAction(self.menuTheme.menuAction())
        self.menuEditor.addAction(self.options_act)
        self.menuEditor.addAction(self.find_replace_act)
        self.menuEditor.addSeparator()
        self.menuEditor.addAction(self.open_settings_folder_act)
        self.menuTemplates.addAction(self.live_template_editor_act)
        self.menuTemplates.addSeparator()
        self.menubar.addAction(self.menu_tabs.menuAction())
        self.menubar.addAction(self.menuEditor.menuAction())
        self.menubar.addAction(self.menuTemplates.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(editor_window)
        QtCore.QMetaObject.connectSlotsByName(editor_window)

    def retranslateUi(self, editor_window):
        editor_window.setWindowTitle(QtGui.QApplication.translate("editor_window", "VEX Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.load_from_selected_btn.setToolTip(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>Auto load VEX parameter from selected node</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.load_from_selected_btn.setText(QtGui.QApplication.translate("editor_window", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.load_from_selected_extra_btn.setToolTip(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>Set VEX parameter from parameter list on selected node</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.load_from_selected_extra_btn.setText(QtGui.QApplication.translate("editor_window", "L+", None, QtGui.QApplication.UnicodeUTF8))
        self.load_from_file_btn.setToolTip(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>Open .h file from disk</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.load_from_file_btn.setText(QtGui.QApplication.translate("editor_window", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.blank_tab_btn.setToolTip(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>Create New Empty Tab</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.blank_tab_btn.setText(QtGui.QApplication.translate("editor_window", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.save_current_btn.setToolTip(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>Save code (Ctrl+Enter)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.save_current_btn.setText(QtGui.QApplication.translate("editor_window", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.reload_current_btn.setToolTip(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>Reload sourse code</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.reload_current_btn.setText(QtGui.QApplication.translate("editor_window", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.node_info_lb.setText(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>Node: /obj/geo1/nodename<br/>Parm: snippet</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.show_sourse_btn.setText(QtGui.QApplication.translate("editor_window", "Select Node", None, QtGui.QApplication.UnicodeUTF8))
        self.file_info_static_lb.setText(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>File Path:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.file_info_lb.setText(QtGui.QApplication.translate("editor_window", "<html><head/><body><p>path</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.show_sourse_btn_2.setText(QtGui.QApplication.translate("editor_window", "Open Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_tabs.setTitle(QtGui.QApplication.translate("editor_window", "Tabs", None, QtGui.QApplication.UnicodeUTF8))
        self.backup_menu_act.setTitle(QtGui.QApplication.translate("editor_window", "Backups", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("editor_window", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEditor.setTitle(QtGui.QApplication.translate("editor_window", "Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTheme.setTitle(QtGui.QApplication.translate("editor_window", "Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTemplates.setTitle(QtGui.QApplication.translate("editor_window", "Templates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_to_file.setText(QtGui.QApplication.translate("editor_window", "Save vex file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_from_File.setText(QtGui.QApplication.translate("editor_window", "Load vex File", None, QtGui.QApplication.UnicodeUTF8))
        self.create_from_node_act.setText(QtGui.QApplication.translate("editor_window", "Create From Selected Node", None, QtGui.QApplication.UnicodeUTF8))
        self.reload_source_act.setText(QtGui.QApplication.translate("editor_window", "Reload Current Tab From Sourse", None, QtGui.QApplication.UnicodeUTF8))
        self.save_section_act.setText(QtGui.QApplication.translate("editor_window", "Save Current Code", None, QtGui.QApplication.UnicodeUTF8))
        self.manual_act.setText(QtGui.QApplication.translate("editor_window", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.about_act.setText(QtGui.QApplication.translate("editor_window", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_Window_2.setText(QtGui.QApplication.translate("editor_window", "Help Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutocompletion.setText(QtGui.QApplication.translate("editor_window", "Autocompletion", None, QtGui.QApplication.UnicodeUTF8))
        self.vex_manual_act.setText(QtGui.QApplication.translate("editor_window", "VEX Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.context_help_act.setText(QtGui.QApplication.translate("editor_window", "Show help for selected method", None, QtGui.QApplication.UnicodeUTF8))
        self.context_help_act.setShortcut(QtGui.QApplication.translate("editor_window", "Shift+F1", None, QtGui.QApplication.UnicodeUTF8))
        self.save_tabs_in_hip_act.setText(QtGui.QApplication.translate("editor_window", "Save Tabs Inside HIP", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_tabs.setText(QtGui.QApplication.translate("editor_window", "Load Tabs", None, QtGui.QApplication.UnicodeUTF8))
        self.create_from_file_act.setText(QtGui.QApplication.translate("editor_window", "Create From File", None, QtGui.QApplication.UnicodeUTF8))
        self.create_empty_act.setText(QtGui.QApplication.translate("editor_window", "Create Empty Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.use_hou_browser_act.setText(QtGui.QApplication.translate("editor_window", "Use Houdini Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_tabs_act.setText(QtGui.QApplication.translate("editor_window", "Clear Saved Tabs", None, QtGui.QApplication.UnicodeUTF8))
        self.open_theme_editor_act.setText(QtGui.QApplication.translate("editor_window", "Edit Theme...", None, QtGui.QApplication.UnicodeUTF8))
        self.set_font_size_act.setText(QtGui.QApplication.translate("editor_window", "Font Size...", None, QtGui.QApplication.UnicodeUTF8))
        self.load_tabs_from_hip_act.setText(QtGui.QApplication.translate("editor_window", "Load Tabs From Current HIP", None, QtGui.QApplication.UnicodeUTF8))
        self.auto_create_parms_act.setText(QtGui.QApplication.translate("editor_window", "Auto Update Node Spare Parameters On Save", None, QtGui.QApplication.UnicodeUTF8))
        self.theme_light_act.setText(QtGui.QApplication.translate("editor_window", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.theme_dark_act.setText(QtGui.QApplication.translate("editor_window", "Dark", None, QtGui.QApplication.UnicodeUTF8))
        self.live_template_editor_act.setText(QtGui.QApplication.translate("editor_window", "Templates Editor...", None, QtGui.QApplication.UnicodeUTF8))
        self.use_online_manual_act.setText(QtGui.QApplication.translate("editor_window", "Use Online Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.show_whitespaces_act.setText(QtGui.QApplication.translate("editor_window", "Show Whitespaces", None, QtGui.QApplication.UnicodeUTF8))
        self.check_new_version_act.setText(QtGui.QApplication.translate("editor_window", "Check New Version", None, QtGui.QApplication.UnicodeUTF8))
        self.options_act.setText(QtGui.QApplication.translate("editor_window", "Options...", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_backups_act.setText(QtGui.QApplication.translate("editor_window", "Clear backups", None, QtGui.QApplication.UnicodeUTF8))
        self.open_backup_folder_act.setText(QtGui.QApplication.translate("editor_window", "Open folder", None, QtGui.QApplication.UnicodeUTF8))
        self.save_to_new_act.setText(QtGui.QApplication.translate("editor_window", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.open_settings_folder_act.setText(QtGui.QApplication.translate("editor_window", "Open settings folder", None, QtGui.QApplication.UnicodeUTF8))
        self.help_window_act.setText(QtGui.QApplication.translate("editor_window", "Help Window", None, QtGui.QApplication.UnicodeUTF8))
        self.find_replace_act.setText(QtGui.QApplication.translate("editor_window", "Find and Replace...", None, QtGui.QApplication.UnicodeUTF8))
        self.find_replace_act.setShortcut(QtGui.QApplication.translate("editor_window", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))

