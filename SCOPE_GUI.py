from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        # Allow smaller minimum window size for vertical resizing
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_utilres_status = QtWidgets.QVBoxLayout()
        self.verticalLayout_utilres_status.setObjectName("verticalLayout_utilres_status")
        self.horizontalLayout_utils_res = QtWidgets.QHBoxLayout()
        self.horizontalLayout_utils_res.setObjectName("horizontalLayout_utils_res")
        self.verticalLayout_utils = QtWidgets.QVBoxLayout()
        self.verticalLayout_utils.setObjectName("verticalLayout_utils")
        self.groupBox_input = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_input.setObjectName("groupBox_input")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_input)
        self.verticalLayout.setObjectName("verticalLayout")
        # Direct file selection row inside input group (remove Upload File tab)
        self.horizontalLayout_file = QtWidgets.QHBoxLayout()
        self.horizontalLayout_file.setObjectName("horizontalLayout_file")
        self.filename = QtWidgets.QLineEdit(self.groupBox_input)
        self.filename.setObjectName("filename")
        self.horizontalLayout_file.addWidget(self.filename)
        self.pushButton_select_file = QtWidgets.QPushButton(self.groupBox_input)
        self.pushButton_select_file.setObjectName("pushButton_select_file")
        self.horizontalLayout_file.addWidget(self.pushButton_select_file)
        self.verticalLayout.addLayout(self.horizontalLayout_file)
        self.horizontalLayout_fasta = QtWidgets.QHBoxLayout()
        self.horizontalLayout_fasta.setObjectName("horizontalLayout_fasta")
        self.filename_fasta = QtWidgets.QLineEdit(self.groupBox_input)
        self.filename_fasta.setObjectName("filename_fasta")
        self.horizontalLayout_fasta.addWidget(self.filename_fasta)
        self.pushButton_select_fasta = QtWidgets.QPushButton(self.groupBox_input)
        self.pushButton_select_fasta.setObjectName("pushButton_select_fasta")
        self.horizontalLayout_fasta.addWidget(self.pushButton_select_fasta)
        self.verticalLayout.addLayout(self.horizontalLayout_fasta)
        self.verticalLayout_utils.addWidget(self.groupBox_input)
        # Step 1: feature extraction
        self.groupBox_feature_extract = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_feature_extract.setObjectName("groupBox_feature_extract")
        self.verticalLayout_feature = QtWidgets.QVBoxLayout(self.groupBox_feature_extract)
        self.verticalLayout_feature.setObjectName("verticalLayout_feature")
        self.widget_feature_body = QtWidgets.QWidget(self.groupBox_feature_extract)
        self.widget_feature_body.setObjectName("widget_feature_body")
        self.verticalLayout_feature_body = QtWidgets.QVBoxLayout(self.widget_feature_body)
        self.verticalLayout_feature_body.setObjectName("verticalLayout_feature_body")
        self.label_feature = QtWidgets.QLabel(self.widget_feature_body)
        self.label_feature.setWordWrap(True)
        self.label_feature.setObjectName("label_feature")
        self.verticalLayout_feature_body.addWidget(self.label_feature)
        self.button_extract_features = QtWidgets.QPushButton(self.widget_feature_body)
        self.button_extract_features.setObjectName("button_extract_features")
        self.verticalLayout_feature_body.addWidget(self.button_extract_features)
        self.verticalLayout_feature.addWidget(self.widget_feature_body)
        self.label_feature_hint = QtWidgets.QLabel(self.groupBox_feature_extract)
        self.label_feature_hint.setObjectName("label_feature_hint")
        self.label_feature_hint.setWordWrap(True)
        self.verticalLayout_feature.addWidget(self.label_feature_hint)
        self.verticalLayout_utils.addWidget(self.groupBox_feature_extract)

        # Step 2: catalytic-site prediction (description panel)
        self.groupBox_catalytic = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_catalytic.setObjectName("groupBox_catalytic")
        self.verticalLayout_catalytic = QtWidgets.QVBoxLayout(self.groupBox_catalytic)
        self.verticalLayout_catalytic.setObjectName("verticalLayout_catalytic")
        self.widget_catalytic_body = QtWidgets.QWidget(self.groupBox_catalytic)
        self.widget_catalytic_body.setObjectName("widget_catalytic_body")
        self.verticalLayout_catalytic_body = QtWidgets.QVBoxLayout(self.widget_catalytic_body)
        self.verticalLayout_catalytic_body.setObjectName("verticalLayout_catalytic_body")
        self.label_catalytic = QtWidgets.QLabel(self.widget_catalytic_body)
        self.label_catalytic.setWordWrap(True)
        self.label_catalytic.setObjectName("label_catalytic")
        self.verticalLayout_catalytic_body.addWidget(self.label_catalytic)
        self.verticalLayout_catalytic.addWidget(self.widget_catalytic_body)
        self.label_catalytic_hint = QtWidgets.QLabel(self.groupBox_catalytic)
        self.label_catalytic_hint.setObjectName("label_catalytic_hint")
        self.label_catalytic_hint.setWordWrap(True)
        self.verticalLayout_catalytic.addWidget(self.label_catalytic_hint)
        self.verticalLayout_utils.addWidget(self.groupBox_catalytic)
        
        self.groupBox_parameters = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        # Collapsible body inside parameters group
        self.verticalLayout_params_group = QtWidgets.QVBoxLayout(self.groupBox_parameters)
        self.verticalLayout_params_group.setObjectName("verticalLayout_params_group")
        self.widget_parameters_body = QtWidgets.QWidget(self.groupBox_parameters)
        self.widget_parameters_body.setObjectName("widget_parameters_body")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_parameters_body)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        
        self.LineEdit_num_workers = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_num_workers.setObjectName("LineEdit_num_workers")
        self.LineEdit_num_workers.setText("1")
        self.verticalLayout_8.addWidget(self.LineEdit_num_workers)
        
        self.LineEdit_chain = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_chain.setObjectName("LineEdit_chain")
        self.LineEdit_chain.setText("A")
        self.verticalLayout_8.addWidget(self.LineEdit_chain)
        
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        # Add parameters body to group
        self.verticalLayout_params_group.addWidget(self.widget_parameters_body)
        self.verticalLayout_utils.addWidget(self.groupBox_parameters)
        self.groupBox_operator = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_operator.setObjectName("groupBox_operator")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_operator)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.button_predict = QtWidgets.QPushButton(self.groupBox_operator)
        self.button_predict.setObjectName("button_predict")
        self.horizontalLayout_4.addWidget(self.button_predict)

        self.buttonn_save = QtWidgets.QPushButton(self.groupBox_operator)
        self.buttonn_save.setObjectName("buttonn_save")
        self.horizontalLayout_4.addWidget(self.buttonn_save)

        self.buttonn_clean = QtWidgets.QPushButton(self.groupBox_operator)
        self.buttonn_clean.setObjectName("buttonn_clean")
        self.horizontalLayout_4.addWidget(self.buttonn_clean)

        self.button_load_result = QtWidgets.QPushButton(self.groupBox_operator)
        self.button_load_result.setObjectName("button_load_result")
        self.horizontalLayout_4.addWidget(self.button_load_result)


        
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_utils.addWidget(self.groupBox_operator)
        self.verticalLayout_utils.setStretch(0, 2)
        self.verticalLayout_utils.setStretch(1, 6)
        self.verticalLayout_utils.setStretch(2, 1)
        self.verticalLayout_utils.setStretch(3, 1)
        self.horizontalLayout_utils_res.addLayout(self.verticalLayout_utils)
        self.Tab_res = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab_res.setObjectName("Tab_res")
        self.tab_meloculesdata = QtWidgets.QWidget()
        self.tab_meloculesdata.setObjectName("tab_meloculesdata")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.tab_meloculesdata)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.Tab_res.addTab(self.tab_meloculesdata, "")
        self.horizontalLayout_utils_res.addWidget(self.Tab_res)
        self.horizontalLayout_utils_res.setStretch(0, 4)
        self.horizontalLayout_utils_res.setStretch(1, 6)



        self.verticalLayout_utilres_status.addLayout(self.horizontalLayout_utils_res)
        # Status area restored with titled group box
        self.groupBox_status = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_status.setObjectName("groupBox_status")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_status)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowser_status = QtWidgets.QTextBrowser(self.groupBox_status)
        self.textBrowser_status.setObjectName("textBrowser_status")
        try:
            self.groupBox_status.setMaximumHeight(90)
            self.textBrowser_status.setMaximumHeight(30)
        except Exception:
            pass
        self.verticalLayout_9.addWidget(self.textBrowser_status)
        self.verticalLayout_utilres_status.addWidget(self.groupBox_status)
        self.verticalLayout_utilres_status.setStretch(0, 9)
        self.verticalLayout_utilres_status.setStretch(1, 1)
        self.verticalLayout_19.addLayout(self.verticalLayout_utilres_status)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1614, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.Tab_res.setCurrentIndex(0)
        self.button_predict.clicked.connect(MainWindow.predict) # type: ignore
        self.button_extract_features.clicked.connect(MainWindow.extractScopeFeatures) # type: ignore
        self.buttonn_save.clicked.connect(MainWindow.getSavePath)
        self.buttonn_clean.clicked.connect(MainWindow.clean)
        self.button_load_result.clicked.connect(MainWindow.loadResultFile) # type: ignore
        self.pushButton_select_file.clicked.connect(MainWindow.selectFile) # type: ignore
        self.pushButton_select_fasta.clicked.connect(MainWindow.selectFastaFile) # type: ignore
        
        self.LineEdit_chain.textChanged.connect(MainWindow.validate_chain_input)
        self.LineEdit_num_workers.textChanged.connect(MainWindow.validate_num_workers_input)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SCOPE — Catalytic Site Prediction"))
        self.groupBox_input.setTitle(_translate("MainWindow", "Input: FASTA and PDB"))
        self.pushButton_select_file.setText(_translate("MainWindow", "Select PDB"))
        self.filename_fasta.setPlaceholderText(
            _translate("MainWindow", "Required for catalytic prediction; header protein ID (e.g. >1chu-A)")
        )
        self.pushButton_select_fasta.setText(_translate("MainWindow", "Select FASTA"))

        self.groupBox_feature_extract.setTitle(_translate("MainWindow", "Step 1: Feature extraction"))
        self.label_feature.setText(
            _translate(
                "MainWindow",
                "Select FASTA and PDB above, then extract and cache features (PSSM, DSSP, ProtT5, etc.; may take long).",
            )
        )
        self.button_extract_features.setText(_translate("MainWindow", "Extract features"))
        self.label_feature_hint.setText(
            _translate("MainWindow", "Do not run Predict until feature extraction is done.")
        )

        self.groupBox_catalytic.setTitle(_translate("MainWindow", "Step 2: Catalytic site prediction"))
        self.label_catalytic.setText(
            _translate(
                "MainWindow",
                "Complete Step 1 first. Predict below loads cached features and runs inference only.",
            )
        )
        self.label_catalytic_hint.setText(
            _translate("MainWindow", "Use together with Step 1 after features are ready.")
        )

        # Step 1 / Step 2：始终展开，不折叠
        try:
            self.widget_feature_body.setVisible(True)
            self.widget_catalytic_body.setVisible(True)
            self.label_feature_hint.setVisible(False)
            self.label_catalytic_hint.setVisible(False)
        except Exception:
            pass

        try:
            self.groupBox_parameters.mousePressEvent = lambda e: self._toggle_group_body(self.widget_parameters_body)
        except Exception:
            pass
        self.groupBox_parameters.setTitle(_translate("MainWindow", "Paramenters"))
        self.label_5.setText(_translate("MainWindow", "Num_workers:"))
        self.label_6.setText(_translate("MainWindow", "Chain (A/B/...):"))
        
        self.groupBox_operator.setTitle(_translate("MainWindow", "Operator"))
        self.button_predict.setText(_translate("MainWindow", "Predict"))
        self.buttonn_save.setText(_translate("MainWindow", "Save results"))
        self.buttonn_clean.setText(_translate("MainWindow", "Clean"))
        self.button_load_result.setText(_translate("MainWindow", "Load result file"))
        # Results group removed; tabs are placed directly
        self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_meloculesdata), _translate("MainWindow", "Prediction"))
        self.groupBox_status.setTitle(_translate("MainWindow", "Status"))
    
    def show_tabSon_meloculesdata(self):
        # 重建嵌套 Tab 时丢弃旧的 Plot 页引用，避免指向已删除的 Qt 对象
        for _plot_attr in (
            "lineEdit_threshold",
            "label_threshold",
            "button_update_network",
            "horizontalLayout_threshold",
            "verticalLayout_tab_summaryplot",
            "tabItem_plot",
            "frame_plot",
            "label_plot",
        ):
            if hasattr(self, _plot_attr):
                setattr(self, _plot_attr, None)

        self.tabSon_meloculesdata = QtWidgets.QTabWidget(self.tab_meloculesdata)
        self.tabSon_meloculesdata.setObjectName("tabSon_meloculesdata")
        self.tabItem_alldata = QtWidgets.QWidget()
        self.tabItem_alldata.setObjectName("tabItem_alldata")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tabItem_alldata)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.table_alldata = QtWidgets.QTableWidget(self.tabItem_alldata)
        self.table_alldata.setObjectName("table_alldata")
        self.verticalLayout_12.addWidget(self.table_alldata)
        self.tabSon_meloculesdata.addTab(self.tabItem_alldata, "Results")
        # self.tabItem_singlemelocule = QtWidgets.QWidget()
        # self.tabItem_singlemelocule.setObjectName("tabItem_singlemelocule")
        # self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.tabItem_singlemelocule)
        # self.verticalLayout_21.setObjectName("verticalLayout_21")
        # self.label_selectmelocule = QtWidgets.QLabel(self.tabItem_singlemelocule)
        # self.label_selectmelocule.setObjectName("label_selectmelocule")
        # self.verticalLayout_21.addWidget(self.label_selectmelocule)
        # self.label_selectmelocule.setText("Select Melocule by Id")
        # self.comboBox_selectMelocule = QtWidgets.QComboBox(self.tabItem_singlemelocule)
        # self.comboBox_selectMelocule.setObjectName("comboBox_selectMelocule")
        # self.verticalLayout_21.addWidget(self.comboBox_selectMelocule)
        



        # self.scrollArea_single = QtWidgets.QScrollArea(self.tabItem_singlemelocule)
        # self.scrollArea_single.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scrollArea_single.setWidgetResizable(True)
        # self.scrollArea_single.setObjectName("scrollArea_single")
        self.scrollAreaWidgetContents_single = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_single.setGeometry(QtCore.QRect(0, 0, 867, 849))
        self.scrollAreaWidgetContents_single.setObjectName("scrollAreaWidgetContents_single")
        
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_single)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        
        # self.frame_image = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        # self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_image.setObjectName("frame_image")
        # self.horizontalLayout_22 = QtWidgets.QVBoxLayout(self.frame_image)
        # self.horizontalLayout_22.setObjectName("verticalLayout_22")
        # self.label_image = QtWidgets.QLabel(self.frame_image)
        # self.label_image.setObjectName("label_image")
        # self.horizontalLayout_22.addWidget(self.label_image)
        # self.verticalLayout_14.addWidget(self.frame_image)
        

        self.frame_image = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_image.sizePolicy().hasHeightForWidth())
        self.frame_image.setSizePolicy(sizePolicy)
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_image)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_image_1 = QtWidgets.QLabel(self.frame_image)
        self.label_image_1.setObjectName("label_image_1")
        self.label_image_1.setScaledContents(True)
        self.label_image_1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.horizontalLayout_10.addWidget(self.label_image_1)
        self.label_image_2 = QtWidgets.QLabel(self.frame_image)
        self.label_image_2.setObjectName("label_image_2")
        self.label_image_2.setScaledContents(True)
        self.label_image_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.horizontalLayout_10.addWidget(self.label_image_2)
        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 5)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_14.addWidget(self.frame_image)



        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_PhyChe = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_PhyChe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_PhyChe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_PhyChe.setObjectName("frame_PhyChe")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_PhyChe)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_phyche = QtWidgets.QLabel(self.frame_PhyChe)
        self.label_phyche.setObjectName("label_phyche")
        self.label_phyche.setText("Physicochemical")
        self.verticalLayout_13.addWidget(self.label_phyche)
        self.table_Phyche = QtWidgets.QTableWidget(self.frame_PhyChe)
        self.table_Phyche.setObjectName("table_Phyche")
        self.verticalLayout_13.addWidget(self.table_Phyche)
        self.horizontalLayout_7.addWidget(self.frame_PhyChe)
        self.frame_absorption = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_absorption.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_absorption.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_absorption.setObjectName("frame_absorption")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_absorption)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_absorption = QtWidgets.QLabel(self.frame_absorption)
        self.label_absorption.setObjectName("label_absorption")
        self.label_absorption.setText("Absorption")
        self.verticalLayout_15.addWidget(self.label_absorption)
        self.table__absorption = QtWidgets.QTableWidget(self.frame_absorption)
        self.table__absorption.setObjectName("table__absorption")
        self.verticalLayout_15.addWidget(self.table__absorption)
        self.horizontalLayout_7.addWidget(self.frame_absorption)
        self.frame_distribution = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_distribution.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_distribution.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_distribution.setObjectName("frame_distribution")
        self.verticalLayout_frame_distribution = QtWidgets.QVBoxLayout(self.frame_distribution)
        self.verticalLayout_frame_distribution.setObjectName("verticalLayout_frame_distribution")
        self.label_distribution = QtWidgets.QLabel(self.frame_distribution)
        self.label_distribution.setObjectName("label_distribution")
        self.verticalLayout_frame_distribution.addWidget(self.label_distribution)
        self.label_distribution.setText("Distribution")
        self.table_distribution = QtWidgets.QTableWidget(self.frame_distribution)
        self.table_distribution.setObjectName("table_distribution")
        self.verticalLayout_frame_distribution.addWidget(self.table_distribution)
        self.horizontalLayout_7.addWidget(self.frame_distribution)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_metabolism = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_metabolism.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_metabolism.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_metabolism.setObjectName("frame_metabolism")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_metabolism)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_metabolism = QtWidgets.QLabel(self.frame_metabolism)
        self.label_metabolism.setObjectName("label_metabolism")
        self.verticalLayout_16.addWidget(self.label_metabolism)
        self.label_metabolism.setText("Metabolism")
        self.table_metabolism = QtWidgets.QTableWidget(self.frame_metabolism)
        self.table_metabolism.setObjectName("table_metabolism")
        self.verticalLayout_16.addWidget(self.table_metabolism)
        self.horizontalLayout_9.addWidget(self.frame_metabolism)
        self.frame_excretion = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_excretion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_excretion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_excretion.setObjectName("frame_excretion")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_excretion)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_excretion = QtWidgets.QLabel(self.frame_excretion)
        self.label_excretion.setObjectName("label_excretion")
        self.label_excretion.setText("Excretion")
        self.verticalLayout_18.addWidget(self.label_excretion)
        self.table_excretion = QtWidgets.QTableWidget(self.frame_excretion)
        self.table_excretion.setObjectName("table_excretion")
        self.verticalLayout_18.addWidget(self.table_excretion)
        self.horizontalLayout_9.addWidget(self.frame_excretion)
        self.frame_toxicity = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_toxicity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toxicity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toxicity.setObjectName("frame_toxicity")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_toxicity)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_toxicity = QtWidgets.QLabel(self.frame_toxicity)
        self.label_toxicity.setObjectName("label_toxicity")
        self.verticalLayout_17.addWidget(self.label_toxicity)
        self.label_toxicity.setText("Toxicity")
        self.table_toxicity = QtWidgets.QTableWidget(self.frame_toxicity)
        self.table_toxicity.setObjectName("table_toxicity")
        self.verticalLayout_17.addWidget(self.table_toxicity)
        self.horizontalLayout_9.addWidget(self.frame_toxicity)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.verticalLayout_14.setStretch(0, 9)
        self.verticalLayout_14.setStretch(1, 10)
        self.verticalLayout_14.setStretch(2, 10)
        # self.tabSon_meloculesdata.addTab(self.tabItem_singlemelocule, "Single Melocule")
        self.verticalLayout_20.addWidget(self.tabSon_meloculesdata)
        # self.comboBox_selectMelocule.currentTextChanged.connect(self.show_single_melocule)

        self.table_Phyche.resizeColumnsToContents()
        self.table__absorption.resizeColumnsToContents()
        self.table_distribution.resizeColumnsToContents()
        self.table_metabolism.resizeColumnsToContents()
        self.table_excretion.resizeColumnsToContents()
        self.table_toxicity.resizeColumnsToContents()

        # self.show_preds_plot()

        # self.scrollArea_single.setWidget(self.scrollAreaWidgetContents_single)
        # self.verticalLayout_21.addWidget(self.scrollArea_single)
        # self.verticalLayout_14.setStretch(0,2)
        # self.verticalLayout_14.setStretch(1,5)
        # self.verticalLayout_14.setStretch(2,5)
        # 降低最小高度，便于整体窗口上下缩放
        self.scrollAreaWidgetContents_single.setMinimumSize(600,1200)

        # 调节scrollArea中的控件大小
        
        # self.frame_image.setGeometry(9,9,100,100)
        # self.frame_PhyChe.setGeometry(1,1,250,448)
        # self.frame_absorption.setGeometry(257,1,250,448)
        # self.frame_distribution.setGeometry(512,1,250,448)
        # self.frame_metabolism.setGeometry(257,1,250,448)
        # self.frame_excretion.setGeometry(1,1,250,448)
        # self.frame_toxicity.setGeometry(512,1,250,448)
        



        
        
        # self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_meloculesdata), _translate("MainWindow", "Melocules Data"))

from PyQt5.QtWidgets import QTreeWidgetItem, QSizePolicy
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QInputDialog, QTableWidget, QTableWidgetItem, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QTextEdit, QDialog
from PyQt5.QtGui import QPixmap
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# 尝试导入PyQtWebEngine，如果失败则使用备用方案
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    WEBENGINE_AVAILABLE = True
except ImportError:
    WEBENGINE_AVAILABLE = False
    print("Warning: PyQtWebEngine is not installed; 3D view will use an external browser.")
from pathlib import Path



import pandas as pd
import numpy as np
import pickle
import json
import os
import subprocess
import tempfile
import datetime

from typing import Dict, List, Optional, Set
import re
from Bio import SeqIO

# SCOPE 催化位点：残基得分 ≥ 该阈值则 Pre_label=1
CATALYTIC_THRESHOLD = 0.5

try:
    from SCOPE_GUI_infer import (
        DATA_DIR as SCOPE_DATA_DIR,
        check_scope_features_ready,
        extract_features_and_cache_from_fasta_pdb,
        load_fasta_sequences,
        predict_results_for_protein_list,
    )
except ImportError:
    SCOPE_DATA_DIR = None
    check_scope_features_ready = None
    extract_features_and_cache_from_fasta_pdb = None
    load_fasta_sequences = None
    predict_results_for_protein_list = None


def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
        else:
            clear_layout(item.layout())

class NumericSortProxyModel(QSortFilterProxyModel):
    """Custom sort proxy for numerical column sorting"""
    def lessThan(self, left, right):
        left_data = left.data(QtCore.Qt.UserRole)
        right_data = right.data(QtCore.Qt.UserRole)
        
        # If both data have UserRole (numerical), compare by value
        if left_data is not None and right_data is not None:
            try:
                return float(left_data) < float(right_data)
            except (ValueError, TypeError):
                pass
        
        # Otherwise compare by default string
        return super().lessThan(left, right)
   
class MyDesigner(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textBrowser_status.setText(
            "\nWelcome to SCOPE catalytic site prediction: run Extract features first, then Predict."
        )
        self.predicting = False
        self.extracting_features = False
        # # 启用系统标题栏按钮并取消无边框，确保显示最小化/最大化/关闭
        # try:
        #     self.setWindowFlag(QtCore.Qt.FramelessWindowHint, False)
        #     self.setWindowFlag(QtCore.Qt.WindowTitleHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowSystemMenuHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        #     # 重新应用窗口装饰
        #     self.showNormal()
        # except Exception:
        #     pass
        # #（移除旧的 Task 初始化）

    def selectFile(self):
        filePath,_ = QFileDialog.getOpenFileName(self.filename, "Open Files")
        self.filename.setText(filePath)
        
        # 设置PDB文件路径
        if filePath:
            self.pdb_path = filePath
            self.textBrowser_status.setText(f"\nPDB file selected: {filePath}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

    def selectFastaFile(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            "Select FASTA",
            "",
            "FASTA (*.fa *.fasta *.faa);;All files (*)",
        )
        if filePath:
            self.filename_fasta.setText(filePath)
            self.textBrowser_status.append(f"\nFASTA selected: {filePath}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

    def _scope_fasta_path(self) -> str:
        if hasattr(self, "filename_fasta") and self.filename_fasta.text().strip():
            return self.filename_fasta.text().strip()
        return ""

    def _aa_from_infer_line(self, protein_id: str, position: int) -> str:
        """从 InferResult/<protein_id> 第 position 行读取单字母氨基酸（与推理输出首列一致）。"""
        if not SCOPE_DATA_DIR or position < 1:
            return ""
        fp = os.path.join(SCOPE_DATA_DIR, "InferResult", protein_id)
        if not os.path.isfile(fp):
            return ""
        try:
            with open(fp, "r") as f:
                for idx, line in enumerate(f):
                    if idx + 1 != position:
                        continue
                    parts = line.strip().split("\t")
                    if not parts:
                        return ""
                    return str(parts[0]).strip()[:1] or ""
        except OSError:
            return ""
        return ""

    def _build_scope_catalytic_dataframe(
        self,
        protein_list: List[str],
        prot_seq: Optional[Dict[str, str]] = None,
    ) -> pd.DataFrame:
        """将 SCOPE_data/InferResult/<prot> 转为与表格兼容的 DataFrame（含各位点氨基酸，来自推理文件首列）。"""
        if not SCOPE_DATA_DIR:
            return pd.DataFrame(
                columns=["Proteases", "Protein|position", "AA", "Pre_Score", "Pre_label"]
            )
        infer_dir = os.path.join(SCOPE_DATA_DIR, "InferResult")
        rows: List[dict] = []
        for prot in protein_list:
            fp = os.path.join(infer_dir, prot)
            if not os.path.isfile(fp):
                continue
            with open(fp, "r") as f:
                for idx, line in enumerate(f):
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("\t")
                    if len(parts) < 2:
                        continue
                    try:
                        sc = float(parts[1])
                    except ValueError:
                        continue
                    pos = idx + 1
                    aa = str(parts[0]).strip()[:1] or ""
                    if not aa and prot_seq and prot in prot_seq:
                        s = prot_seq[prot]
                        if 1 <= pos <= len(s):
                            aa = s[pos - 1]
                    rows.append(
                        {
                            "Protease": "Catalytic_site",
                            "Protein|position": f"{prot}|{pos}",
                            "AA": aa,
                            "Pre_Score": sc,
                            "Pre_label": 1 if sc >= CATALYTIC_THRESHOLD else 0,
                        }
                    )
        if not rows:
            return pd.DataFrame(
                columns=["Proteases", "Protein|position", "AA", "Pre_Score", "Pre_label"]
            )
        return pd.DataFrame(rows)

    def _end_predict_session(self):
        self.predicting = False
        try:
            self.LineEdit_chain.textChanged.connect(self.validate_chain_input)
        except Exception:
            pass
        try:
            self.LineEdit_num_workers.textChanged.connect(self.validate_num_workers_input)
        except Exception:
            pass
        self.button_predict.setEnabled(True)
        if hasattr(self, "button_extract_features"):
            self.button_extract_features.setEnabled(True)

    def _end_extract_session(self):
        self.extracting_features = False
        if hasattr(self, "button_extract_features"):
            self.button_extract_features.setEnabled(True)
        if hasattr(self, "button_predict"):
            self.button_predict.setEnabled(True)

    def extractScopeFeatures(self):
        """第一步：仅提取并缓存特征（不运行预测）。"""
        from PyQt5.QtWidgets import QMessageBox

        if self.extracting_features or self.predicting:
            return
        if extract_features_and_cache_from_fasta_pdb is None:
            self.textBrowser_status.append("\nError: Could not load SCOPE_GUI_infer.")
            return

        vr = self._validate_scope_inputs_dict()
        if not vr["valid"]:
            self.textBrowser_status.setText(vr["message"])
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return

        fasta_scope = self._scope_fasta_path()
        pdb_path = str(Path(self.filename.text().strip()))
        reply = QMessageBox.question(
            self,
            "Step 1: Feature extraction",
            "This will run PSSM, DSSP, ProtT5, etc., and may take a long time.\n"
            "If cached features already match the current PDB, redundant work will be skipped.\n\nStart now?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,
        )
        if reply == QMessageBox.No:
            self.textBrowser_status.append("\nFeature extraction cancelled.")
            return

        self.extracting_features = True
        self.button_extract_features.setEnabled(False)
        self.button_predict.setEnabled(False)
        self.textBrowser_status.setText("\nExtracting features, please wait…")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        QtWidgets.QApplication.processEvents()

        try:

            def _cb(msg: str):
                self.textBrowser_status.append("\n" + msg)
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                QtWidgets.QApplication.processEvents()

            extract_features_and_cache_from_fasta_pdb(
                fasta_scope,
                pdb_path,
                status_callback=_cb,
            )
            self.textBrowser_status.append(
                "\nStep 1 finished: features are ready. Open Step 2 and click Predict."
            )
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        except Exception as e:
            self.textBrowser_status.append(f"\nFeature extraction failed: {e}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        finally:
            self._end_extract_session()

    def _validate_scope_inputs_dict(self):
        """与 validate_parameters 中 SCOPE 分支一致，返回 dict。"""
        fasta_scope = self._scope_fasta_path()
        if not fasta_scope:
            return {"valid": False, "message": "Error: Please select both FASTA and PDB."}
        if extract_features_and_cache_from_fasta_pdb is None:
            return {"valid": False, "message": "Error: Could not load SCOPE_GUI_infer."}
        fasta_file = Path(fasta_scope)
        if not fasta_file.exists():
            return {"valid": False, "message": f"Error: FASTA not found: {fasta_file}"}
        if fasta_file.suffix.lower() not in [".fa", ".fasta", ".faa"]:
            return {
                "valid": False,
                "message": f"Error: FASTA must use .fa / .fasta / .faa; got: {fasta_file.suffix}",
            }
        if not self.filename.text() or not self.filename.text().strip():
            return {"valid": False, "message": "Error: Both PDB and FASTA are required."}
        pdb_file = Path(self.filename.text().strip())
        if not pdb_file.exists():
            return {"valid": False, "message": f"Error: PDB not found: {pdb_file}"}
        if pdb_file.suffix.lower() not in [".pdb", ".ent"]:
            return {
                "valid": False,
                "message": f"Error: PDB must be .pdb or .ent; got: {pdb_file.suffix}",
            }
        return {"valid": True, "message": ""}

    def loadResultFile(self):
        """Load local result file"""
        filePath, _ = QFileDialog.getOpenFileName(
            self, 
            "Select Result File", 
            "", 
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if filePath:
            try:
                # 读取CSV文件
                self.data_with_preds = pd.read_csv(filePath)
                
                # 显示加载成功信息
                self.textBrowser_status.setText(f"\nSuccessfully loaded result file: {filePath}")
                self.textBrowser_status.setText(f"\nData shape: {self.data_with_preds.shape}")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                
                # 确保表格控件已创建
                if not hasattr(self, "tabSon_meloculesdata") or self.tabSon_meloculesdata is None:
                    self.textBrowser_status.setText("\nCreating table controls...")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    self.show_tabSon_meloculesdata()
                # elif not self._plot_controls_alive():
                #     self.show_preds_plot()

                # 显示结果表格
                self.textBrowser_status.setText("\nDisplaying table data...")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                self.show_preds_table()
                
                self.textBrowser_status.setText("\nFile loading completed successfully!")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                
            except Exception as e:
                self.textBrowser_status.setText(f"\nError loading file: {str(e)}")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

    def _toggle_group_body(self, body_widget: QtWidgets.QWidget):
        """切换分组内部主体可见性（折叠/展开）"""
        try:
            body_widget.setVisible(not body_widget.isVisible())
        except Exception:
            pass

    def clean(self):
        # 清理动态创建的控件引用
        if hasattr(self, 'comboBox_protein_pos'):
            self.comboBox_protein_pos = None
        if hasattr(self, 'horizontalLayout_filter'):
            self.horizontalLayout_filter = None
        if hasattr(self, 'button_save_table'):
            self.button_save_table = None
        if hasattr(self, 'lineEdit_threshold'):
            self.lineEdit_threshold = None
        if hasattr(self, 'label_threshold'):
            self.label_threshold = None
        if hasattr(self, 'button_update_network'):
            self.button_update_network = None
        if hasattr(self, 'button_zoom_plot'):
            self.button_zoom_plot = None
        if hasattr(self, 'button_save_plot'):
            self.button_save_plot = None
        if hasattr(self, 'horizontalLayout_threshold'):
            self.horizontalLayout_threshold = None
        if hasattr(self, 'verticalLayout_tab_summaryplot'):
            self.verticalLayout_tab_summaryplot = None
        if hasattr(self, 'frame_plot'):
            self.frame_plot = None
        if hasattr(self, 'label_plot'):
            self.label_plot = None
        if hasattr(self, 'verticalLayout_frameplot'):
            self.verticalLayout_frameplot = None
        if hasattr(self, 'tabSon_meloculesdata'):
            self.tabSon_meloculesdata = None
        if hasattr(self, 'table_alldata'):
            self.table_alldata = None
        
        # 清理数据
        if hasattr(self, 'data_with_preds'):
            self.data_with_preds = None
    
        # 删除已经删除的 Qt 对象的引用
        self.centralwidget.deleteLater()
        self.centralwidget = None
        self.layout = None
        self.label = None
        self.combo_box = None
        self.button = None

        # 重新初始化界面
        self.setupUi(self)
        self.show_tabSon_meloculesdata()
        try:
            self.LineEdit_atc_code.setReadOnly(False)
            self.LineEdit_possr.setReadOnly(False)
        except Exception:
            pass

    def on_task_mode_changed(self):
        """已弃用：保留空实现以防信号残留"""
        return

    def getSavePath(self):
        time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        savePath = QFileDialog.getExistingDirectory(self, "Save Results")
        # savePath, ok = QInputDialog.getText(self, "Save Results", "Input Path")
        #if ok:
        self.save_path = Path(savePath+f'/predict_results_{time_str}.csv')
        self.data_with_preds.to_csv(self.save_path)
        self.textBrowser_status.setText("\nThe result has been saved to"+ savePath+f"/predict_results_{time_str}.csv !")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def validate_parameters(self):
        """Validate all required parameters before prediction"""
        fasta_scope = self._scope_fasta_path()
        if fasta_scope:
            if extract_features_and_cache_from_fasta_pdb is None or check_scope_features_ready is None:
                return {
                    "valid": False,
                    "message": "Error: Could not load SCOPE_GUI_infer (catalytic-site prediction unavailable).",
                }
            fasta_file = Path(fasta_scope)
            if not fasta_file.exists():
                return {"valid": False, "message": f"Error: FASTA not found: {fasta_file}"}
            if fasta_file.suffix.lower() not in [".fa", ".fasta", ".faa"]:
                return {
                    "valid": False,
                    "message": f"Error: FASTA must use .fa / .fasta / .faa; got: {fasta_file.suffix}",
                }
            if not self.filename.text() or not self.filename.text().strip():
                return {"valid": False, "message": "Error: Both PDB and FASTA are required."}
            pdb_file = Path(self.filename.text().strip())
            if not pdb_file.exists():
                return {"valid": False, "message": f"Error: PDB not found: {pdb_file}"}
            if pdb_file.suffix.lower() not in [".pdb", ".ent"]:
                return {
                    "valid": False,
                    "message": f"Error: PDB must be .pdb or .ent; got: {pdb_file.suffix}",
                }
            ok, _, err = check_scope_features_ready(fasta_scope, str(pdb_file))
            if not ok:
                return {
                    "valid": False,
                    "message": err
                    or "Error: Feature extraction is not done or the current PDB does not match the cache. Run Extract features first.",
                }
            return {"valid": True, "message": "Ready for Step 2 prediction."}

        # Check PDB file selection
        if not self.filename.text() or self.filename.text().strip() == "":
            return {
                'valid': False,
                'message': "Error: Please select a PDB file first!"
            }
        
        # Check if PDB file exists
        pdb_file = Path(self.filename.text())
        if not pdb_file.exists():
            return {
                'valid': False,
                'message': f"Error: PDB file does not exist: {pdb_file}"
            }
        
        # Check file extension
        if not pdb_file.suffix.lower() in ['.pdb', '.ent']:
            return {
                'valid': False,
                'message': f"Error: Invalid file format. Please select a PDB file (.pdb or .ent), got: {pdb_file.suffix}"
            }
        
        atc_code = self.LineEdit_atc_code.text().strip()
        if not atc_code:
            return {
                'valid': False,
                'message': "Warning: No protease selected. Please select at least one protease."
            }
        
        proteases_list = [x.strip() for x in atc_code.split(',') if x.strip()]
        if proteases_list:
            for protease in proteases_list:
                if not protease or len(protease) < 3:
                    return {
                        'valid': False,
                        'message': f"Error: Invalid protease ID format: '{protease}'. Please check your selection."
                    }
        
        # Check chain parameter
        chain = self.LineEdit_chain.text().strip()
        if not chain:
            return {
                'valid': False,
                'message': "Error: Chain parameter cannot be empty. Please specify a chain (e.g., A, B, C)."
            }
        
        # Validate chain format (should be single letter)
        if len(chain) != 1 or not chain.isalpha():
            return {
                'valid': False,
                'message': f"Error: Invalid chain format: '{chain}'. Chain should be a single letter (e.g., A, B, C)."
            }
        
        # Check positions parameter (optional but validate format if provided)
        possr = self.LineEdit_possr.text().strip()
        if possr:
            try:
                # Split by comma and validate each position
                positions = [x.strip() for x in possr.split(',') if x.strip()]
                for pos in positions:
                    pos_int = int(pos)
                    if pos_int < 1:
                        return {
                            'valid': False,
                            'message': f"Error: Invalid position value: '{pos}'. Positions should be positive integers starting from 1."
                        }
            except ValueError:
                return {
                    'valid': False,
                    'message': f"Error: Invalid positions format: '{possr}'. Please use comma-separated integers (e.g., 4,5,6)."
                }
        else:
            # 如果positions为空，给出信息提示但不阻止运行
            return {
                'valid': True,
                'message': "Info: Positions parameter is empty. The system will predict all possible positions, which may take longer computation time. To specify specific positions, enter comma-separated values like '4,5,6'."
            }
        
        # Check num_workers parameter
        num_workers_text = self.LineEdit_num_workers.text().strip()
        if num_workers_text and num_workers_text.lower() != 'none':
            try:
                num_workers = int(num_workers_text)
                if num_workers < 1:
                    return {
                        'valid': False,
                        'message': f"Error: Invalid number of workers: {num_workers}. Should be a positive integer or 'None'."
                    }
            except ValueError:
                return {
                    'valid': False,
                    'message': f"Error: Invalid number of workers format: '{num_workers_text}'. Should be an integer or 'None'."
                }
        
        # All validations passed
        return {
            'valid': True,
            'message': "All parameters validated successfully."
        }
    
    def validate_chain_input(self):
        """Real-time validation for chain input"""
        chain = self.LineEdit_chain.text().strip()
        if chain and (len(chain) != 1 or not chain.isalpha()):
            # 设置样式提示错误
            self.LineEdit_chain.setStyleSheet("border: 2px solid red;")
            self.textBrowser_status.setText(f"Warning: Invalid chain format: '{chain}'. Should be a single letter (e.g., A, B, C).")
        else:
            # 清除错误样式
            self.LineEdit_chain.setStyleSheet("")
            if chain:
                # 只在非预测状态下显示验证信息
                # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
                if not hasattr(self, 'predicting') or not self.predicting:
                    self.textBrowser_status.setText("Chain parameter looks good.")
    
    def validate_positions_input(self):
        """Real-time validation for positions input"""
        possr = self.LineEdit_possr.text().strip()
        if possr:
            try:
                positions = [x.strip() for x in possr.split(',') if x.strip()]
                for pos in positions:
                    pos_int = int(pos)
                    if pos_int < 1:
                        self.LineEdit_possr.setStyleSheet("border: 2px solid red;")
                        self.textBrowser_status.setText(f"Warning: Invalid position value: '{pos}'. Should be positive integers starting from 1.")
                        return
                self.LineEdit_possr.setStyleSheet("")
                # 只在非预测状态下显示验证信息
                # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
                if not hasattr(self, 'predicting') or not self.predicting:
                    self.textBrowser_status.setText("Positions parameter looks good.")

            except ValueError:
                self.LineEdit_possr.setStyleSheet("border: 2px solid red;")
                self.textBrowser_status.setText(f"Warning: Invalid positions format: '{possr}'. Use comma-separated integers (e.g., 4,5,6).")
        else:
            self.LineEdit_possr.setStyleSheet("")
            # 只在非预测状态下显示验证信息
            # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
            if not hasattr(self, 'predicting') or not self.predicting:
                self.textBrowser_status.setText("Info: Positions parameter is empty. The system will predict all possible positions, which may take longer computation time.")
    
    def validate_num_workers_input(self):
        """Real-time validation for num_workers input"""
        num_workers_text = self.LineEdit_num_workers.text().strip()
        if num_workers_text and num_workers_text.lower() != 'none':
            try:
                num_workers = int(num_workers_text)
                if num_workers < 1:
                    self.LineEdit_num_workers.setStyleSheet("border: 2px solid red;")
                    self.textBrowser_status.setText(f"Warning: Invalid number of workers: {num_workers}. Should be a positive integer or 'None'.")
                else:
                    self.LineEdit_num_workers.setStyleSheet("")
                    # 只在非预测状态下显示验证信息
                    # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
                    if not hasattr(self, 'predicting') or not self.predicting:
                        self.textBrowser_status.setText("Number of workers parameter looks good.")

            except ValueError:
                self.LineEdit_num_workers.setStyleSheet("border: 2px solid red;")
                self.textBrowser_status.setText(f"Warning: Invalid number of workers format: '{num_workers_text}'. Should be an integer or 'None'.")
        else:
            self.LineEdit_num_workers.setStyleSheet("")
    
    def predict(self):
        # 先禁用预测按钮，防止重复点击
        self.button_predict.setEnabled(False)

        # 设置预测状态标志
        self.predicting = True

        # 暂时断开验证信号连接，防止覆盖Status信息
        try:
            self.LineEdit_chain.textChanged.disconnect(self.validate_chain_input)
        except:
            pass
        try:
            self.LineEdit_possr.textChanged.disconnect(self.validate_positions_input)
        except:
            pass
        try:
            self.LineEdit_num_workers.textChanged.disconnect(self.validate_num_workers_input)
        except:
            pass

        # 显示预测开始提示
        self.textBrowser_status.setText("\nPrediction in progress, please wait...")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        # 立刻刷新事件循环，确保提示在耗时计算前显示
        QtWidgets.QApplication.processEvents()
        
        # 运行前判断参数是否完整
        validation_result = self.validate_parameters()
        if not validation_result['valid']:
            self.textBrowser_status.setText(f"\n{validation_result['message']}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            self._end_predict_session()
            return
        
        # 首次运行后组件显示
        if not hasattr(self, "tabSon_meloculesdata") or self.tabSon_meloculesdata is None:
            self.show_tabSon_meloculesdata()
        # elif not self._plot_controls_alive():
        #     self.show_preds_plot()

        fasta_scope = self._scope_fasta_path()
        if fasta_scope:
            if hasattr(self, "button_extract_features"):
                self.button_extract_features.setEnabled(False)
            self.pdb_path = str(Path(self.filename.text().strip()))
            try:

                def _scope_status_cb(msg: str):
                    self.textBrowser_status.append("\n" + msg)
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    QtWidgets.QApplication.processEvents()

                ok, protein_list, err = check_scope_features_ready(fasta_scope, self.pdb_path)
                if not ok:
                    raise RuntimeError(
                        err
                        or "Features not ready: run Extract features first and keep the same FASTA/PDB as when extracting."
                    )
                self.textBrowser_status.append(
                    "\nStep 2: Loading cached features and running model inference …"
                )
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                QtWidgets.QApplication.processEvents()
                predict_results_for_protein_list(
                    protein_list,
                    status_callback=_scope_status_cb,
                )
                self.data_with_preds = self._build_scope_catalytic_dataframe(protein_list)
                if self.data_with_preds is None or self.data_with_preds.empty:
                    raise RuntimeError(
                        "Inference output is empty. Check FASTA header protein IDs, PDB chain vs FASTA, and SCOPE_data/InferResult."
                    )
                self.textBrowser_status.append(
                    f"\nCatalytic rule: CATALYTIC_THRESHOLD = {CATALYTIC_THRESHOLD} (Pre_label = 1 when Pre_Score ≥ this value)."
                )
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                self.show_preds_table()
            except Exception as e:
                self.textBrowser_status.append(f"\nSCOPE prediction failed: {e}")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            finally:
                self._end_predict_session()
            return

        if hasattr(self, "button_extract_features"):
            self.button_extract_features.setEnabled(False)

        self.data_path = Path(self.filename.text())
        self.atc_code = self.LineEdit_atc_code.text()
        # 解析为列表
        self.proteases_list = [x.strip() for x in self.atc_code.split(',') if x.strip()]
        # print("self.atc_code",self.atc_code)
        # print("self.proteases_list",self.proteases_list)
        # self.smile_column = self.LineEdit_smile_column.text()
        #self.include_physchem = self.LineEdit_include_physchem.text()
        # print(self.LineEdit_num_workers.text())
        self.num_workers = None if self.LineEdit_num_workers.text()=='None' else int(self.LineEdit_num_workers.text())
        self.chain = self.LineEdit_chain.text()
        self.possr = self.LineEdit_possr.text()
        
        # 获取当前脚本的绝对路径
        script_path = os.path.abspath(__file__)
        # 提取脚本所在目录
        script_dir = os.path.dirname(script_path)
        self.save_path = script_dir
        # 设置res目录路径
        self.res_path = os.path.join(script_dir, 'res')
        # print(f"script_dir: {script_dir}")
        # print(f"res_path: {self.res_path}")
        # print(f"res_path exists: {os.path.exists(self.res_path)}")
        
        # 如果res目录不存在，则创建它
        if not os.path.exists(self.res_path):
            try:
                os.makedirs(self.res_path)
                print(f"Created res directory: {self.res_path}")
            except Exception as e:
                print(f"Failed to create res directory: {e}")
                # 如果创建失败，使用当前目录
                self.res_path = script_dir
                print(f"Using script directory instead: {self.res_path}") 
        # 处理蛋白酶选择警告（如果验证通过但未选择蛋白酶）
        if not self.proteases_list:
            self.textBrowser_status.append("\nNo protease selected, using all proteases!")
            # 继续执行，不返回
        
        # 检查possr参数
        if not self.possr or self.possr.strip() == "":
            self.textBrowser_status.append("\nInfo: Positions parameter is empty. The system will predict all possible positions.")
            self.textBrowser_status.append("\nNote: Predicting all positions may take longer computation time. To specify specific positions, enter comma-separated values (e.g., 4,5,6).")
            # self.textBrowser_status.append("\nTo specify specific positions, enter comma-separated values (e.g., 4,5,6).")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
            # 询问用户是否继续（默认选择Yes）
            from PyQt5.QtWidgets import QMessageBox
            reply = QMessageBox.question(
                self, 
                'Predict All Positions', 
                'The positions parameter is empty. The system will predict all possible positions.\n\nThis may take longer computation time.\n\nDo you want to continue?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes  # 默认选择Yes
            )
            
            if reply == QMessageBox.No:
                self.textBrowser_status.append("\nPrediction cancelled by user.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                self._end_predict_session()
                return
            else:
                self.textBrowser_status.append("\nContinuing with prediction of all positions...")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

        # 添加额外的参数验证
        try:

            
        # predict
            # print("self.possr",self.possr)
            # 获取PDB文件的目录路径
            pdb_dir = os.path.dirname(self.pdb_path)

            
            # 回调：将阶段性用时写入状态框
            def _status_cb(msg: str):
                """将回调消息中的 Position x / y 转换成百分比进度条"""
                try:
                    text = str(msg)
                    # 匹配 "Position {i+1} / {len(test_loader)}" 模式
                    m = re.search(r"Position\s+(\d+)\s*/\s*(\d+)", text)
                    if m:
                        cur = int(m.group(1))
                        total = int(m.group(2))
                        if total > 0:
                            pct = int(round(cur * 100 / total))
                            # 简单进度条（每#代表2%）最多50个#
                            bars = max(1, min(50, pct // 2))
                            bar_text = '#' * bars
                            self.textBrowser_status.setText(f"Progress: {bar_text} {pct}%")
                        else:
                            self.textBrowser_status.setText(text)
                    else:
                        # 非匹配信息原样输出
                        self.textBrowser_status.setText(text)
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    QtWidgets.QApplication.processEvents()
                except Exception:
                    pass

            # if Cleavage_site_prediction is None:
            #     raise RuntimeError(
            #         "Without FASTA, cleavage-site prediction requires OmniCleave, which is not installed in this environment. "
            #         "For catalytic-site prediction, provide FASTA and click Predict."
            #     )
            # self.data_with_preds = Cleavage_site_prediction(
            #     self.res_path, self.chain, 'Multi-protease', 
            #     self.data_path, pdb_dir, 'pdb', 
            #      self.atc_code, self.num_workers,self.possr,
            #      status_callback=_status_cb
            # )
            
            self.textBrowser_status.setText("\nPrediction completed successfully!")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
        except Exception as e:
            error_msg = f"\nError during prediction: {str(e)}"
            self.textBrowser_status.setText(error_msg)
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

            # 如果是possr相关错误，提供更具体的建议
            if "possr" in str(e).lower() or "position" in str(e).lower():
                self.textBrowser_status.setText(error_msg + "\n\nSuggestion: Please check the positions parameter. Try entering valid positions like '4,5,6' or leave empty for default behavior.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

            self._end_predict_session()
            return

        self.show_preds_table()

        
            

        # 状态栏显示运行过程中的异常信息
        # self.textBrowser_status.clear()
        if os.path.exists("logs.txt"):
            with open("logs.txt") as f:
                lines = f.readline()
                for line in lines:
                    self.textBrowser_status.insertPlainText(line)
        # self.textBrowser_status.insertPlainText("\nFinished!")
        # self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        
        self._end_predict_session()

    def show_preds_table(self):
        # 创建筛选控件（如果还没有创建）
        if not hasattr(self, 'comboBox_protein_pos') or self.comboBox_protein_pos is None:
            self.create_filter_controls()
        
        # 更新下拉列表选项
        self.update_filter_options()
        
        # 显示所有数据
        self.filter_and_display_data()

    def _plot_controls_alive(self) -> bool:
        le = getattr(self, "lineEdit_threshold", None)
        if le is None:
            return False
        try:
            le.text()
            return True
        except RuntimeError:
            return False

    def show_preds_plot(self):
        """Add Plot tab with threshold row (network plot not implemented in this build)."""
        if not hasattr(self, "tabSon_meloculesdata") or self.tabSon_meloculesdata is None:
            self.show_tabSon_meloculesdata()
            return
        if self._plot_controls_alive():
            return
        if self.tabSon_meloculesdata.count() >= 2:
            return

        self.tabItem_plot = QtWidgets.QWidget()
        self.tabItem_plot.setObjectName("tabItem_plot")
        self.verticalLayout_tab_summaryplot = QtWidgets.QVBoxLayout(self.tabItem_plot)
        self.verticalLayout_tab_summaryplot.setObjectName("verticalLayout_tab_summaryplot")

        self.horizontalLayout_threshold = QtWidgets.QHBoxLayout()
        self.horizontalLayout_threshold.setObjectName("horizontalLayout_threshold")
        self.label_threshold = QtWidgets.QLabel(self.tabItem_plot)
        self.label_threshold.setObjectName("label_threshold")
        self.label_threshold.setText("Score threshold:")
        self.lineEdit_threshold = QtWidgets.QLineEdit(self.tabItem_plot)
        self.lineEdit_threshold.setObjectName("lineEdit_threshold")
        self.lineEdit_threshold.setText(str(CATALYTIC_THRESHOLD))
        self.button_update_network = QtWidgets.QPushButton(self.tabItem_plot)
        self.button_update_network.setObjectName("button_update_network")
        self.button_update_network.setText("Update plot")
        self.horizontalLayout_threshold.addWidget(self.label_threshold)
        self.horizontalLayout_threshold.addWidget(self.lineEdit_threshold)
        self.horizontalLayout_threshold.addWidget(self.button_update_network)
        self.horizontalLayout_threshold.addStretch()
        self.verticalLayout_tab_summaryplot.addLayout(self.horizontalLayout_threshold)

        self.label_plot = QtWidgets.QLabel(self.tabItem_plot)
        self.label_plot.setObjectName("label_plot")
        self.label_plot.setWordWrap(True)
        self.label_plot.setText(
            "The protease network summary is not generated for SCOPE catalytic-site results. "
            "Use the Results tab and 3D View; the threshold field is kept for compatibility."
        )
        self.verticalLayout_tab_summaryplot.addWidget(self.label_plot)

        self.frame_plot = QtWidgets.QFrame(self.tabItem_plot)
        self.frame_plot.setObjectName("frame_plot")
        self.verticalLayout_frameplot = QtWidgets.QVBoxLayout(self.frame_plot)
        self.verticalLayout_frameplot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_tab_summaryplot.addWidget(self.frame_plot, stretch=1)

        self.tabSon_meloculesdata.addTab(self.tabItem_plot, "Plot")
        self.button_update_network.clicked.connect(self.update_network_plot)

        if getattr(self, "_plot_tab_signal_source", None) is not self.tabSon_meloculesdata:
            self.tabSon_meloculesdata.currentChanged.connect(self.on_tab_changed)
            self._plot_tab_signal_source = self.tabSon_meloculesdata

    def update_network_plot(self):
        """No matplotlib/network graph bundled; keep status UX only."""
        if hasattr(self, "label_plot") and self.label_plot is not None:
            self.label_plot.setText(
                "No network figure in this version. "
                "See scores in the Results table; use 3D View for structure."
            )
        self.textBrowser_status.setText("\nPlot tab: no network figure to update (simplified GUI).")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

    def create_filter_controls(self):
        """Create filter controls"""
        # 如果控件已存在且不为None，先清理
        if hasattr(self, 'horizontalLayout_filter') and self.horizontalLayout_filter is not None:
            try:
                # 清理现有布局
                while self.horizontalLayout_filter.count():
                    item = self.horizontalLayout_filter.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            except:
                pass
        
        # 创建水平布局用于筛选控件
        self.horizontalLayout_filter = QtWidgets.QHBoxLayout()
        self.horizontalLayout_filter.setObjectName("horizontalLayout_filter")
        
        # 蛋白质位置选择标签和下拉框
        self.label_protein_pos = QtWidgets.QLabel(self.tab_meloculesdata)
        self.label_protein_pos.setObjectName("label_protein_pos")
        self.label_protein_pos.setText("Select Protein Position:")
        self.horizontalLayout_filter.addWidget(self.label_protein_pos)
        
        self.comboBox_protein_pos = QtWidgets.QComboBox(self.tab_meloculesdata)
        self.comboBox_protein_pos.setObjectName("comboBox_protein_pos")
        self.comboBox_protein_pos.addItem("All")
        # Enable horizontal scrolling in dropdown
        try:
            self.comboBox_protein_pos.setView(QtWidgets.QListView())
            self.comboBox_protein_pos.view().setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.comboBox_protein_pos.view().setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
            if hasattr(self.comboBox_protein_pos.view(), 'setTextElideMode'):
                self.comboBox_protein_pos.view().setTextElideMode(QtCore.Qt.ElideNone)
        except Exception:
            pass
        self.horizontalLayout_filter.addWidget(self.comboBox_protein_pos)
        
        # 添加筛选控件到布局
        self.verticalLayout_20.insertLayout(0, self.horizontalLayout_filter)
        
        # 添加保存表格按钮
        self.button_save_table = QtWidgets.QPushButton(self.tab_meloculesdata)
        self.button_save_table.setObjectName("button_save_table")
        self.button_save_table.setText("Save Table")
        self.horizontalLayout_filter.addWidget(self.button_save_table)
        
        # 添加3Dmol.js可视化按钮
        self.button_3dmol_visualize = QtWidgets.QPushButton(self.tab_meloculesdata)
        self.button_3dmol_visualize.setObjectName("button_3dmol_visualize")
        self.button_3dmol_visualize.setText("3D View")
        self.button_3dmol_visualize.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #138496;
            }
            QPushButton:pressed {
                background-color: #117a8b;
            }
        """)
        self.horizontalLayout_filter.addWidget(self.button_3dmol_visualize)
        
        # 连接信号
        self.comboBox_protein_pos.currentTextChanged.connect(self.filter_and_display_data)
        self.button_save_table.clicked.connect(self.save_table_data)
        self.button_3dmol_visualize.clicked.connect(self.visualize_with_3dmol)
    
    def update_filter_options(self):
        """Update filter options"""
        if not hasattr(self, 'comboBox_protein_pos') or self.comboBox_protein_pos is None:
            return

        try:
            self.comboBox_protein_pos.clear()
            self.comboBox_protein_pos.addItem("All")
            if hasattr(self, 'data_with_preds') and self.data_with_preds is not None and not self.data_with_preds.empty:
                if "Protein|position" in self.data_with_preds.columns:
                    protein_positions = sorted(self.data_with_preds["Protein|position"].unique())
                    self.comboBox_protein_pos.addItems([str(x) for x in protein_positions])
        except RuntimeError:
            self.create_filter_controls()
            self.update_filter_options()
    
    def filter_and_display_data(self):
        """Filter and display data based on selection"""
        if not hasattr(self, 'data_with_preds') or self.data_with_preds is None or self.data_with_preds.empty:
            return
        
        if not hasattr(self, 'comboBox_protein_pos') or self.comboBox_protein_pos is None:
            return

        try:
            selected_protein_pos = self.comboBox_protein_pos.currentText()
        except RuntimeError:
            self.create_filter_controls()
            return

        filtered_data = self.data_with_preds.copy()

        if (
            selected_protein_pos != "All"
            and "Protein|position" in filtered_data.columns
        ):
            filtered_data = filtered_data[filtered_data["Protein|position"] == selected_protein_pos]
        
        # 显示筛选后的数据
        self.display_data_in_table(filtered_data)
        
        # 注意：网络图现在只在用户点击Plot页面时才绘制，以提高表格显示速度
    
    def display_data_in_table(self, data):
        """Display data in table"""
        # 确保表格控件存在
        if not hasattr(self, 'table_alldata'):
            if hasattr(self, 'tabSon_meloculesdata'):
                # 如果tabSon_meloculesdata存在但table_alldata不存在，重新创建
                self.show_tabSon_meloculesdata()
            else:
                print("Error: Table widget not created")
                return
        
        self.table_alldata.clear()
        
        # 处理数据：不显示 Pre_label / Proteases；将 Protein|position 拆成两列；按 Pre_Score 生成 label
        display_data = data.copy()
        
        if "Pre_label" in display_data.columns:
            display_data = display_data.drop("Pre_label", axis=1)
        
        if "Protein|position" in display_data.columns:
            protein_pos_split = display_data["Protein|position"].str.split("|", expand=True)
            if protein_pos_split.shape[1] >= 2:
                display_data["Protein"] = protein_pos_split[0]
                display_data["Position"] = protein_pos_split[1]
            display_data = display_data.drop("Protein|position", axis=1, errors="ignore")
        
        if "Proteases" in display_data.columns:
            display_data = display_data.drop("Proteases", axis=1)
        
        if "Pre_Score" in display_data.columns:
            scores = pd.to_numeric(display_data["Pre_Score"], errors="coerce").fillna(0.0)
            # Pre_Score ≥ 0.5 → label=1（催化位点），否则 0
            display_data["label"] = (scores >= CATALYTIC_THRESHOLD).astype(int)
        else:
            display_data["label"] = 0
        
        # 氨基酸单字母：优先已有 AA 列，否则从 InferResult 按 Protein + Position 补全
        if "Protein" in display_data.columns and "Position" in display_data.columns:
            def _cell_aa(row: pd.Series) -> str:
                raw = row.get("AA", "")
                if pd.notna(raw) and str(raw).strip():
                    return str(raw).strip()[:1]
                try:
                    pos_i = int(float(row["Position"]))
                except (ValueError, TypeError):
                    return ""
                return self._aa_from_infer_line(str(row["Protein"]).strip(), pos_i)

            display_data["AA"] = display_data.apply(_cell_aa, axis=1)
        
        desired_columns = ["Protein", "Position", "AA", "Pre_Score", "label"]
        existing_cols = [c for c in desired_columns if c in display_data.columns]
        display_data = display_data[existing_cols]
        
        # 设置表格属性
        colum_num = display_data.shape[1]
        index_num = display_data.shape[0]
        header = display_data.columns
        self.table_alldata.setColumnCount(colum_num)
        self.table_alldata.setRowCount(index_num)
        self.table_alldata.setHorizontalHeaderLabels(header)
        
        # 启用排序功能
        self.table_alldata.setSortingEnabled(True)
        
        # 设置自定义排序代理（如果需要更精确的数值排序）
        # 注意：QTableWidget的排序功能已经足够，这里主要是为了确保数值排序正确
        
        # 设置表格内容
        for i in range(0, index_num):
            for j in range(0, colum_num):
                value = display_data.values[i][j]
                col_name = display_data.columns[j]
                if col_name == "Pre_Score":
                    try:
                        formatted_value = f"{float(value):.3f}"
                        cell = QTableWidgetItem(formatted_value)
                        cell.setData(QtCore.Qt.UserRole, float(value))
                    except (ValueError, TypeError):
                        cell = QTableWidgetItem(str(value))
                elif col_name == "label":
                    try:
                        iv = int(value)
                        cell = QTableWidgetItem(str(iv))
                        cell.setData(QtCore.Qt.UserRole, iv)
                    except (ValueError, TypeError):
                        cell = QTableWidgetItem(str(value))
                else:
                    cell = QTableWidgetItem(str(value))
                
                self.table_alldata.setItem(i, j, cell)

    def save_table_data(self):
        """Save current table data to file"""
        # 检查是否有数据
        if not hasattr(self, 'data_with_preds') or self.data_with_preds.empty:
            self.textBrowser_status.setText("\nError: No prediction data available. Please run prediction first.")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return
        
        try:
            # 获取当前筛选的数据
            filtered_data = self.get_current_filtered_data()
            
            if filtered_data.empty:
                self.textBrowser_status.setText("\nNo data to save after filtering.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 打开文件保存对话框
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Table Data",
                "prediction_results.csv",
                "CSV Files (*.csv);;Excel Files (*.xlsx);;TSV Files (*.tsv);;All Files (*)"
            )
            
            if file_path:
                # 根据文件扩展名选择保存格式
                if file_path.lower().endswith('.xlsx'):
                    # 保存为Excel格式
                    filtered_data.to_excel(file_path, index=False, engine='openpyxl')
                    self.textBrowser_status.setText(f"\nTable data saved successfully to Excel file: {file_path}")
                elif file_path.lower().endswith('.tsv'):
                    # 保存为TSV格式
                    filtered_data.to_csv(file_path, sep='\t', index=False)
                    self.textBrowser_status.setText(f"\nTable data saved successfully to TSV file: {file_path}")
                else:
                    # 默认保存为CSV格式
                    filtered_data.to_csv(file_path, index=False)
                    self.textBrowser_status.setText(f"\nTable data saved successfully to CSV file: {file_path}")
                
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                
        except Exception as e:
            self.textBrowser_status.setText(f"\nError saving table data: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def on_tab_changed(self, index):
        """Handle tab change events"""
        if index == 1:  # Plot tab (index 1)
            # 当切换到Plot页面时，自动绘制网络图
            if hasattr(self, 'data_with_preds') and self.data_with_preds is not None and not self.data_with_preds.empty:
                if hasattr(self, 'lineEdit_threshold') and self.lineEdit_threshold is not None:
                    self.textBrowser_status.setText("\nAuto-updating network plot...")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    self.update_network_plot()
                else:
                    self.textBrowser_status.setText("\nPlot controls not initialized. Please load data first.")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def _ensure_position_column(self, df: pd.DataFrame) -> pd.DataFrame:
        d = df.copy()
        if "Position" in d.columns:
            return d
        if "Protein|position" not in d.columns:
            return d
        sp = d["Protein|position"].str.split("|", expand=True)
        if sp.shape[1] >= 2:
            d["Position"] = sp[1]
        return d

    def _catalytic_residue_positions_from_df(self, df: pd.DataFrame) -> List[int]:
        """PDB 残基编号列表：Pre_label==1 或 Pre_Score≥CATALYTIC_THRESHOLD（无 Pre_label 时）。"""
        if df is None or df.empty:
            return []
        d = self._ensure_position_column(df)
        if "Position" not in d.columns:
            return []
        if "Pre_label" in d.columns:
            mask = pd.to_numeric(d["Pre_label"], errors="coerce").fillna(0).astype(int) == 1
        elif "Pre_Score" in d.columns:
            mask = pd.to_numeric(d["Pre_Score"], errors="coerce") >= CATALYTIC_THRESHOLD
        else:
            return []
        out: List[int] = []
        for p in d.loc[mask, "Position"]:
            try:
                out.append(int(p))
            except (ValueError, TypeError):
                continue
        return sorted(set(out))

    def _chain_id_for_3dmol(self, df: pd.DataFrame) -> str:
        d = self._ensure_position_column(df)
        if "Protein" in d.columns and len(d) > 0:
            pid = str(d["Protein"].iloc[0]).strip()
            if "-" in pid:
                ch = pid.split("-", 1)[1].strip().replace("_", "A")
                if ch:
                    return ch[0]
        if hasattr(self, "LineEdit_chain") and self.LineEdit_chain.text().strip():
            return self.LineEdit_chain.text().strip()[0]
        return "A"

    def _sorted_pdb_positions(self, plot_data: pd.DataFrame) -> List[int]:
        out: List[int] = []
        for p in plot_data["Position"].unique():
            try:
                out.append(int(float(p)))
            except (ValueError, TypeError):
                continue
        return sorted(set(out))

    def visualize_with_3dmol(self):
        """根据预测结果：序列中标红所有催化位点；3D 仅展示所选催化位点邻域。"""
        try:
            # 检查是否有数据
            if not hasattr(self, 'data_with_preds') or self.data_with_preds is None or self.data_with_preds.empty:
                self.textBrowser_status.setText("\nError: No prediction data available. Please run prediction or load result file first.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 检查PDB文件是否存在
            if not hasattr(self, 'pdb_path') or not self.pdb_path or not os.path.exists(self.pdb_path):
                # 如果没有PDB文件，让用户选择
                from PyQt5.QtWidgets import QFileDialog
                pdb_file, _ = QFileDialog.getOpenFileName(
                    self, 
                    "Select PDB File for 3D Visualization", 
                    "", 
                    "PDB files (*.pdb);;All files (*)"
                )
                if not pdb_file:
                    self.textBrowser_status.setText("\nError: PDB file is required for 3D visualization. Please select a PDB file.")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    return
                self.pdb_path = pdb_file
            
            # 获取当前筛选的数据
            plot_data = self.get_current_filtered_data()
            if plot_data.empty:
                self.textBrowser_status.setText("\nError: No data to visualize. Please adjust filter settings.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            plot_data = self._ensure_position_column(plot_data)
            if "Position" not in plot_data.columns:
                self.textBrowser_status.setText("\nError: Position column not found in data.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return

            catalytic_positions = self._catalytic_residue_positions_from_df(plot_data)
            all_positions = self._sorted_pdb_positions(plot_data)

            from PyQt5.QtWidgets import QInputDialog

            if catalytic_positions:
                items = [str(p) for p in catalytic_positions]
                msg = (
                    "Choose a catalytic site (PDB residue number) to view as the neighborhood center.\n"
                    "The sequence panel highlights all predicted catalytic sites in red."
                )
            else:
                items = [str(p) for p in all_positions]
                msg = (
                    "No catalytic sites in the current filter (Pre_label=1 or Pre_Score≥threshold).\n"
                    "Pick any residue to view its neighborhood, or adjust filters / predictions."
                )
            if not items:
                self.textBrowser_status.setText("\nError: No valid positions found in data.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return

            position, ok = QInputDialog.getItem(
                self,
                "3D View — Select center residue",
                msg,
                items,
                0,
                False,
            )
            
            if not ok or not position:
                return
            
            chain_id = self._chain_id_for_3dmol(plot_data)
            
            self.create_3dmol_visualization_dialog(
                self.pdb_path,
                chain_id,
                position,
                catalytic_positions=catalytic_positions,
            )
            
        except Exception as e:
            self.textBrowser_status.setText(f"\nError in 3Dmol visualization: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def create_3dmol_visualization_dialog(self, pdb_path, chain_id, position, catalytic_positions=None):
        """Create 3Dmol.js visualization and open in browser"""
        try:
            # 创建简单的参数设置对话框
            dialog = QDialog(self)
            dialog.setWindowTitle(f"3Dmol.js Visualization - Position {position}")
            dialog.setModal(True)
            dialog.resize(400, 150)
            
            layout = QVBoxLayout()
            
            # 添加控制面板
            control_layout = QHBoxLayout()
            
            # 距离阈值控制
            threshold_label = QLabel("Distance Threshold (Å):")
            threshold_spinbox = QSpinBox()
            threshold_spinbox.setRange(1, 50)
            threshold_spinbox.setValue(10)
            threshold_spinbox.setSuffix(" Å")
            
            control_layout.addWidget(threshold_label)
            control_layout.addWidget(threshold_spinbox)
            control_layout.addStretch()
            
            layout.addLayout(control_layout)
            
            # 添加按钮
            button_layout = QHBoxLayout()
            
            # 在浏览器中打开按钮
            open_browser_button = QPushButton("Open in Browser")
            open_browser_button.setStyleSheet("""
                QPushButton {
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
                QPushButton:pressed {
                    background-color: #004085;
                }
            """)
            
            # 保存按钮
            save_button = QPushButton("Save HTML")
            save_button.setStyleSheet("""
                QPushButton {
                    background-color: #28a745;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #218838;
                }
                QPushButton:pressed {
                    background-color: #1e7e34;
                }
            """)
            
            # 取消按钮
            cancel_button = QPushButton("Cancel")
            cancel_button.setStyleSheet("""
                QPushButton {
                    background-color: #6c757d;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #5a6268;
                }
                QPushButton:pressed {
                    background-color: #545b62;
                }
            """)
            
            button_layout.addWidget(open_browser_button)
            button_layout.addWidget(save_button)
            button_layout.addWidget(cancel_button)
            
            layout.addLayout(button_layout)
            
            # 连接信号
            def open_in_browser():
                try:
                    import os
                    import webbrowser
                    
                    # 添加调试信息
                    self.textBrowser_status.setText(f"\nDebug: open_in_browser function called")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    
                    # 使用self.pdb_path而不是参数pdb_path
                    current_pdb_path = self.pdb_path
                    
                    # 添加调试信息
                    self.textBrowser_status.setText(f"\nDebug: Using PDB file: {current_pdb_path}")
                    self.textBrowser_status.setText(f"\nDebug: PDB file exists: {os.path.exists(current_pdb_path) if current_pdb_path else False}")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    
                    # 检查PDB文件是否存在
                    if not os.path.exists(current_pdb_path):
                        self.textBrowser_status.setText(f"\nError: PDB file not found: {current_pdb_path}")
                        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        return
                    
                    # 生成HTML内容
                    html_content = self.generate_3dmol_html(
                        current_pdb_path,
                        chain_id,
                        position,
                        threshold_spinbox.value(),
                        catalytic_positions=catalytic_positions or [],
                    )
                    
                    # 保存HTML文件并在浏览器中打开
                    
                    # 获取GUI文件夹路径
                    gui_dir = os.path.dirname(os.path.abspath(__file__))
                    res_dir = os.path.join(gui_dir, "res")
                    
                    # 确保res文件夹存在
                    if not os.path.exists(res_dir):
                        os.makedirs(res_dir)
                    
                    # 使用固定HTML文件名
                    html_filename = "3dmol_visualization.html"
                    html_file = os.path.join(res_dir, html_filename)
                    
                    # 写入HTML文件（覆盖之前的文件）
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    # 打开浏览器
                    # webbrowser.open(f'file://{temp_file}')
                    webbrowser.open(f'file://{html_file}')
                    # 更新状态
                    self.textBrowser_status.setText(f"\nOpening 3Dmol visualization in browser...")
                    # self.textBrowser_status.setText(f"\nTemporary file: {temp_file}")
                    self.textBrowser_status.setText(f"\nFile: {html_file}")
                    self.textBrowser_status.setText(f"\nTarget: Chain {chain_id}, Position {position}")
                    self.textBrowser_status.setText(f"\nDistance threshold: {threshold_spinbox.value()} Å")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    
                    # 关闭对话框
                    dialog.accept()
                    
                except Exception as e:
                    self.textBrowser_status.setText(f"\nError opening browser: {str(e)}")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
            def save_html():
                try:
                    import os
                    
                    # 使用self.pdb_path而不是参数pdb_path
                    current_pdb_path = self.pdb_path
                    
                    # 检查PDB文件是否存在
                    if not os.path.exists(current_pdb_path):
                        self.textBrowser_status.setText(f"\nError: PDB file not found: {current_pdb_path}")
                        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        return
                    
                    # 生成HTML内容
                    html_content = self.generate_3dmol_html(
                        current_pdb_path,
                        chain_id,
                        position,
                        threshold_spinbox.value(),
                        catalytic_positions=catalytic_positions or [],
                    )
                    
                    # 打开文件保存对话框
                    file_path, _ = QFileDialog.getSaveFileName(
                        dialog, 
                        "Save HTML File", 
                        f"3dmol_visualization_position_{position}_threshold_{threshold_spinbox.value()}.html",
                        "HTML files (*.html)"
                    )
                    if file_path:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(html_content)
                        self.textBrowser_status.setText(f"\n3Dmol.js visualization saved to: {file_path}")
                        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        
                        # 询问是否在浏览器中打开
                        from PyQt5.QtWidgets import QMessageBox
                        reply = QMessageBox.question(
                            dialog, 
                            'Open in Browser', 
                            f'HTML file saved successfully!\n\nDo you want to open it in your browser now?',
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.Yes
                        )
                        
                        if reply == QMessageBox.Yes:
                            import webbrowser
                            webbrowser.open(f'file://{file_path}')
                            self.textBrowser_status.setText(f"\nOpening saved file in browser...")
                            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        
                        dialog.accept()
                        
                except Exception as e:
                    self.textBrowser_status.setText(f"\nError saving HTML: {str(e)}")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
            def cancel_dialog():
                dialog.reject()
            
            open_browser_button.clicked.connect(open_in_browser)
            save_button.clicked.connect(save_html)
            cancel_button.clicked.connect(cancel_dialog)
            
            dialog.setLayout(layout)
            dialog.exec_()
            
        except Exception as e:
            self.textBrowser_status.setText(f"\nError creating 3Dmol dialog: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def generate_3dmol_html(self, pdb_path, chain_id, position, threshold, catalytic_positions=None):
        """Generate HTML with 3Dmol.js: red catalytic sites in sequence; 3D shows neighborhood of selected site."""
        if catalytic_positions is None:
            catalytic_positions = []
        try:
            catalytic_js_array = json.dumps([int(x) for x in catalytic_positions])
        except (ValueError, TypeError):
            catalytic_js_array = "[]"
        # 读取PDB文件内容
        try:
            with open(pdb_path, 'r') as f:
                pdb_content = f.read()
            print(f"Successfully loaded PDB file: {pdb_path} ({len(pdb_content)} characters)")
        except Exception as e:
            print(f"Failed to load PDB file {pdb_path}: {e}")
            # 使用默认示例PDB内容作为后备
            pdb_content = "ATOM      1  N   ALA A   1      20.154  16.967  23.862  1.00 11.18           N  \nATOM      2  CA  ALA A   1      19.030  16.053  23.456  1.00 10.53           C  \n"
        
        # 获取当前脚本目录，用于构建本地文件路径
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_3dmol_path = os.path.join(script_dir, 'static', 'js', '3Dmol-min.js')
        
        # 尝试读取本地3Dmol.js文件内容
        local_3dmol_content = ""
        try:
            with open(local_3dmol_path, 'r', encoding='utf-8') as f:
                local_3dmol_content = f.read()
            print(f"Successfully loaded local 3Dmol.js ({len(local_3dmol_content)} characters)")
        except Exception as e:
            print(f"Failed to load local 3Dmol.js: {e}")
            local_3dmol_content = ""
        
        # 如果有本地3Dmol.js文件，直接嵌入；否则使用CDN
        if local_3dmol_content:
            script_tag = f'<script>{local_3dmol_content}</script>'
            load_script = '''
// 直接使用内嵌的3Dmol.js
window.onload = function() {
    document.getElementById('loading').innerHTML = '3Dmol.js loaded successfully.';
    
    // 等待3Dmol.js完全初始化
    let waitCount = 0;
    const maxWaitCount = 100; // 最多等待5秒 (100 * 50ms)
    
    function waitFor3Dmol() {
        if (typeof $3Dmol !== 'undefined' && $3Dmol.createViewer) {
            console.log('3Dmol.js is ready');
            init();
        } else if (waitCount < maxWaitCount) {
            waitCount++;
            console.log('Waiting for 3Dmol.js to initialize... (' + waitCount + '/' + maxWaitCount + ')');
            setTimeout(waitFor3Dmol, 50);
        } else {
            console.error('3Dmol.js failed to initialize after maximum wait time');
            document.getElementById('loading').innerHTML = 'Error: 3Dmol.js failed to initialize properly.';
        }
    }
    
    // 延迟启动，确保3Dmol.js完全加载
    setTimeout(waitFor3Dmol, 200);
};
            '''
        else:
            script_tag = '<script src="https://3Dmol.org/build/3Dmol-min.js" onerror="loadBackup3Dmol()"></script>'
            load_script = '''
        // 检查网络连接
        function checkNetworkConnection() {
            return new Promise((resolve) => {
                const img = new Image();
                img.onload = () => resolve(true);
                img.onerror = () => resolve(false);
                img.src = 'https://3Dmol.org/favicon.ico?t=' + Date.now();
                setTimeout(() => resolve(false), 3000);
            });
        }
        
        // 尝试多个CDN源加载3Dmol.js
        async function load3Dmol() {
            // 首先检查网络连接
            const hasNetwork = await checkNetworkConnection();
            if (!hasNetwork) {
                document.getElementById('loading').innerHTML = 'No internet connection detected. Using fallback mode.';
                tryLocalFallback();
                return;
            }
            
            const cdnSources = [
                'https://3Dmol.org/build/3Dmol-min.js',
                'https://cdn.jsdelivr.net/npm/3dmol@2.1.0/build/3Dmol-min.js',
                'https://unpkg.com/3dmol@2.1.0/build/3Dmol-min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.1.0/3Dmol-min.js'
            ];
            
            let currentIndex = 0;
            
            function tryNextCDN() {
                if (currentIndex >= cdnSources.length) {
                    // 尝试使用本地备用方案
                    tryLocalFallback();
                    return;
                }
                
                const script = document.createElement('script');
                script.src = cdnSources[currentIndex];
                script.onload = function() {
                    console.log('3Dmol.js loaded successfully from:', cdnSources[currentIndex]);
                    
                    // 等待3Dmol.js完全初始化
                    let waitCount = 0;
                    const maxWaitCount = 100; // 最多等待5秒 (100 * 50ms)
                    
                    function waitFor3Dmol() {
                        if (typeof $3Dmol !== 'undefined' && $3Dmol.createViewer) {
                            console.log('3Dmol.js is ready');
                            document.getElementById('loading').innerHTML = '3Dmol.js loaded successfully.';
                            init();
                        } else if (waitCount < maxWaitCount) {
                            waitCount++;
                            console.log('Waiting for 3Dmol.js to initialize... (' + waitCount + '/' + maxWaitCount + ')');
                            setTimeout(waitFor3Dmol, 50);
                        } else {
                            console.error('3Dmol.js failed to initialize after maximum wait time');
                            document.getElementById('loading').innerHTML = 'Error: 3Dmol.js failed to initialize properly.';
                        }
                    }
                    
                    // 延迟启动，确保3Dmol.js完全加载
                    setTimeout(waitFor3Dmol, 200);
                };
                script.onerror = function() {
                    console.log('Failed to load from:', cdnSources[currentIndex]);
                    currentIndex++;
                    tryNextCDN();
                };
                document.head.appendChild(script);
            }
            
            tryNextCDN();
        }
        
        function tryLocalFallback() {
            console.log('Trying local 3Dmol.js...');
            
            // 尝试加载本地3Dmol.js文件
            const script = document.createElement('script');
            script.src = './static/js/3Dmol-min.js';
            script.onload = function() {
                console.log('Local 3Dmol.js loaded successfully');
                document.getElementById('loading').innerHTML = 'Local 3Dmol.js loaded successfully.';
                
                // 等待3Dmol.js完全初始化
                let waitCount = 0;
                const maxWaitCount = 100; // 最多等待5秒 (100 * 50ms)
                
                function waitFor3Dmol() {
                    if (typeof $3Dmol !== 'undefined' && $3Dmol.createViewer) {
                        console.log('Local 3Dmol.js is ready');
                        init();
                    } else if (waitCount < maxWaitCount) {
                        waitCount++;
                        console.log('Waiting for local 3Dmol.js to initialize... (' + waitCount + '/' + maxWaitCount + ')');
                        setTimeout(waitFor3Dmol, 50);
                    } else {
                        console.error('Local 3Dmol.js failed to initialize after maximum wait time');
                        document.getElementById('loading').innerHTML = 'Error: Local 3Dmol.js failed to initialize properly.';
                    }
                }
                
                // 延迟启动，确保3Dmol.js完全加载
                setTimeout(waitFor3Dmol, 200);
            };
            script.onerror = function() {
                console.log('Local 3Dmol.js not found, using simplified fallback');
                trySimplifiedFallback();
            };
            document.head.appendChild(script);
        }
        
        function trySimplifiedFallback() {
            // 创建一个简化的3Dmol.js替代方案
            console.log('Using simplified fallback...');
            
            // 创建一个简化的3Dmol对象
            window.$3Dmol = {
                createViewer: function(element, options) {
                    return {
                        addModel: function(data, format) {
                            console.log('Fallback: addModel called');
                        },
                        setStyle: function(selection, style) {
                            console.log('Fallback: setStyle called');
                        },
                        render: function() {
                            console.log('Fallback: render called');
                        },
                        zoomTo: function(selection) {
                            console.log('Fallback: zoomTo called');
                        },
                        getModel: function() {
                            return {
                                selectedAtoms: function(criteria) {
                                    return [];
                                }
                            };
                        },
                        addSurface: function(type, options, selection) {
                            console.log('Fallback: addSurface called');
                        },
                        removeAllSurfaces: function() {
                            console.log('Fallback: removeAllSurfaces called');
                        },
                        addLabel: function(text, options) {
                            console.log('Fallback: addLabel called');
                        },
                        removeAllLabels: function() {
                            console.log('Fallback: removeAllLabels called');
                        }
                    };
                },
                SurfaceType: {
                    VDW: 'VDW'
                },
                rasmolElementColors: {}
            };
            
            // 显示备用模式信息
            document.getElementById('loading').innerHTML = 'Using simplified fallback mode - 3Dmol.js not available. Some features may be limited.';
            
            // 延迟初始化
            setTimeout(function() {
                init();
            }, 500);
        }
        
        // 页面加载后开始加载3Dmol.js
        window.onload = function() {
            load3Dmol();
        };
            '''
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>3Dmol Local Residue Visualization - Chain {chain_id}, Position {position}</title>
    {script_tag}
    <script>
        {load_script}
    </script>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            margin: 0 0 10px 0;
            font-size: 24px;
        }}
        .header p {{
            margin: 5px 0;
            opacity: 0.9;
        }}
        #viewer {{
            width: 100%;
            height: 700px;
            border: 2px solid #dee2e6;
            border-radius: 10px;
            position: relative;
            overflow: hidden;
            background: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .controls {{
            margin: 15px 0;
            padding: 15px;
            background: white;
            border-radius: 10px;
            border: 1px solid #dee2e6;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
        }}
        .controls button {{
            margin: 2px;
            padding: 10px 16px;
            background: linear-gradient(135deg, #007bff, #0056b3);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .controls button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        .controls button:active {{
            transform: translateY(0);
        }}
        .info {{
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #28a745;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stats {{
            background: linear-gradient(135deg, #e3f2fd, #bbdefb);
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #2196F3;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .loading {{
            text-align: center;
            padding: 40px;
            color: #666;
            font-size: 16px;
        }}
        .instructions {{
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #ffc107;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .instructions ul {{
            margin: 10px 0;
            padding-left: 20px;
        }}
        .instructions li {{
            margin: 5px 0;
        }}
        .sequence-panel {{
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border: 1px solid #dee2e6;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .sequence-panel h3 {{
            margin: 0 0 15px 0;
            color: #2C3E50;
            font-size: 18px;
            font-weight: bold;
        }}
        .sequence-container {{
            width: 100%;
        }}
        .sequence-info {{
            display: flex;
            gap: 20px;
            margin-bottom: 15px;
            font-size: 14px;
            color: #666;
        }}
        .sequence-info span {{
            display: flex;
            align-items: center;
        }}
        .sequence-display {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 15px;
            overflow-x: auto;
        }}
        .sequence-text {{
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.8;
            white-space: pre-wrap;
            user-select: text;
            letter-spacing: 1px;
            word-break: break-all;
        }}
        .residue {{
            display: inline-block;
            padding: 3px 6px;
            margin: 1px;
            border-radius: 4px;
            font-weight: bold;
            min-width: 24px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 14px;
            line-height: 1.2;
        }}
        .residue:hover {{
            transform: scale(1.1);
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }}
        .residue.target {{
            background-color: #dc3545;
            color: white;
            border: 2px solid #c82333;
        }}
        .residue.catalytic {{
            background-color: #c82333;
            color: #fff;
            border: 2px solid #7f1d1d;
            font-weight: bold;
        }}
        .residue.catalytic.focus {{
            box-shadow: 0 0 0 3px #ffc107;
            outline: 2px solid #ffc107;
        }}
        .residue.local {{
            background-color: #ffc107;
            color: #212529;
            border: 1px solid #e0a800;
        }}
        .residue.other {{
            background-color: #e9ecef;
            color: #6c757d;
            border: 1px solid #ced4da;
        }}
        .sequence-legend {{
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
        }}
        .legend-color {{
            width: 16px;
            height: 16px;
            border-radius: 3px;
            border: 1px solid #ccc;
        }}
        .legend-color.target {{
            background-color: #dc3545;
        }}
        .legend-color.catalytic {{
            background-color: #c82333;
        }}
        .legend-color.local {{
            background-color: #ffc107;
        }}
        .legend-color.other {{
            background-color: #e9ecef;
        }}
        .line-number {{
            color: #6c757d;
            font-size: 12px;
            margin-right: 10px;
            font-weight: normal;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>3D Protein Structure Visualization</h1>
        <p><strong>Center residue (neighborhood sphere):</strong> chain {chain_id}, PDB number {position}</p>
        <p><strong>Neighborhood radius:</strong> {threshold} Å (Cα–Cα distance)</p>
        <p><strong>Sequence:</strong> red = all predicted catalytic sites; 3D shows only the neighborhood of this center.</p>
        <p><strong>PDB File:</strong> {os.path.basename(pdb_path)}</p>
    </div>
    
    <div class="controls">
        <button onclick="resetView()">Reset View</button>
        <button onclick="toggleSurface()">Toggle Surface</button>
        <button onclick="toggleLabels()">Toggle Labels</button>
        <button onclick="centerOnTarget()">Center on Target</button>
        <button onclick="showAllChains()">Show All Chains</button>
        <button onclick="showLocalOnly()">Show Local Only</button>
        <button onclick="toggleDisplayMode()">Toggle Display Mode</button>
    </div>
    
    <div id="viewer">
        <div class="loading" id="loading">Loading 3Dmol.js...</div>
    </div>
    
    <div class="stats" id="stats">
        <strong>Statistics:</strong><br>
        <span id="residueCount">Calculating...</span>
    </div>
    
    <div class="sequence-panel">
        <h3>Protein Sequence</h3>
        <div class="sequence-container">
            <div class="sequence-info">
                <span>Chain: <strong id="chainInfo">{chain_id}</strong></span>
                <span>Total Residues: <strong id="totalResidues">Calculating...</strong></span>
                <span>Local Residues: <strong id="localResidues">Calculating...</strong></span>
            </div>
            <div class="sequence-display" id="sequenceDisplay">
                <div class="sequence-text" id="sequenceText">Loading sequence...</div>
            </div>
            <div class="sequence-legend">
                <div class="legend-item">
                    <span class="legend-color catalytic"></span>
                    <span>Predicted catalytic sites (red)</span>
                </div>
                <div class="legend-item">
                    <span class="legend-color local"></span>
                    <span>Other residues in neighborhood</span>
                </div>
                <div class="legend-item">
                    <span class="legend-color other"></span>
                    <span>Rest of chain</span>
                </div>
            </div>
        </div>
    </div>
    
    <div class="instructions">
        <strong>Instructions:</strong>
        <ul>
            <li><strong>Mouse Controls:</strong> Left click + drag to rotate, right click + drag to pan, scroll to zoom</li>
            <li><strong>3D view:</strong> By default only the local structure within {threshold} Å of residue {position}</li>
            <li><strong>Sequence:</strong> All predicted catalytic sites in red; gold outline = selected center residue</li>
            <li><strong>CPK Colorscheme:</strong> Carbon (Cyan), Nitrogen (Blue), Oxygen (Red), Sulfur (Yellow), Hydrogen (White)</li>
            <li><strong>Display Modes:</strong> Switch between stick, sphere, and cartoon representations</li>
        </ul>
    </div>

    <script>
        let viewer;
        let surfaceVisible = false;
        let labelsVisible = true;
        let showAllChainsMode = false;
        let displayMode = 'stick'; // 'stick', 'sphere', 'cartoon'
        let localResidues = new Set();
        let targetResidue = {int(position)};
        let catalyticSites = new Set({catalytic_js_array});
        let chainId = '{chain_id}';
        let threshold = {float(threshold)};
        
        function init() {{
            try {{
                // 检查3Dmol.js是否加载成功
                if (typeof $3Dmol === 'undefined') {{
                    document.getElementById('loading').innerHTML = 'Error: 3Dmol.js failed to load. Please check your internet connection.';
                    return;
                }}
                
                // 隐藏加载提示
                const loadingDiv = document.getElementById('loading');
                if (loadingDiv) {{
                    loadingDiv.style.display = 'none';
                }}
                
                // 创建viewer，确保不会影响其他元素
                const viewerElement = document.getElementById('viewer');
                viewer = $3Dmol.createViewer(viewerElement, {{
                    defaultcolors: $3Dmol.rasmolElementColors
                }});
            
            // Load PDB data
            const pdbData = `{pdb_content}`;
            viewer.addModel(pdbData, "pdb");
            
                // 计算局部残基
                calculateLocalResidues();
                
                // 设置初始显示模式
                showLocalOnly();
                
                // 添加标签
                addLabels();
                
                // 更新统计信息
                updateStats();
                
                // 生成蛋白质序列
                generateProteinSequence();
                
                // 居中显示
                centerOnTarget();
                
                console.log('3Dmol.js visualization initialized successfully');
                
                // 确保按钮区域可见
                const controlsDiv = document.querySelector('.controls');
                if (controlsDiv) {{
                    controlsDiv.style.display = 'block';
                    controlsDiv.style.visibility = 'visible';
                    controlsDiv.style.position = 'relative';
                    controlsDiv.style.zIndex = '1000';
                    console.log('Controls div is visible');
                }} else {{
                    console.error('Controls div not found!');
                }}
                
                // 设置定时器，定期检查按钮可见性
                setInterval(function() {{
                    ensureControlsVisible();
                }}, 1000);
                
            }} catch (error) {{
                console.error('Error initializing 3Dmol.js:', error);
                const loadingDiv = document.getElementById('loading');
                if (loadingDiv) {{
                    loadingDiv.innerHTML = 'Error initializing visualization: ' + error.message;
                }}
            }}
        }}
        
        function calculateLocalResidues() {{
            // 获取目标残基的α碳原子坐标
            const targetAtoms = viewer.getModel().selectedAtoms({{chain: chainId, resi: targetResidue, atom: 'CA'}});
            if (targetAtoms.length === 0) {{
                console.log('Target residue α-carbon not found');
                return;
            }}
            
            const targetPos = targetAtoms[0];
            localResidues.clear();
            localResidues.add(targetResidue); // 添加目标残基
            
            // 遍历所有残基，计算与目标残基的距离
            const allAtoms = viewer.getModel().selectedAtoms({{chain: chainId, atom: 'CA'}});
            
            allAtoms.forEach(atom => {{
                if (atom.resi !== targetResidue) {{
                    const distance = Math.sqrt(
                        Math.pow(atom.x - targetPos.x, 2) +
                        Math.pow(atom.y - targetPos.y, 2) +
                        Math.pow(atom.z - targetPos.z, 2)
                    );
                    
                    if (distance <= threshold) {{
                        localResidues.add(atom.resi);
                    }}
                }}
            }});
            
            console.log(`Found ${{localResidues.size}} local residues:`, Array.from(localResidues).sort((a, b) => a - b));
        }}
        
        function showLocalOnly() {{
            showAllChainsMode = false;
            
            // 隐藏所有残基
            viewer.setStyle({{}}, {{}});
            
            // 只显示局部残基
            const localResidueList = Array.from(localResidues);
            
            // 根据显示模式设置样式
            let baseStyle = {{}};
            let targetStyle = {{}};
            let nearbyStyle = {{}};
            
            if (displayMode === 'stick') {{
                // Stick模式 - 使用CPK颜色方案，碳原子为青色
                baseStyle = {{
                    stick: {{
                        radius: 0.3,
                        colorscheme: 'CPK',
                        opacity: 0.8
                    }}
                }};
                // 目标残基使用更粗的stick，保持CPK颜色
                targetStyle = {{
                    stick: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等粗细的stick，保持CPK颜色
                nearbyStyle = {{
                    stick: {{
                        radius: 0.4,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'sphere') {{
                // Sphere模式 - 使用CPK颜色方案，碳原子为青色
                baseStyle = {{
                    sphere: {{
                        radius: 0.4,
                        colorscheme: 'CPK',
                        opacity: 0.8
                    }}
                }};
                // 目标残基使用更大的sphere，保持CPK颜色
                targetStyle = {{
                    sphere: {{
                        radius: 0.6,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等大小的sphere，保持CPK颜色
                nearbyStyle = {{
                    sphere: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'cartoon') {{
                // Cartoon模式 - 使用CPK颜色方案
                baseStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.8
                    }}
                }};
                targetStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                nearbyStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }}
            
            // 应用基础样式
            viewer.setStyle({{chain: chainId, resi: localResidueList}}, baseStyle);
            
            // 高亮目标残基
            viewer.setStyle({{chain: chainId, resi: targetResidue}}, targetStyle);
            
            // 高亮范围内的其他残基
            const nearbyResidues = localResidueList.filter(resi => resi !== targetResidue);
            if (nearbyResidues.length > 0) {{
                viewer.setStyle({{chain: chainId, resi: nearbyResidues}}, nearbyStyle);
            }}
            
            const catNear = nearbyResidues.filter(r => catalyticSites.has(r));
            if (displayMode === 'stick' && catNear.length > 0) {{
                viewer.setStyle({{chain: chainId, resi: catNear}}, {{
                    stick: {{ color: 'red', radius: 0.44, opacity: 1.0 }}
                }});
            }} else if (displayMode === 'sphere' && catNear.length > 0) {{
                viewer.setStyle({{chain: chainId, resi: catNear}}, {{
                    sphere: {{ color: 'red', radius: 0.52, opacity: 1.0 }}
                }});
            }} else if (displayMode === 'cartoon' && catNear.length > 0) {{
                viewer.setStyle({{chain: chainId, resi: catNear}}, {{
                    cartoon: {{ color: 'red', opacity: 1.0 }}
                }});
            }}
            if (displayMode === 'stick' && catalyticSites.has(targetResidue)) {{
                viewer.setStyle({{chain: chainId, resi: targetResidue}}, {{
                    stick: {{ color: 'darkred', radius: 0.58, opacity: 1.0 }}
                }});
            }} else if (displayMode === 'sphere' && catalyticSites.has(targetResidue)) {{
                viewer.setStyle({{chain: chainId, resi: targetResidue}}, {{
                    sphere: {{ color: 'darkred', radius: 0.62, opacity: 1.0 }}
                }});
            }} else if (displayMode === 'cartoon' && catalyticSites.has(targetResidue)) {{
                viewer.setStyle({{chain: chainId, resi: targetResidue}}, {{
                    cartoon: {{ color: 'darkred', opacity: 1.0 }}
                }});
            }}
            
            viewer.render();
            // 确保按钮在渲染后仍然可见
            ensureControlsVisible();
            
            // 更新序列显示
            generateProteinSequence();
        }}
        
        function showAllChains() {{
            showAllChainsMode = true;
            
            // 显示所有链 - 使用cartoon形式作为背景
            viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum', opacity: 0.3}}}});
            
            // 根据显示模式设置目标链样式
            let chainStyle = {{}};
            let targetStyle = {{}};
            let nearbyStyle = {{}};
            
            if (displayMode === 'stick') {{
                // Stick模式 - 使用CPK颜色方案，碳原子为青色
                chainStyle = {{
                    stick: {{
                        radius: 0.2,
                        colorscheme: 'CPK',
                        opacity: 0.6
                    }}
                }};
                // 目标残基使用更粗的stick，保持CPK颜色
                targetStyle = {{
                    stick: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等粗细的stick，保持CPK颜色
                nearbyStyle = {{
                    stick: {{
                        radius: 0.4,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'sphere') {{
                // Sphere模式 - 使用CPK颜色方案，碳原子为青色
                chainStyle = {{
                    sphere: {{
                        radius: 0.3,
                        colorscheme: 'CPK',
                        opacity: 0.6
                    }}
                }};
                // 目标残基使用更大的sphere，保持CPK颜色
                targetStyle = {{
                    sphere: {{
                        radius: 0.6,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等大小的sphere，保持CPK颜色
                nearbyStyle = {{
                    sphere: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'cartoon') {{
                // Cartoon模式 - 使用CPK颜色方案
                chainStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.6
                    }}
                }};
                targetStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                nearbyStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }}
            
            // 高亮目标链
            viewer.setStyle({{chain: chainId}}, chainStyle);
            
            // 高亮目标残基
            viewer.setStyle({{chain: chainId, resi: targetResidue}}, targetStyle);
            
            // 高亮范围内的残基
            const nearbyResidues = Array.from(localResidues).filter(resi => resi !== targetResidue);
            if (nearbyResidues.length > 0) {{
                viewer.setStyle({{chain: chainId, resi: nearbyResidues}}, nearbyStyle);
            }}
            
            // α碳原子使用标准CPK颜色方案，不再额外设置颜色
            
            viewer.render();
            // 确保按钮在渲染后仍然可见
            ensureControlsVisible();
            
            // 更新序列显示
            generateProteinSequence();
        }}
        
        function addLabels() {{
            try {{
                // 先移除所有标签
                viewer.removeAllLabels();
                
            if (labelsVisible) {{
                    console.log('Adding labels...');
                    console.log('localResidues size:', localResidues.size);
                    console.log('targetResidue:', targetResidue);
                    console.log('chainId:', chainId);
                    
                    // 确保localResidues不为空
                    if (localResidues.size === 0) {{
                        console.log('localResidues is empty, recalculating...');
                        calculateLocalResidues();
                    }}
                    
                    // 获取残基的氨基酸字母
                    function getResidueName(residueNumber) {{
                        try {{
                            const atoms = viewer.getModel().selectedAtoms({{chain: chainId, resi: residueNumber}});
                            if (atoms.length > 0) {{
                                return atoms[0].resn; // 获取残基名称
                            }}
                        }} catch (error) {{
                            console.error('Error getting residue name for', residueNumber, ':', error);
                        }}
                        return 'UNK'; // 如果无法获取，返回未知
                    }}
                    
                    // 方法1: 尝试使用addResLabels (3Dmol.js内置方法)
                    try {{
                        console.log('Trying addResLabels method...');
                        viewer.addResLabels({{chain: chainId, resi: Array.from(localResidues)}}, {{
                            backgroundColor: 'yellow',
                            backgroundOpacity: 0.7,
                            fontColor: 'black',
                            fontSize: 12
                        }});
                        console.log('addResLabels method successful');
                    }} catch (error) {{
                        console.log('addResLabels failed, trying individual labels:', error);
                        
                        // 方法2: 使用addLabel为每个残基添加标签
                        const targetResidueName = getResidueName(targetResidue);
                        console.log('Adding target residue label:', targetResidueName + targetResidue);
                        
                        viewer.addLabel(`${{targetResidueName}}${{targetResidue}}`, {{
                            position: {{chain: chainId, resi: targetResidue}}, 
                            backgroundColor: 'red', 
                            backgroundOpacity: 0.8, 
                            fontColor: 'white',
                            fontSize: 14
                        }});
                        
                        // 为范围内的其他残基添加标签
                        const nearbyResidues = Array.from(localResidues).filter(resi => resi !== targetResidue);
                        console.log('nearbyResidues:', nearbyResidues);
                        
                        nearbyResidues.forEach(resi => {{
                            const residueName = getResidueName(resi);
                            console.log('Adding nearby residue label:', residueName + resi);
                            
                            viewer.addLabel(`${{residueName}}${{resi}}`, {{
                                position: {{chain: chainId, resi: resi}}, 
                                backgroundColor: 'yellow', 
                                backgroundOpacity: 0.7, 
                                fontColor: 'black',
                                fontSize: 12
                            }});
                        }});
                    }}
                    
                    console.log('Labels added successfully');
                }} else {{
                    console.log('Labels hidden');
                }}
            }} catch (error) {{
                console.error('Error in addLabels:', error);
            }}
        }}
        
        function updateStats() {{
            const totalResidues = localResidues.size;
            const nearbyResidues = totalResidues - 1; // 减去目标残基
            
            document.getElementById('residueCount').innerHTML = `
                Total Local Residues: ${{totalResidues}}<br>
                Target Residue: ${{targetResidue}}<br>
                Nearby Residues: ${{nearbyResidues}}<br>
                Distance Threshold: ${{threshold}} Å
            `;
        }}
        
        function generateProteinSequence() {{
            try {{
                console.log('Generating protein sequence...');
                
                // 获取所有残基信息
                const allAtoms = viewer.getModel().selectedAtoms({{chain: chainId}});
                const residues = new Map();
                
                // 按残基编号分组
                allAtoms.forEach(atom => {{
                    if (!residues.has(atom.resi)) {{
                        residues.set(atom.resi, {{
                            resi: atom.resi,
                            resn: atom.resn,
                            chain: atom.chain
                        }});
                    }}
                }});
                
                // 转换为数组并排序
                const sortedResidues = Array.from(residues.values()).sort((a, b) => a.resi - b.resi);
                console.log('Found', sortedResidues.length, 'residues');
                
                // 更新统计信息
                document.getElementById('totalResidues').textContent = sortedResidues.length;
                document.getElementById('localResidues').textContent = localResidues.size;
                
                // 生成序列HTML - 使用单字母形式
                let sequenceHTML = '';
                const residuesPerLine = 60; // 每行显示60个残基
                
                sortedResidues.forEach((residue, index) => {{
                    let cssClass = 'other';
                    const isCat = catalyticSites.has(residue.resi);
                    const inLocal = localResidues.has(residue.resi);
                    if (isCat) {{
                        cssClass = 'catalytic';
                        if (residue.resi === targetResidue) {{
                            cssClass += ' focus';
                        }}
                    }} else if (inLocal) {{
                        cssClass = 'local';
                    }}
                    
                    // 将三字母氨基酸代码转换为单字母
                    const singleLetter = getSingleLetterCode(residue.resn);
                    sequenceHTML += `<span class="residue ${{cssClass}}" data-resi="${{residue.resi}}" title="Residue ${{residue.resn}}${{residue.resi}} (${{singleLetter}})">${{singleLetter}}</span>`;
                    
                    // 每60个残基换行，并添加行号
                    if ((index + 1) % residuesPerLine === 0) {{
                        const lineNumber = Math.floor((index + 1) / residuesPerLine);
                        sequenceHTML += `<br><span class="line-number">${{lineNumber * residuesPerLine + 1}}</span>`;
                    }}
                }});
                
                // 更新序列显示
                document.getElementById('sequenceText').innerHTML = sequenceHTML;
                
                // 添加点击事件
                document.querySelectorAll('.residue').forEach(element => {{
                    element.addEventListener('click', function() {{
                        const resi = parseInt(this.dataset.resi);
                        console.log('Clicked on residue:', resi);
                        // 可以在这里添加点击残基时的操作
                        centerOnResidue(resi);
                    }});
                }});
                
                console.log('Protein sequence generated successfully');
                
            }} catch (error) {{
                console.error('Error generating protein sequence:', error);
                document.getElementById('sequenceText').innerHTML = 'Error loading sequence';
            }}
        }}
        
        function getSingleLetterCode(threeLetterCode) {{
            const aminoAcidMap = {{
                'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
                'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
                'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
                'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V',
                'ASX': 'B', 'GLX': 'Z', 'XAA': 'X', 'UNK': 'X'
            }};
            return aminoAcidMap[threeLetterCode.toUpperCase()] || 'X';
        }}
        
        function centerOnResidue(resi) {{
            try {{
                viewer.zoomTo({{chain: chainId, resi: resi}});
            viewer.render();
                console.log('Centered on residue:', resi);
            }} catch (error) {{
                console.error('Error centering on residue:', error);
            }}
        }}
        
        function resetView() {{
            try {{
                if (showAllChainsMode) {{
                    showAllChains();
                }} else {{
                    showLocalOnly();
                }}
            viewer.zoomTo();
            }} catch (error) {{
                console.error('Error in resetView:', error);
            }}
        }}
        
        function toggleSurface() {{
            try {{
            if (surfaceVisible) {{
                viewer.removeAllSurfaces();
                surfaceVisible = false;
            }} else {{
                    // 为局部残基添加VDW表面
                    const localResidueList = Array.from(localResidues);
                    viewer.addSurface($3Dmol.SurfaceType.VDW, {{
                        opacity: 0.4, 
                        color: 'lightblue'
                    }}, {{chain: chainId, resi: localResidueList}});
                surfaceVisible = true;
            }}
            viewer.render();
            }} catch (error) {{
                console.error('Error in toggleSurface:', error);
            }}
        }}
        
        function toggleLabels() {{
            try {{
                console.log('toggleLabels called, current labelsVisible:', labelsVisible);
            labelsVisible = !labelsVisible;
                console.log('toggleLabels called, new labelsVisible:', labelsVisible);
                addLabels();
            viewer.render();
                console.log('toggleLabels completed');
            }} catch (error) {{
                console.error('Error in toggleLabels:', error);
            }}
        }}
        
        function centerOnTarget() {{
            try {{
                viewer.zoomTo({{chain: chainId, resi: targetResidue}});
            viewer.render();
            }} catch (error) {{
                console.error('Error in centerOnTarget:', error);
            }}
        }}
        
        function toggleDisplayMode() {{
            try {{
                // 循环切换显示模式: stick -> sphere -> cartoon -> stick
                if (displayMode === 'stick') {{
                    displayMode = 'sphere';
                }} else if (displayMode === 'sphere') {{
                    displayMode = 'cartoon';
                }} else {{
                    displayMode = 'stick';
                }}
                
                // 重新应用显示模式
                if (showAllChainsMode) {{
                    showAllChains();
                }} else {{
                    showLocalOnly();
                }}
                
                console.log('Display mode changed to:', displayMode);
            }} catch (error) {{
                console.error('Error in toggleDisplayMode:', error);
            }}
        }}
        
        function ensureControlsVisible() {{
            // 强制确保按钮区域可见
            const controlsDiv = document.querySelector('.controls');
            if (controlsDiv) {{
                controlsDiv.style.display = 'block';
                controlsDiv.style.visibility = 'visible';
                controlsDiv.style.position = 'relative';
                controlsDiv.style.zIndex = '1000';
            }}
        }}
        
        // 初始化函数现在由load3Dmol()调用
    </script>
</body>
</html>
"""
        return html_content
    
    def get_current_filtered_data(self):
        """Get currently filtered data based on user selections"""
        if not hasattr(self, 'data_with_preds') or self.data_with_preds is None or self.data_with_preds.empty:
            return pd.DataFrame()

        filtered_data = self.data_with_preds.copy()
        if hasattr(self, "comboBox_protein_pos") and self.comboBox_protein_pos is not None:
            try:
                selected_protein_pos = self.comboBox_protein_pos.currentText()
            except RuntimeError:
                selected_protein_pos = "All"
            if selected_protein_pos != "All" and "Protein|position" in filtered_data.columns:
                filtered_data = filtered_data[filtered_data["Protein|position"] == selected_protein_pos]
        
        # 处理数据：创建Position列（与display_data_in_table方法保持一致）
        if 'Protein|position' in filtered_data.columns:
            # 分割Protein|position列
            protein_pos_split = filtered_data['Protein|position'].str.split('|', expand=True)
            if protein_pos_split.shape[1] >= 2:
                filtered_data['Protein'] = protein_pos_split[0]
                filtered_data['Position'] = protein_pos_split[1]
        
        return filtered_data
    
    

                                                                                                
import qdarkstyle
from qdarkstyle.light.palette import LightPalette

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyqt5", palette=LightPalette()))
    main_ui = MyDesigner()
    main_ui.show()
    # main_ui.showMaximized()
    app.exec_()
